from pysamp.player import Player as BasePlayer

class Player(BasePlayer):
    _registry = {}
    """
    Retrieve an instance from the registry, creating it if needed.
    """
    def __init__(self, playerid):
        super().__init__(playerid)
        self.city_selection = -1
        self.has_city_selected = False
        self.last_city_selection_tick = 0

    @classmethod
    def from_registry(cls, player):
        """
        This should be used to make sure that our callback takes an instance of the class from the dictionary
        """
        if isinstance(player, int):
            playerid = player
        
        if isinstance(player, BasePlayer):
            playerid = player.id
            
        player = cls._registry.get(playerid)

        if not player:
            cls._registry[playerid] = player = cls(playerid)

        return player

    @classmethod 
    def delete_registry(cls, player: BasePlayer):
        """
        Removes an instance from the registry
        """
        playerid = player.id
        del cls._registry[playerid]
