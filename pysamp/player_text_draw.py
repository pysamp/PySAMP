from pysamp import (
    player_text_draw,
    player_text_draw_alignment,
    player_text_draw_background_color,
    player_text_draw_box_color,
    player_text_draw_color
)
from player import Player


class TextDraw(Player):
    def __init__(self, x: float, y: float, text: str) -> None:
        """Create a textdraw for the player.

        :param x: the x-position as a float on the screen.
        :param y: the y-position as a float on the screen.
        :param text: The text to show.
        :return: The textdraw ID that references this textdraw as an integer.

        .. note::
            - You need the textdraw ID later in order to remove or edit it.
            - The (0,0) coordinate is the top left coordinate for the textdraw\
                area based on a 640x448 "canvas" (irrespective of screen\
                resolution). If you plan on using\
                ``player.text_draw_alignment()`` with alignment 3 (right),\
                the x,y coordinate is the *top right* coordinate\
                for the textdraw.
            - This function only "creates" the textdraw, you must use\
                ``player.text_draw_show()`` to show it to a player.
            - It is recommended to use WHOLE numbers instead of decimal\
                positions when creating player textdraws to ensure resolution\
                friendly design.
            - Player-textdraws are automatically destroyed when a player\
                disconnects
            - Keyboard key mapping codes (such as ``~k~~VEHICLE_ENTER_EXIT~``)\
                Doesn't work beyond 255th character.

        .. warning::
            - If you choose values for y that are less than 1, the first\
                text row will be invisible and only the shadow is visible.
            - ``text`` must NOT be empty or the server will crash.\
                Use " " (a space) or _ (underscore) instead.
            - If the last character in the text is a space (" "),\
                the text will all be blank.
            - If part of the text is off-screen, the color of the text will\
                not show, only the shadow (if enabled) will.
        """
        return create_player_text_draw (self.id, x, y, text)

    def text_draw_destroy(self, text: str) -> bool:
        """Destroy a textdraw with a given textdraw ID.

        :param text: The textdraw ID to destroy.
        :return: Does not return anything in particular.
        """
        return player_text_draw_destroy(self.id, text)

    def text_draw_letter_size(self, text, x, y):
        """Sets the width and height of the letters in a player-textdraw.
        ___________

        - text    \t The ID of the player-textdraw to change the letter size of
        - Float:x \t Width of a char.
        - Float:y \t Height of a char.
        ___________

        Returns
        ------
        - Does not return any value

        Tips
        -----
        - Fonts appear to look the best with an X to Y ratio of 1 to 4 (e.g. if x is 0.5 then y should be 2).
        - When using this function purely for the benefit of affecting the textdraw box, multiply 'Y' by 0.135 to convert to TextDrawTextSize-like measurements
        Example
        -----

        No example available for player-textdraws, but check: https://sampwiki.blast.hk/wiki/PlayerTextDrawLetterSize


        """
        return player_text_draw_letter_size(self.id, text, x, y)

    def text_draw_text_size(self, text, x, y):
        """Change the size of a player-textdraw (box if PlayerTextDrawUseBox is enabled and/or clickable area for use with PlayerTextDrawSetSelectable).
        __________

        - text    \t The ID of the player-textdraw to set the size of.
        - Float:x \t The size on the X axis (left/right) following the same 640x480 grid as TextDrawCreate.
        - Float:y \t The size on the Y axis (up/down) following the same 640x480 grid as TextDrawCreate.
        __________

        Returns
        -----
        - Does not return any value

        Notes
        -----
        The x and y have different meanings with different player.text_draw_alignment values:
            1 (left): they are the right-most corner of the box, absolute coordinates.
            2 (center): they need to inverted (switch the two) and the x value is the overall width of the box.
            3 (right): the x and y are the coordinates of the left-most corner of the box
        Using font type 4 (sprite) and 5 (model preview) converts X and Y of this function from corner coordinates to WIDTH and HEIGHT (offsets).

        The TextDraw box starts 10.0 units up and 5.0 to the left as the origin (TextDrawCreate coordinate).

        This function defines the clickable area for use with PlayerTextDrawSetSelectable, whether a box is shown or not.


        Example
        -----
        No example available for player-textdraws, but check: https://sampwiki.blast.hk/wiki/PlayerTextDrawTextSize

        """
        return player_text_draw_text_size(self.id, text, x, y)

    def text_draw_alignment(self, text, alignment):
        """Set the text-alignment of a player-textdraw
        ___________

        - text   	The ID of the player-textdraw to set the alignment of.
        - alignment	1-left, 2-centered, 3-right
        ___________

        Returns
        ------
        - No sepcific value is returned

        Note
        ------
        - For alignment 2 (center) the x and y values of TextSize need to be swapped

        Example
        ----
        No example available for player-textdraws, but read more here: https://sampwiki.blast.hk/wiki/PlayerTextDrawAlignment
        """
        return player_text_draw_alignment(self.id, text, alignment)

    def text_draw_color(self, text, color):
        """Sets the text color of a player-textdraw

        You can also use Gametext colors in textdraws.

        *NOTE* The textdraw must be re-shown to the player in order to update the color.
        ________

        - text  \t Textdraw id to be changed color of, as an int
        - color \t Color in Hexadecimal format
        ________

        Returns
        -----
        - No value is returned

        Example
        -----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawColor
        """
        return player_text_draw_color(self.id, text, color)

    def text_draw_use_box(self, text, use):
        """Toggle the box on a player-textdraw.
        ________

        - text \t Textdraw ID
        - use  \t 1 to use a box, 0 to hide the box.
        ________

        Returns
        -----
        - No value is returned

        Example
        ----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawUseBox
        """
        return player_text_draw_use_box(self.id, text, use)

    def text_draw_box_color(self, text, color):
        """Sets the text color of a player-textdraw box
        ________

        - text  \t Textdraw id to be changed box color of, as an int
        - color \t Color in Hexadecimal format. Alpha (transparency) is supported
        ________

        Returns
        -----
        - No value is returned

        Example
        -----
        No example available for player-textdraws, but check out: https://sampwiki.blast.hk/wiki/PlayerTextDrawBoxColor
        """
        return player_text_draw_box_color(self.id, text, color)

    def text_draw_set_shadow(self, text, size):
        """Adds a shadow to the bottom-right side of the text in a player-textdraw. The shadow font matches the text font.
        _________

        - text	\tThe ID of the player-textdraw to change the shadow of
        - size	\tThe size of the shadow. 0 will hide the shadow.
        _________

        Returns
        ----
        1: successful
        0: failed - maybe player textdraw doesn't exist?

        Note
        ----
        - The shadow can be cut by the box area if the size is set too big for the area

        Example
        ----
        No example available for player-textdraws
        """
        return player_text_draw_set_shadow(self.id, text, size)

    def text_draw_set_outline(self, text, size):
        """Set the outline of a player-textdraw. The outline colour cannot be changed unless PlayerTextDrawBackgroundColor is used
        ___________

        - text\t\tThe ID of the player-textdraw to set the outline of
        - size\t\tThe thickness of the outline
        ___________

        Returns
        ----
        - No values are returned

        Example
        ----
        No example available for player-textdraws
        """
        return player_text_draw_set_outline(self.id, text, size)

    def text_draw_background_color(self, text, color):
        """| METHOD |
        _________

        - text	    The ID of the player-textdraw to set the background color of
        - color	    The color that the textdraw should be set to.
        _________
        Notes
        -----
        - If PlayerTextDrawSetOutline is used with size > 0, the outline color will match the color used in text_draw_background_color.
        - Changing the value of color seems to alter the color used in text_draw_color

        Returns
        ------
        - No value returned

        Example
        -------
        No example available for player-textdraws

        """
        return player_text_draw_background_color(self.id, text, color)

    def text_draw_font(self, text, font):
        """Change the font of a textdraw.

        See all fonts here: https://sampwiki.blast.hk/wiki/PlayerTextDrawFont
        ________

        - text \t The ID of the player-textdraw to change the font of
        - font \t There are four fonts, 0-3. Above 4 may crash the client.
        ________

        Returns
        -----
        - No value is returned

        """
        return player_text_draw_font(self.id, text, font)

    def text_draw_set_proportional(self, text, set):
        """Appears to scale text spacing to a proportional ratio.
        Useful when using PlayerTextDrawLetterSize to ensure the text has even character spacing.
        _______________

        - text \t The ID of the player-textdraw to set the proportionality of
        - set  \t 1 to enable proportionality, 0 to disable
        _______________

        Returns
        -----
        - No value is returned

        """
        return player_text_draw_set_proportional(self.id, text, set)

    def text_draw_set_selectable(self, text, set):
        """This method MUST be used BEFORE the textdraw is shown to the player!

        This method makes the textdraw selectable. `player.text_draw_text_size` defines the clickable area.

        _________

        - text	        The ID of the player-textdraw
        - set	        The color that the textdraw should be set to.
        _________


        Returns
        ----
        - No value returned

        Example
        ----
        No example available for player-textdraws.
        """
        return player_text_draw_set_selectable(self.id, text, set)

    def player_text_draw_show(self, text):
        """Use this method to show a player-textdraw for the player.

        - text \t\t The textdraw id to show for the player
        """
        return player_text_draw_show(self.id, text)

    def player_text_draw_hide(self, text):
        """Use this method to hide a player-textdraw for the player.

        - text\t\t The textdraw id to hide for the player

        Returns
        ----
        - No values returned
        """
        return player_text_draw_hide(self.id, text)

    def text_draw_hide_for_player(self, text):
        """This method hides a *global* textdraw for the player. To hide a player-textdraw, check `player.player_text_draw_hide`

        - text\t\tThe global textdraw id to hide for the player.

        Returns
        ----
        - No values returned
        """
        return text_draw_hide_for_player(self.id, text)

    def text_draw_set_string(self, text, string):
        """Update the shown text in the player-textdraw. You don't have to show the textdraw again in order to apply the changes

        ____________

        - text  	The ID of the textdraw to change
        - string	The new string for the TextDraw. Max length: 1023 characters
        ____________

        Returns
        -----
        - No values returned

        """
        return player_text_draw_set_string(self.id, text, string)

    def text_draw_set_preview_model(self, text, modelindex):
        """Sets a player textdraw 2D preview sprite of a specified model ID.
        ____________

        - text  	The ID of the textdraw to change
        - modelid	The modelid to show. Can be any valid object id.
        ____________

        Returns
        ----
        1: The function executed successfully. If an invalid model is passed 'success' is reported, but the model will appear as a yellow/black question mark.
        0: The function failed to execute. Player and/or textdraw do not exist.


        """
        return player_text_draw_set_preview_model(self.id, text, modelindex)

    def text_draw_set_preview_rot(self, text, fRotX, fRotY, fRotZ, fZoom=1.0):
        """Sets the rotation and zoom of a 3D model preview player-textdraw.
        __________________

        - text	\tThe ID of the player-textdraw to change.
        - Float:fRotX	The X rotation value.
        - Float:fRotY	The Y rotation value.
        - Float:fRotZ	The Z rotation value.
        - Float:fZoom	The zoom value, default value 1.0, smaller values make the camera closer and larger values make the camera further away.
        __________________

        Returns
        ------
        - No values returned
        """
        return player_text_draw_set_preview_rot(
            self.id, text, fRotX, fRotY, fRotZ, fZoom
        )

    def text_draw_set_preview_veh_col(self, text, color1, color2):
        """Set the color of a vehicle in a player-textdraw model preview (if a vehicle is shown).

        The textdraw MUST use the font TEXT_DRAW_FONT_MODEL_PREVIEW and be showing a vehicle, in order for this method to have an effect.

        _______________

        - text  	The ID of the player's player-textdraw to change.
        - color1	The color to set the vehicle's primary color to.
        - color2	The color to set the vehicle's secondary color to.
        _______________

        Returns
        ------
        - No values returned

        """
        return player_text_draw_set_preview_veh_col(self.id, text, color1, color2)