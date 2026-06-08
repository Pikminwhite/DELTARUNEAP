# DELTARUNE Archipelago Setup Guide

## Required Software

- DELTARUNE from the [Steam page](https://store.steampowered.com/app/1671210/)
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)
- DELTARUNE APWorld from the [Releases Page](https://github.com/theemeraldsword85/DELTARUNEAP/releases)

## Recommended Software

- Universal Tracker APWorld from the [UT Releases Page](https://github.com/FarisTheAncient/Archipelago/releases)

## Installation

### Patching the game

**Require DELTARUNE 1.04 vanilla *(last public branch on Steam)***

Start the DELTARUNE client from your Archipelago folder or the Archipelago app and input `/auto_patch <Your DELTARUNE Install Directory>` at the bottom.

If you game is a steam install on you `C:` drive, you can use `/auto_patch steaminstall` or if it's a downloaded depot `/auto_patch steamdepot`

If you're not sure, you can easily find the directory by opening the DELTARUNE directory through Steam by right-clicking DELTARUNE in your library and selecting `Manage -> Browse local files`. Then, on Windows you can see the directory that you need at the top of the window that opens.

#### Linux users

**Linux is currently not supported as it will disconnect you from the server few seconds after connection**

The Linux installation is mostly similar, however, DELTARUNE will be installed on Steam as the Linux 
variant.

Since this randomizer only supports the Windows version, we must fix this, by right-click the game in Steam, going to `Properties -> Compatibility`, and checking `Force the use of a specific Steam Play compatibility tool`.

This downloads the Windows version of DELTARUNE to use instead of the Linux version. If the play button is greyed out in Steam, be sure to go to `Settings -> Compatibility` and toggle `Enable Steam Play for all other titles`.

### Create your YAML

Your YAML file is the settings of your Archipelago world.

You can create it with the `Option Creator` in the Archipelago Launcher or with `Generate Template Options` after what you can find the default YAML and other presets in `<Your Archipelago folder Path>/Players` after what you can manually edit.

### Connect to the Multiworld

Open your patched DELTARUNE version and choose `Change  connection info` then input your host, port, slot and password is existing.

You can copy/paste directly `host:port` into the host slot.

If you can to change the preview items color, it's configurable by switching menu with left/right arrow key.

You can eventualy open the DELTARUNE Text Client in the Archipelago Launcher to be able to use Text commands and Universal Tracker features.

#### Linux users

**On Steam (via Proton)**: This assumes the game is in a Steam Library folder.  Right-click DELTARUNE, go to `Manage -> 
Browse Local Files`. Go up the directories to the `steamapps` folder, open `compatdata/1671210` (1671210 is the "magic number" for
DELTARUNE in Steam).  Save data from here is at `/pfx/drive_c/users/steamuser/AppData/Local/DELTARUNE`.

**Through WINE directly**: This depends on the prefix used.  If it is default, then the save data is located at
`/home/USERNAME/.wine/drive_c/users/USERNAME/AppData/Local/DELTARUNE`.