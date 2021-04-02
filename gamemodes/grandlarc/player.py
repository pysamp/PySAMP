from samp import *

class PlayerVars(Player):

    def __init__(
        self, playerid, 
        city_selection = -1,
        has_city_selected = False,
        last_city_selection_tick = 0
    ):
        self.city_selection = city_selection
        self.has_city_selected = has_city_selected
        self.last_city_selection_tick = 0
        super().__init__(playerid) # To get all functionality from the parent "Player" class in samp.py
        
    @property
    def city_selection(self):
        return self.city_selection
        
    @city_selection.setter
    def city_selection(self, value):
        self.city_selection = value
    
