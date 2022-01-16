from samp import (
    GetPlayerName,
    SendClientMessage,
)


def OnPlayerConnect(playerid):
    player_name = GetPlayerName(playerid)
    SendClientMessage(
        playerid,
        0xFF0000FF,
        f'Hello from Python, {player_name}!',
    )
