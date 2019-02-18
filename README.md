# PySAMP
Using PySAMP in your SA-MP server allows you to create gamemodes with the python language. All API-functions, callbacks and constants except timers and http functions can be accessed in python. 
In case of the call-by-reference functions like ```GetPlayerName``` are returning the value instead of using a reference, since call-by-reference isn't possible in python.
The following example shows the difference.

```C
public OnPlayerConnect(playerid)
{
  new name[MAX_PLAYER_NAME], string[MAX_PLAYER_NAME + 24];
  GetPlayerName(playerid, name, MAX_PLAYER_NAME);
  format(string, sizeof(string), "%s has joined the server.", name);
  SendClientMessageToAll(0x000000FF, string);
}
```

```python
from pysamp import *

def OnPlayerConnect(playerid):
    name = GetPlayerName(playerid, Const('MAX_PLAYER_NAME'))
    SendClientMessageToAll(0x000000FF,  '%s has joined the server.'.format(name))
    return 1
```

As you can see, all referenced return values are removed and instead the method returns either a value or a tuple.
The corresponding python gamemode has to be saved as `gamemode.py` in a `python/` subfolder of your server directory.

# Using
Make sure, that you installed the 32-bit Python 3.5m version on your server!

# Compiling
If the uploaded binaries don't suite your needs, you might have to compile the project on your own. 
You can also create an issue, so I can compile it for your system, just mention your system architecture.

So, if you want to compile it on your own, note the following things.
- You read the [SAMPGDK tutorial](https://github.com/Zeex/sampgdk/wiki/Setting-up-GDK-with-CMake).
- Python (3.5 Linux)/(3.6 Windows) (32 bit version!) is installed on your computer
- You copied the sampsdk and sampgdk files into the src folder, as defined in CMakeLists.txt

Use cmake to create a project and then compile it as you're used to it.

# Thanks to
- SA:MP Team for developing SA:MP
- Zeex for developing the SAMPGDK which is used by pySAMP
- Python Software Foundation
