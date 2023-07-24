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


    @classmethod
    def from_registry_native(cls, player: BasePlayer) -> "Player":
        if isinstance(player, int):
            player_id = player

        if isinstance(player, BasePlayer):
            player_id = player.id

        player = cls._registry.get(player_id)

        if not player:
            cls._registry[player_id] = player = cls(player_id)

        return player


    @classmethod
    def using_registry(cls, func):
        """
        This should be used to make sure that our callback takes an instance of the class from the dictionary
        """
        @wraps(func)
        def from_registry(*args, **kwargs):
            args = list(args)
            args[0] = cls.from_registry_native(args[0])
            return func(*args, **kwargs)

        return from_registry


    @classmethod
    def delete_registry(cls, player: BasePlayer):
        """
        Removes an instance from the registry
        """
        playerid = player.id
        del cls._registry[playerid]
