from collections import defaultdict
from dataclasses import dataclass, field
from types import ModuleType
from typing import Any, Callable, Optional

from .names import names as builtin_callback_names


@dataclass
class HookedCallback:
    """A hooked callback. Assigned to python module on pysamp import.

    Calls main callback in "python" module, then registered module callbacks.
    """
    name: str
    original: Optional[Callable[..., None]]

    def __call__(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        """Call the real callback first, then all registered modules'."""
        if self.original:
            ret = self.original(*args, **kwargs)
            if ret is not None:
                return ret

        return registry.dispatch(self.name, *args, **kwargs)


@dataclass
class RegisteredCallback:
    """A registered callback. Wraps user-provided callables in the registry.

    Used to track the actual (SAMP) callback name a callable is registered to.
    """
    name: str
    callback: Callable[..., Optional[bool]]

    def __call__(
        self,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> Optional[bool]:
        return self.callback(*args, **kwargs)


@dataclass
class CallbackRegistry:
    """A registry for module callbacks. Gets populated on pysamp import."""
    _by_group: dict[str, list[RegisteredCallback]] = field(
        default_factory=lambda: defaultdict(list)
    )
    _by_callback_name: dict[str, list[RegisteredCallback]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def _register_module(self) -> None:
        """Register all callbacks in a module, called on import."""
        module = _path_hook._module_being_imported

        for name in builtin_callback_names:
            callback = getattr(module, name, None)

            if not callback:
                continue

            self.register_callback(name, callback)

    def register_callback(
        self,
        name: str,
        callback: Callable[..., None],
        group: Optional[Any] = None,
    ) -> None:
        """Register callback, called by register_module for each callback.

        group is used to group callbacks for later unregistration. If not
        specified, it will default to the name of the module currently being
        imported, or raise a ValueError if no import is taking place.
        """
        import python
        original = getattr(python, name, None)

        if not isinstance(original, HookedCallback):
            hook_callback(python, name)

        if not group:
            module = _path_hook._module_being_imported

            if not module:
                raise ValueError(
                    f'No module is being imported and group is {group!r}.'
                )

            group = module.__name__

        registered_callback = RegisteredCallback(name, callback)
        self._by_callback_name[name].append(registered_callback)
        self._by_group[group].append(registered_callback)

    def unregister(self, group: Any) -> None:
        """Unregisters all callbacks from given group.

        Raises KeyError if group doesn't exist.
        """
        callbacks = self._by_group.get(group)

        if not callbacks:
            raise KeyError(f'Group {group!r} does not exist.')

        by_name = self._by_callback_name

        for callback in callbacks:
            name = callback.name
            by_name[name].remove(callback)

    def dispatch(
        self,
        callback_name: str,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> None:
        """Dispatch an event to all registered module callbacks."""
        for callback in self._by_callback_name[callback_name]:
            ret = callback(*args, **kwargs)
            if ret is not None:
                return ret


def hook_callback(module: ModuleType, name: str) -> None:
    """Hooks a single callback from given module.

    Makes top level callbacks in the module use callbacks registry.
    """
    original = getattr(module, name, None)

    if isinstance(original, HookedCallback):
        return

    setattr(module, name, HookedCallback(name, original))


def hook() -> None:
    """Hooks all callbacks from user's "python" module.

    Hooks are later used to call registered callbacks inside submodules.
    """
    import python

    for name in builtin_callback_names:
        hook_callback(python, name)


registry = CallbackRegistry()

from . import _path_hook  # noqa
