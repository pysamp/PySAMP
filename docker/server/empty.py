from pysamp.player import Player

from pysamp import callbacks  # needs to be before any submodules you make


# Called when a player connects.
@Player.on_connect
def on_player_connection(player: Player):
    player_name = player.get_name()
    player.send_client_message(
        0xFF0000FF,
        f'Hello from Python, {player_name}!',
    )


# required to make the events work. Needs to be on bottom:
callbacks.hook()
