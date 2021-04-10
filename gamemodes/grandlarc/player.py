from samp import *

class Player:
    """
    Creates a player class that contains all necessary variables during a session
    """
    def __init__(self, 
        playerid,
        city_selection = -1,
        has_city_selected = False,
        last_city_selection_tick = 0
    ):
        self.playerid = playerid
        self.city_selection = city_selection
        self.has_city_selected = has_city_selected
        self.last_city_selection_tick = 0
        pass
    pass
