import functools
from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

from samp import SendClientMessage  # type: ignore

from .callbacks import registry


class CommandHandler(Protocol):
    def __call__(self, playerid: int, *args: str) -> None: ...


class Validator(Protocol):
    """Return True if playerid is allowed, False otherwise."""
    def __call__(self, playerid: int) -> bool: ...


class Message(Protocol):
    text: str
    color: int

    def send(self, playerid: int) -> None: ...


@dataclass
class Command:
    triggers: set[str]
    handler: CommandHandler
    split_args: bool
    requires: tuple[Validator, ...]
    error_message: Message

    def handle(self, playerid: int, args_text: str) -> None:
        """Call handler, doing validation and argument splitting if needed."""
        for validator in self.requires:
            if not validator(playerid):
                self.error_message.send(playerid)
                return

        args = [
            arg
            for arg in (
                [args_text] if not self.split_args
                else args_text.split(' ')
            )
            if arg
        ]
        self.handler(playerid, *args)


@dataclass
class CommandDispatcher:
    _commands: list[Command] = field(default_factory=list)
    _commands_by_trigger: dict[str, Command] = field(default_factory=dict)

    def _register(self, command: Command) -> None:
        """Register a Command to be triggered later on.

        Don't use this directly: prefer the @cmd decorator which does extra
        checks in addition to looking much better.
        """
        self._commands.append(command)
        self._commands_by_trigger.update({
            trigger: command
            for trigger in command.triggers
        })

    def handle(self, playerid: int, command_text: str) -> bool:
        """Attempt to handle command_text sent by playerid.

        Returns True if a Command was found, False otherwise.
        Should be used in OnPlayerCommandText.
        """
        trigger, _, args_text = command_text.partition(' ')
        command = self._commands_by_trigger.get(trigger)

        if not command:
            UNKNOWN_COMMAND.send(playerid)
            return False

        command.handle(playerid, args_text)

        return True


@dataclass
class BaseMessage:
    """Bare message class implementing Message protocol."""
    text: str
    color: int

    def send(self, playerid: int) -> None:
        SendClientMessage(playerid, self.color, self.text)


def _NO_FUNCTION(playerid: int, *args: str) -> None: ...


DEFAULT_ERROR_MESSAGE = BaseMessage(
    text='You are not allowed to use this command.',
    color=0xFF0000FF,
)
UNKNOWN_COMMAND = BaseMessage(
    text='SERVER: Unknown command.',
    color=0xFFFFFFFF,
)


def cmd(
    function: CommandHandler = _NO_FUNCTION,
    /,
    *,
    aliases: tuple[str, ...] = (),
    use_function_name: bool = True,
    split_args: bool = True,
    requires: tuple[Validator, ...] = (),
    error_message: Message = DEFAULT_ERROR_MESSAGE,
) -> Callable[[Any], Any]:
    """Decorate a command handler to register it with the given options.

    function: The command handler to register. Useful when there is no need for
        other arguments, one can use the bare decorator without calling it.
    aliases: Alternative command names to trigger the handler with. If this is
        empty and use_function_name is False, a ValueError is raised.
    use_function_name: Whether to use the function name as a command name to
        trigger the handler with. If this is False and aliases is empty, a
        ValueError is raised.
    split_args: Whether command arguments should be passed to the function as
        individual string arguments (split by whitespace) or as a single
        string argument (all text after the issued command).
    requires: Tuple of callables implementing the Validator protocol. If
        specified, they will be called in order with a playerid as argument
        and should return False if the player is not allowed to use this
        command, in which case error_message will be issued.
    error_message: An object implementing the Message protocol. It will be sent
        to the player in case they are not allowed to use this command.
    """
    if function is _NO_FUNCTION:
        return functools.partial(
            cmd,
            aliases=aliases,
            use_function_name=use_function_name,
            split_args=split_args,
            requires=requires,
            error_message=error_message,
        )

    triggers = set()

    if use_function_name:
        # See https://github.com/python/mypy/issues/12795
        triggers.add(function.__name__)  # type: ignore

    triggers.update(aliases)

    if not triggers:
        raise ValueError('Unable to register a command without triggers.')

    dispatcher._register(Command(
        triggers={f'/{trigger}' for trigger in triggers},
        handler=function,
        split_args=split_args,
        requires=requires,
        error_message=error_message,
    ))

    return function


dispatcher = CommandDispatcher()
registry.register_callback(
    'OnPlayerCommandText',
    dispatcher.handle,
    'pysamp.commands',
)
