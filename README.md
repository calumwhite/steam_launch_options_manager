# steam_launch_options_manager
Allows changing the steam launcher options with one command and on going maintenance.

## Why?
My reason for creating this was that I am running a Nvidia optimus equipped laptop with POP os (Ubuntu based and great). To get steam games running on the discrete graphics card I had to change the launcher options for each game inside steam. Effort and needs ongoing maintenance.

## !!!ISSUES!!!
Linux Only

This is new and poorly tested. That said it does create a backup of the config at $XDG_DATA_HOME/steam_launch_options_manager defaulting to $HOME/.config/steam_launch_options_manager. If .localconfig.vdf was corrupted or deleted it should be not a big issue only things like big picture control binds and launch options would be lost. PLS don't sue me either way.

This is not tested on any non debian based distros and might fail to autodetect path. Manually entering the path should still work.

## Installation
Assuming as system with python3 already installed.
Thus install pip (eg on debian based)

```
sudo apt update
sudo apt install python3-pip
```

Then install vdf

```
pip3 install --user vdf
```

Git clone the repo into.
```
/usr/share/pyshared
```

Copy the file called

```
steam_launch_options_manager
```

into the folder

```
/usr/local/bin
```

this will require sudo privileges. Then mark as executable either using right click, properties, permissions or using chmod.

Recommended:
Add graphical shortcut. This won't enable initalisation but will enable repeated use.

Copy the file


```
steam_launch_options_manager.desktop
```

into

```
/usr/share/applications
```
## Usage
Run in the terminal

```
steam_launch_options_manager --initialise
```

and follow the onscreen prompts.

The option enable optimus adds  __NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia to the beginning of the launch options.

After initalising the rules the script will run for all steam games on your account. And then steam will launch.

Running for maintenance:

Use the GUI shortcut or

```
steam_launch_options_manager
```

Tip: Run steam every time with the gui shortcut to steam_launch_options_manager, to keep your config across all games always current.

## Troubleshoot
Make sure steam has not got any processes open restarting is an easy way to achieve this.

## TODO
Multiple accounts only the first account is modified at current

Windows support

Test on non Debian based systems. (Please let me know if this works or if you have any issues)

Non-steam games in steam launcher

Game by game support

Icon for menu shortcuts
