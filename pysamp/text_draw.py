from pysamp import (
    text_draw_alignment,
    text_draw_background_color,
    text_draw_box_color,
    text_draw_color,
    text_draw_create,
    text_draw_destroy,
    text_draw_font,
    text_draw_hide_for_all,
    text_draw_hide_for_player,
    text_draw_letter_size,
    text_draw_set_outline,
    text_draw_set_preview_model,
    text_draw_set_preview_rot,
    text_draw_set_preview_veh_col,
    text_draw_set_proportional,
    text_draw_set_selectable,
    text_draw_set_shadow,
    text_draw_set_string,
    text_draw_show_for_all,
    text_draw_text_size,
    text_draw_use_box,
)
from pysamp.player import Player


class Textdraw:
    def __init__(self, x: float, y: float, text):
        self.id = text_draw_create(x, y, text)

    def destroy(self):
        return text_draw_destroy(self.id)

    def letter_size(self, x: float, y: float):
        return text_draw_letter_size(self.id, x, y)

    def text_size(self, x: float, y: float):
        return text_draw_text_size(self.id, x, y)

    def alignment(self, alignment):
        return text_draw_alignment(self.id, alignment)

    def color(self, color):
        return text_draw_color(self.id, color)

    def use_box(self, use):
        return text_draw_use_box(self.id, use)

    def box_color(self, color):
        return text_draw_box_color(self.id, color)

    def set_shadow(self, size):
        return text_draw_set_shadow(self.id, size)

    def set_outline(self, size):
        return text_draw_set_outline(self.id, size)

    def background_color(self, color):
        return text_draw_background_color(self.id, color)

    def font(self, font):
        return text_draw_font(self.id, font)

    def set_proportional(self, set):
        return text_draw_set_proportional(self.id, set)

    def set_selectable(self, set):
        return text_draw_set_selectable(self.id, set)

    def show_for_all(self):
        return text_draw_show_for_all(self.id)

    def hide_for_all(self):
        return text_draw_hide_for_all(self.id)

    def set_string(self, string: str):
        return text_draw_set_string(self.id, string)

    def set_preview_model(self, modelindex):
        return text_draw_set_preview_model(self.id, modelindex)

    def set_preview_rot(
        self, rotation_x: float, rotation_y: float, rotation_z: float, zoom=1.0
    ):
        return text_draw_set_preview_rot(
            self.id, rotation_x, rotation_y, rotation_z, zoom
        )

    def set_preview_veh_col(self, color1, color2):
        return text_draw_set_preview_veh_col(self.id, color1, color2)

    def hide_for_player(self, player: "Player") -> bool:
        """This method hides a global textdraw for the player.
        """
        return text_draw_hide_for_player(self.id, player.id)
