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
            renpy.music.play("audio/li.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def reapBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/li.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

    def genericBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/generic.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character('Jonghyun', image="protag", color="#79be9e", callback=[protagBleep,name_callback], cb_name="protag")
define li = Character('Noel', image="li", color="#b22673", callback=[liBleep, name_callback], cb_name="li")
define qirin = Character('hello', image="qirin", color="#4e6e8f", callback=[qirinBleep,name_callback], cb_name="qirin")
define reaper = Character('hi', image="reaper", color="#b85b6b", callback=[reapBleep,name_callback], cb_name="reaper")
define narrator = Character(callback=name_callback, cb_name=None)
define generic = Character('[genericName]', color="#918196", callback=[genericBleep,name_callback], cb_name=None)

image black = Solid("#000")

# define sprites for auto highlights
image li angry = At('li angry.png', sprite_highlight('li'))
image li blush = At('li blush.png', sprite_highlight('li'))
image li closedeyes = At('li closedeyes.png', sprite_highlight('li'))
image li default = At('li default.png', sprite_highlight('li'))
image li fear = At('li fear.png', sprite_highlight('li'))
image li happy = At('li happy.png', sprite_highlight('li'))
image li sad = At('li sad.png', sprite_highlight('li'))
image li smile = At('li smile.png', sprite_highlight('li'))
image li stubborn = At('li stubborn.png', sprite_highlight('li'))
image li surprise = At('li surprise.png', sprite_highlight('li'))
image li think = At('li think.png', sprite_highlight('li'))

image protag angry = At('protag angry.png', sprite_highlight('protag'))
image protag blush = At('protag blush.png', sprite_highlight('protag'))
image protag closedeyes = At('protag closedeyes.png', sprite_highlight('protag'))
image protag default = At('protag default.png', sprite_highlight('protag'))
image protag fear = At('protag fear.png', sprite_highlight('protag'))
image protag happy = At('protag happy.png', sprite_highlight('protag'))
image protag sad = At('protag sad.png', sprite_highlight('protag'))
image protag smile = At('protag smile.png', sprite_highlight('protag'))
image protag stubborn = At('protag stubborn.png', sprite_highlight('protag'))
image protag surprise = At('protag surprise.png', sprite_highlight('protag'))
image protag think = At('protag think.png', sprite_highlight('protag'))

image qirin default = At('qirin default.png', sprite_highlight('qirin'))
image qirin happy = At('qirin happy.png', sprite_highlight('qirin'))
image qirin hooded = At('qirin hooded.png', sprite_highlight('qirin'))
image qirin sad = At('qirin sad.png', sprite_highlight('qirin'))
image qirin think = At('qirin think.png', sprite_highlight('qirin'))

image reaper default = At('reaper default.png', sprite_highlight('reaper'))
image reaper happy = At('reaper happy.png', sprite_highlight('reaper'))
image reaper sad = At('reaper sad.png', sprite_highlight('reaper'))
image reaper think = At('reaper think.png', sprite_highlight('reaper'))

# The game starts here.

label start():
    $ genericName = ""

    stop music fadeout 1.0

    call scene01

    call scene02

    return

label end():
    show protag smile
    show li smile
    protag "I guess we can end it here."
    li "Alright, I'll see you later then."

    return
