import sys
import os
from cx_Freeze import setup, Executable


def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


packages = ["pygame", "psutil"]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter']
files = ["AUDIO/MUSIC/Big Chillum - David Starfire.wav",
         "AUDIO/MUSIC/Jumping Off - David Starfire.wav",
         "AUDIO/MUSIC/Knight Riddum - David Starfire.wav",
         "AUDIO/MUSIC/Rahu - David Starfire.wav",
         "AUDIO/MUSIC/The One (feat. Alex Grey and Joaqopelli) (Original Mix) - David Starfire.wav",
         "BACKDROPS/joog_shooters_instructions.png",
         "BACKDROPS/joog_shooters_instructions2.png",
         "BACKDROPS/joog_shooters_title.png",
         "BACKDROPS/Pixel-Art-BackGround1.png",
         "BACKDROPS/Pixelated_BG1.png",
         "BACKDROPS/Pixelated_BG2.png",
         "BACKDROPS/Pixelated_BG3.png",
         "BACKDROPS/Smooth_pixel_BG.png",
         "BACKDROPS/synth-wave-retro-city-landscape.png",
         "BUTTONS/checked_box-01.png",
         "BUTTONS/info_icon.png",
         "BUTTONS/music_play.png",
         "BUTTONS/music_play_hover.png",
         "BUTTONS/music_previous.png",
         "BUTTONS/music_previous_hover.png",
         "BUTTONS/music_skip.png",
         "BUTTONS/music_skip_hover.png",
         "BUTTONS/PlaylistBtn.png",
         "BUTTONS/QuitGameBtn.png",
         "BUTTONS/QuitGameBtn_hover.png",
         "BUTTONS/RestartBtn.png",
         "BUTTONS/RestartBtn_hover.png",
         "BUTTONS/RsmBtn.png",
         "BUTTONS/RsmBtn_hover.png",
         "BUTTONS/unchecked_box-01.png",
         "BUTTONS/X_Btn-01.png",
         "SPRITES/?box.png",
         "SPRITES/GunIcon1.png",
         "SPRITES/GunIcon2.png",
         "SPRITES/Joog_turret.png",
         "SPRITES/p1_weapon_slash.png",
         "SPRITES/p2_weapon_slash.png",
         "SPRITES/pause_menu_border.png",
         "SPRITES/platform_tiles_sheet_blue.png",
         "SPRITES/Player1_Large.png",
         "SPRITES/Player2_Large.png",
         "SPRITES/Sprite1_sheet.png",
         "SPRITES/Sprite2_sheet.png",
         "SPRITES/SwordIcon1.png",
         "SPRITES/SwordIcon2.png",
         "SPRITES/weapons_sheet.png",
         ]

files_with_path = []
for file in files:
    files_with_path.append(find_data_file(file))

base = None
if sys.platform == "win32":
    base = "Win32GUI"

Target = Executable(
    script="game.py",
    base=base,
    icon="Icon.ico"
)

setup(
    name="Joog Shooters",
    version="1.1.4",
    author="Seay Zagar",
    description="No Description",
    options={"build_exe": {"include_files": files_with_path,
                           "excludes": excludes,
                           "packages": packages,
                           }
             },
    executables=[Target]
)
