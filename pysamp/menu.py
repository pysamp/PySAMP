from typing import Optional
from pysamp import (add_menu_item, create_menu, destroy_menu, disable_menu,
                    disable_menu_row, get_player_menu, hide_menu_for_player,
                    is_valid_menu, set_menu_column_header,
                    show_menu_for_player)
from samp import INVALID_MENU


class Menu:
    def __init__(
        self,
        id: int
    ) -> None:
        self.id = id

    @classmethod
    def create(
        cls,
        title: str,
        columns: int,
        x: float,
        y: float,
        column_1_width: float,
        column_2_width: float = 0.0
    ) -> "Menu":
        """Create a new menu.

        :param str title: The menu title.
        :param int columns: How many columns the meny should have.
        :param float x: The X position on the screen (horizontally).
        :param float y: the Y position on the screen (vertically)
        :param float column_1_width: The width of the first column.
        :param optional float column_2_width: The width of the second column.
        :return: Returns an instance of :class:`~pysamp.menu.Menu`.
        """
        return cls(
            create_menu(
                title, columns, x, y, column_1_width, column_2_width
            )
        )

    def add_item(self, column: int, text: str) -> None:
        """Add a new menu item to the menu.

        :param int column: The columt to add to. (0 or 1)
        :param str text: The text to write. Max length: 31
        :return: No return value.

        .. note:: You can only have 12 items per menu.
            You can only add 8 color codes per one item.
        """
        if is_valid_menu(self.id):
            add_menu_item(self.id, column, text)
        return

    def destroy(self) -> None:
        """Destroy the menu.

        :return: No return value.
        """
        if is_valid_menu(self.id):
            destroy_menu(self.id)
        return

    def disable(self) -> None:
        """Disable the menu.

        :return: No return value.
        """
        if is_valid_menu(self.id):
            disable_menu(self.id)
        return

    def disable_row(self, row: int) -> None:
        """Disable one of the menu rows for all players.

        :param int row: The row to disable. Rows start at 0.
        :return: No return value.
        """
        if is_valid_menu(self.id):
            disable_menu_row(self.id, row)
        return

    @staticmethod
    def get_player_menu(player: "Player") -> Optional["Menu"]:
        """Figure out which menu a has last had open when none is currently
        open.

        :param Player player: The player to check last open menu for.
        :return: An instance of the menu. None if no menu was opened.
        """
        id = get_player_menu(player.id)
        if id == INVALID_MENU or id is None:
            return None
        return Menu(id)

    def hide_for_player(self, player: "Player") -> None:
        """Hide the menu for a player.

        :param Player player: The player you want to hide the menu for.
        :return: No return value.
        """
        if is_valid_menu(self.id):
            hide_menu_for_player(self.id, player.id)
        return

    def is_valid(self) -> bool:
        """Check if the menu is valid. Returns True or False."""
        return is_valid_menu(self.id)

from pysamp.player import Player  # noqa
