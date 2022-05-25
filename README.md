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
from samp import GetPlayerName, SendClientMessageToAll

def OnPlayerConnect(playerid):
    name = GetPlayerName(playerid)
    SendClientMessageToAll(0xFF0000FF, f'{name} has joined the server.')
```

As you can see, all referenced return values are removed and instead the method returns either a value or a tuple.
The corresponding python gamemode has to be saved as `python.py` module or a `python/` package of your server directory.


# Getting Started

There are three different ways to install the plugin depending on your system. Recommended and supported are the first two ways:

<details>
  <summary>Windows<br></summary>

  <hr>
  Using PySAMP on a Windows machine is fairly easy.
  Follow our instructions <a href="https://github.com/pysamp/PySAMP/wiki/How-to-get-started-with-python-3.9.7-on-Windows/">here</a> in order to install <b>32 bit</b> Python, matching the version in the DLL name you downloaded. As of 2.0.1, this should be version 3.9.7. 64-bit or any other version will not work, and the plugin will not load.
  <hr>
</details>

<details>
  <summary>Linux / OS independent<br></summary>

  <hr>

## Run using docker
### Requirements
- Docker 20.10.0 or greater. Previous versions may work, but they are not tested. Read more [here](https://docs.docker.com/engine/install/) how to install docker on your specific Linux Distribution
- Your user needs to be added to the docker group

### How to get started?
With our docker setup, you can run your entire SA-MP server inside a docker container. Under `/docker/data` you will find a 0.3.7 server root folder as you would recognise it. Our docker setup builds the container, generates the PySAMP runtime / plugin, and afterwards uses the `/docker/data` directory to start up a SA-MP server for you.


1. If you haven't already, please clone the latest main branch of the [repository](https://github.com/habecker/PySAMP/tree/main).  You can clone the repository to your server using `git clone https://github.com/habecker/PySAMP.git`
2. Proceed to the `/docker` folder inside the repo, here you can find the docker-related files. Inspect the files if you need to know what they do in detail.
3. Next up, let us make the bash-scripts executable by running `chmod +x *.sh` inside the `/docker` folder.
4. From the same folder (`/docker`), run the SA-MP server by running `./run.sh`, and gently wait for the process to complete. This will build the docker container and start your server.

### Default actions and notes
- If there are no existing `/docker/data` directory, it will be created. SA-MP server version 0.3.7-R2-1  will be downloaded and installed.
- If there is no gamemode in `/docker/data/gamemodes`, the docker container will put one there to get the server started. If you have defined a different gamemode in `/docker/data/server.cfg`, this file will not be loaded.
- The [Crashdetect](https://github.com/Zeex/samp-plugin-crashdetect) plugin is added automatically, unless it already exists.
- Server starts at port 7777 and it is exposed at port 7777. If you change the port in the `/docker/data/server.cfg`, you will also need to change the docker arguments in `/docker/run.sh`. For example, if you want to run on port 8888, the last line should contain `-p 8888:8888/udp` instead of `-p 7777:7777/udp`.

  <hr>
</details>

<details>
  <summary>Manual Installation (not recommended, unsupported)<br></summary>
  <hr>
  1. Install Python 3.9.7 (32 bit version is <b>required</b>)
  1. Copy the PySAMP.so to the plugins directory of your server
  1. Copy `/docker/server/empty.py` to your server directory, renamed as `python.py`
  <hr>
</details>

# Community
<img src="https://pics.ducky.rocks/images/2019/12/10/imaged9f253a7387d8393.th.png" alt="Discord Logo" width="40"/> 

Join us over at [Discord](https://discord.gg/puw5VeQtbx)! You can join the discussion or even ask for help/support.

# Thanks to
- [@dennorske](https://github.com/dennorske) for reviving this project
- SA:MP Team for developing SA:MP, especially [@Y-Less](https://github.com/Y-Less)
- [@Zeex](https://github.com/Zeex) for developing the SAMPGDK which is used by PySAMP
- Python Software Foundation
