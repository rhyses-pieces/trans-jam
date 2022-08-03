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

# The game starts here.
label start():
    # these are "temp" variables that change in the story regardless of player input
    $ genericName = ""
    $ qirinName = "Customer"
    $ reaperName = "Customer"

    stop music fadeout 1.0

    call scene01
    call scene02
    call scene03
    call scene04
    call scene05
    call scene06

    return

# game endings here
label end():
    show protag smile
    show li smile
    protag "I guess we can end it here."
    li "Alright, I'll see you later then."

    return
