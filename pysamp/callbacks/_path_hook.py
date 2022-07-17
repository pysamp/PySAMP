import os
import sys
import warnings
from importlib.machinery import SOURCE_SUFFIXES, FileFinder, SourceFileLoader
from types import ModuleType

from . import registry


_module_being_imported = None


class PySAMPImportWarning(RuntimeWarning):
    """Gets issued if it seems like import order is incorrect."""


class PySAMPLoader(SourceFileLoader):
    """Custom loader that registers module callbacks on import."""
    def exec_module(self, module: ModuleType) -> None:
        global _module_being_imported
        _module_being_imported = module
        super().exec_module(module)
        registry._register_module()
        _module_being_imported = None


class PySAMPFinder(FileFinder):
    """Custom finder that ignores modules outside `python` package."""
    @classmethod
    def path_hook(cls, *loader_details):
        closure = super().path_hook(*loader_details)
        def path_hook_for_PySAMPFinder(path):
            """Path hook for pysamp.callbacks._path_hook.PySAMPFinder."""
            if not any(
                path == os.path.join(sys_path, 'python')
                for sys_path in sys.path
            ):
                raise ImportError(
                    'Only pysamp submodules are supported.',
                    path=path
                )
            return closure(path)

        return path_hook_for_PySAMPFinder


for module_name in sys.modules:
    if module_name.startswith('python.'):
        warnings.warn(
            f'Module {module_name} was imported before pysamp, '
            'this is probably not what you want.',
            category=PySAMPImportWarning,
        )

sys.path_hooks.insert(
    0,
    # See typeshed issues #7085 and #7086
    PySAMPFinder.path_hook((PySAMPLoader, SOURCE_SUFFIXES))  # type: ignore
)
