# PySAMP
Using PySAMP with your SA-MP server allows you to create gamemodes with the python language. All API-functions, callbacks and constants except timers and http functions can be accessed in python.
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
from pysamp.player import Player
from pysamp import (
  send_client_message_to_all
)


@Player.on_connect
def when_player_connects(player: Player):
    name = player.get_name()
    send_client_message_to_all(0x000000FF,  f'{name} has joined the server.')
```
 
As you can see, all referenced return values are removed and instead the method returns either a value or a tuple.
The corresponding python gamemode has to be saved as `python.py` module or a `python/` package of your server directory. For a more complete python gamemode example, please check `/docker/server/empty.py`.


# Getting Started

There are three different ways to install the plugin depending on your system. Recommended are the first two ways:

<details>
  <summary>Windows<br></summary>

  <hr>
Using PySAMP on a Windows machine is possible! Just make sure you have <b>32-bit Python</b> and the correct version that the plugin requires.

## Install correct python version
Install the correct version (written in the DLL name you downloaded). As of PySAMP `2.1.0`, this should be python version [`3.9.7`](https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe.). 64-bit or any other version will not work, and the plugin will not load.<br>

## Make a python module
The plugin will look for a module named `python` in your server root. That means you can either create `python.py` or `python/__init__.py`.

## Add PySAMP's API
In order to work with our v2.1 API, you need to copy the folder `pysamp` to your server root directory. It includes snake_case versions of the default SA-MP functions, and classes for various objects such as `Player`, `Vehicle`, `TextDraw` and so on. If you created a `python` folder in last step, you should now have the normal SA-MP server folders, plus the two new ones (python and pysamp).

## Server.cfg
1. Add `PySAMP.dll` to your `server.cfg` on the `plugins` line.
2. Add an (empty) gamemode to the `gamemodes` line. For example, use `bare` which is a default, empty gamemode. Please note that this is not mandatory and you should be able to run both a pawn and a python gamemode alongside each other just fine. However if you start from scratch, we strongly recommend you to not mix, as it gives you much better control over your gamemode.
  <hr>
</details>

<details>
  <summary>Using docker<br></summary>

  <hr>

## Run using docker
### Requirements
- Docker 20.10.0 or greater. Previous versions may work, but they are not tested. Read more [here](https://docs.docker.com/engine/install/) how to install docker on your specific Linux Distribution.
- Your user needs to be added to the docker group, so you don't have to run as sudo.

### How to get started?
With our docker setup, you can run your entire SA-MP server inside a docker container. Under `/docker/data` you will find a 0.3.7 server root folder as you would recognise it. Our docker setup builds the container, builds the PySAMP plugin, and afterwards uses the `/docker/data` directory to start up a SA-MP server for you.


1. If you haven't already, please clone the latest main branch of the [repository](https://github.com/habecker/PySAMP/tree/main).  You can clone the repository to your server using `git clone https://github.com/habecker/PySAMP.git`
2. Proceed to the `/docker` folder inside the repo, here you can find the docker-related files. Inspect the files if you need to know what they do in detail.
3. Next up, let us make the bash-scripts executable by running `chmod +x *.sh` inside the `/docker` folder.
4. Inside the same folder (`/docker`), run the SA-MP server by running `./run.sh`, and gently wait for the process to complete. This will build the docker container and start your server. `/docker/data` will appear.

### Default actions and notes
- If there are no existing `/docker/data` directory, it will be created. SA-MP server version 0.3.7-R2-1  will be downloaded and installed.
- If there is no .amx gamemode in `/docker/data/gamemodes`, the docker container will put one there to get the server started. If you have defined a different gamemode in `/docker/data/server.cfg`, the default .amx file will not be loaded, but instead the one you defined will.
- The [Crashdetect](https://github.com/Zeex/samp-plugin-crashdetect) plugin is added automatically, unless it already exists.
- Server starts at port 7777 and it is exposed at port 7777. If you change the port in the `/docker/data/server.cfg`, you will also need to change the docker arguments in `/docker/run.sh`. For example, if you want to run on port 8888, the last line should contain `-p 8888:8888/udp` instead of `-p 7777:7777/udp`.
- if the `/docker/data` directory gives you "permission denied" on linux when you try to edit something, it is because the docker image runs with root, and the files are not accessible for the host user. You can do `chmod` command on the folder to change the permissions to be more open, so that you can edit things in it.

  <hr>
</details>

<details>
  <summary>Manual Installation (Linux)<br></summary>
  <hr>

  1. Install the python version as written in the name of the file on the releases page. This should be version 3.10.4 as of PySAMP 2.1. (32 bit version is required, and it needs to be on $PATH)
  2. Copy the downloaded PySAMP.so to the plugins directory of your server. (If it has a weird name, just rename it to PySAMP.so)
  3. Copy `/docker/server/empty.py` to your server root directory, renamed as `python.py`
  4. Copy `pysamp` folder/module to your server root directory.
  5. Run the server and verify that the plugin has loaded in your logs. If not, make sure step 1-4. is done correctly. You need exact versions of python.
  
  <hr>
</details>

# Community
<img src="https://pics.ducky.rocks/images/2022/07/04/e6921f0f92a828fc9cc7346ebac9e149.png" alt="Discord Logo" width="80"/>

Join us over at [Discord](https://discord.gg/puw5VeQtbx)! You can join the discussion or even ask for help/support.

# Documentation
Documentation is generated using sphinx. Link to WIP documentation for v2.1 (temporary): https://pysamp.github.io/PySAMP/

# Thanks to
- SA:MP Team for developing SA:MP, especially [@Y-Less](https://github.com/Y-Less)
- [@Zeex](https://github.com/Zeex) for developing the SAMPGDK which is used by PySAMP
- Everyone who's involved in shaping and promoting PySAMP
- Python Software Foundation
