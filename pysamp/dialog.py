from pysamp import (
    show_player_dialog
)
from typing import Dict, List


class Dialog:
    """Class to create and show dialogs.

    A dialog is a menu that the player can interact with.
    To create a new dialog, use :meth:`create`.

    The player will see the dialog when you do :meth:`show`. The Dialog class
    keeps track of shown dialogs to a player, and also the last shown
    dialog, which is used on the dialog response event.
    """

    _id: int = 32768  # just a random dialog ID that will be used on SA-MP
    _by_player: Dict["Player", "Dialog"] = {}

    def __init__(
        self,
        type: int,
        title: str,
        content: str,
        button_1: str,
        button_2: str,
        shown_for: List["Player"] = []
    ) -> None:
        self.type = type
        self.title = title
        self.content = content
        self.button_1 = button_1
        self.button_2 = button_2
        self.shown_for = shown_for

    @classmethod
    def create(
        cls,
        type: int,
        title: str,
        content: str,
        button_1: str,
        button_2: str
    ) -> "Dialog":
        """Create/prepare a dialog for use later.

        Use :meth:`show` to show the dialog to a player after creating it.

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
            type,
            title,
            content,
            button_1,
            button_2
        )

    def show(self, for_player: "Player") -> None:
        """Show the dialog created with :meth:`create` to a specific player.

        :param Player for_player: The player you want to show
            the dialog to.
        :return: No return value.

        .. note:: You can only show one dialog to a player at a time.
        """

        show_player_dialog(
            for_player.id,
            Dialog._id,  # we only occupy one ID on SA-MP side.
            self.type,
            self.title,
            self.content,
            self.button_1,
            self.button_2
        )
        Dialog._by_player[for_player] = self
        self.shown_for.append(for_player)
        return

    @staticmethod
    def hide(for_player: "Player") -> None:
        """Shows a dialog with ID -1 to hide open dialog.

        :param Player for_player: The player you'd like to hide open
            dialogs for.
        :return: No return value.
        """
        show_player_dialog(for_player.id, -1, 0, "", "", "", "")
        Dialog._by_player.pop(for_player, None)
        return


from pysamp.player import Player  # noqa