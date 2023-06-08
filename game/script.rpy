# Define dialog bleeps here
init python:
    def protagBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/protag.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def liBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/li.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def qirinBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/qirin.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def reapBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/reaper.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def genericBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/generic.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define protag = Character('Jonghyun', image="protag", color="#79be9e", callback=[protagBleep,name_callback], cb_name = "protag")
define li = Character('Noel', image="li", color="#b22673", callback=[liBleep, name_callback], cb_name="li")
define qirin = Character('[qirinName]', image="qirin", color="#4e6e8f", callback=[qirinBleep,name_callback], cb_name="qirin")
define reaper = Character('[reaperName]', image="reaper", color="#b85b6b", callback=[reapBleep,name_callback], cb_name="reaper")
define narrator = Character(callback=name_callback, cb_name=None)
define generic = Character('[genericName]', color="#918196", callback=[genericBleep,name_callback], cb_name=None)

# generic black background
image black = Solid("#000")

# define default variables here
default truthEnding = 0
default desireEnding = 0
default jokeEnding = 0

default qirin_truth = False
default qirin_desire = False
default qirin_joke = False

default reaper_truth = False
default reaper_desire = False
default reaper_joke = False

default li_truth = False
default li_desire = False
default li_joke = False

# The game starts here.
label start():
    # these are "temp" variables that change in the story regardless of player input
    $ genericName = ""
    $ qirinName = "Customer"
    $ reaperName = "Unknown Caller"

    stop music fadeout 1.0

    call scene01 from _call_scene01
    call scene02 from _call_scene02
    call scene03 from _call_scene03
    call scene04 from _call_scene04
    call scene05 from _call_scene05
    call scene06 from _call_scene06
    call scene07 from _call_scene07
    call scene08 from _call_scene08
    call scene09 from _call_scene09
    call scene10 from _call_scene10
    call scene11 from _call_scene11
    call scene12 from _call_scene12
    call scene13 from _call_scene13
    call scene14 from _call_scene14

    jump end

# game endings here
label end():
    
    call generic_ending from _call_generic_ending

    if truthEnding >= 2:
        call truth_ending from _call_truth_ending
    elif desireEnding >= 2:
        call desire_ending from _call_desire_ending
    elif jokeEnding >= 2:
        call joke_ending from _call_joke_ending
    else:
        call generic_ending.cafe from _call_generic_ending_cafe

    call screen credits

    return
