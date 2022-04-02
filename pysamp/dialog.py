from pysamp import (
    show_player_dialog
)


class Dialog:
    """Class to create and show dialogs.

    A dialog is a menu that the player can interact with.
    To create a new dialog, use :meth:`create`.
    """
    def __init__(
        self,
        id: int,
        type: int,
        title: str,
        content: str,
        button_1: str,
        button_2: str
    ) -> None:
        self.id = id
        self.type = type
        self.title = title
        self.content = content
        self.button_1 = button_1
        self.button_2 = button_2

    @classmethod
    def create(
        cls,
        id: int,
        type: int,
        title: str,
        content: str,
        button_1: str,
        button_2: str
    ) -> "Dialog":
        """Create/prepare a dialog for use later.

        Use :meth:`show` to show the dialog to a player after creating it.

        :param id: Give the dialog an ID. You use this ID to track the object
            and to handle logic when the response event is called.
        :param type: The type of dialog you want to make. There are 6 different
            types: ``DIALOG_STYLE_MSGBOX``, ``DIALOG_STYLE_INPUT``,
            ``DIALOG_STYLE_LIST``, ``DIALOG_STYLE_PASSWORD``,
            ``DIALOG_STYLE_TABLIST``and ``DIALOG_STYLE_TABLIST_HEADERS``.
        :param title: The dialog title show at top.
        :param content: The content of the dialog.
        :param button_1: The positive dialog response button. Can't be longer
            than 8 characters, else it looks weird.
        :param button_2: The second button, negative response.
            If it is left empty, it will be hidden from the dialog.
        :return: This classmethod creates a new instance of :class:`Dialog`.
        """
        return cls(
            id,
            type,
            title,
            content,
            button_1,
            button_2
        )

    def show(self, player: "Player") -> None:
        """Show the dialog created with :meth:`create` to a specific player.

        :param player: The :class:`Player` you want to show the dialog to.
        :return: No return value

        You can only show one dialog to a player at a time.
        """
        show_player_dialog(
            player.id,
            self.id,
            self.type,
            self.title,
            self.content,
            self.button_1,
            self.button_2
        )
        return

from pysamp.player import Player  # noqa