from PySAMP import (
    gang_zone_create,
    gang_zone_destroy,
    gang_zone_flash_for_all,
    gang_zone_flash_for_player,
    gang_zone_hide_for_all,
    gang_zone_hide_for_player,
    gang_zone_show_for_all,
    gang_zone_show_for_player,
    gang_zone_stop_flash_for_all,
    gang_zone_stop_flash_for_player,
)
from Player import Player


class GangZone:
    def __init__(self, minx: float, miny: float, maxx: float, maxy: float):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.id = gang_zone_create(minx, miny, maxx, maxy)

    # TODO: Check this,
    # Not sure if this is right. I want to tell the server the object is no longer needed.
    def __del__(self):
        gang_zone_destroy(self.id)

    def show_for_player(
        self, player: Player, color: int
    ):  # yes, swapped places on args
        return gang_zone_show_for_player(player.id, self.id, color)

    def show_for_all(self, color: int):
        return gang_zone_show_for_all(self.id, color)

    def hide_for_player(self, player: Player):  # yes, swapped places on args
        return gang_zone_hide_for_player(player.id, self.id)

    def hide_for_all(self):
        return gang_zone_hide_for_all(self.id)

    def flash_for_player(
        self, player: Player, flashcolor: int
    ):  # yes, swapped places on args
        return gang_zone_flash_for_player(player.id, self.id, flashcolor)

    def flash_for_all(self, flashcolor: int):
        return gang_zone_flash_for_all(self.id, flashcolor)

    def stop_flash_for_player(self, player: Player):  # yes, swapped places on args
        return gang_zone_stop_flash_for_player(player.id, self.id)

    def stop_flash_for_all(self):
        return gang_zone_stop_flash_for_all(self.id)
