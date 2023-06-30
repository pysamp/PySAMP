from pysamp.player import Player as BasePlayer
from functools import wraps

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


    def using_registry(func):
        """
        This should be used to make sure that our callback takes an instance of the class from the dictionary
        """
        @wraps(func)
        def from_registry(*args, **kwargs):
            args = list(args)
            args[0] = Player.from_registry(args[0])
            return func(*args, **kwargs)

        return from_registry


    @classmethod
    def delete_registry(cls, player: BasePlayer):
        """
        Removes an instance from the registry
        """
        playerid = player.id
        del cls._registry[playerid]
