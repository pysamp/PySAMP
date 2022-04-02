from pysamp import (add_menu_item, create_menu, destroy_menu, disable_menu,
                    disable_menu_row, get_player_menu, hide_menu_for_player,
                    is_valid_menu, set_menu_column_header,
                    show_menu_for_player)


class Menu:
    def __init__(
        self,
        id,
        title: str,
        columns: int,
        x: float,
        y: float,
        column_1_width: float,
        column_2_width: float = 0.0
    ) -> None:
        self.id = id
        self.title = title
        self.columns = columns
        self.x = x
        self.y = y
        self.column_1_width = column_1_width
        self.column_2_width = column_2_width

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
        :return: Returns an instance of :class:`Menu`.
        """
        return cls(
            create_menu(
                title, columns, x, y, column_1_width, column_2_width
            ),
            title,
            columns,
            x,
            y,
            column_1_width,
            column_2_width
        )


from pysamp.player import Player  # noqa
