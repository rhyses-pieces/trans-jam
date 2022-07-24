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

    def genericBleep(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/generic.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound", fadeout=1)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character('Jonghyun', image="protag", color="#79be9e", callback=[protagBleep,name_callback], cb_name="protag")
define li = Character('Noel', image="li", color="#f171af", callback=[liBleep, name_callback], cb_name="li")
define narrator = Character(callback=name_callback, cb_name=None)
define generic = Character('[genericName]', color="#575c69", callback=[genericBleep,name_callback], cb_name=None)

image black = Solid("#000")

# define sprites for auto highlights
image li angry = At('li angry.png', sprite_highlight('li'))
image li blush = At('li blush.png', sprite_highlight('li'))
image li closedeyes = At('li closedeyes.png', sprite_highlight('li'))
image li default = At('li default.png', sprite_highlight('li'))
image li happy = At('li happy.png', sprite_highlight('li'))
image li sad = At('li sad.png', sprite_highlight('li'))
image li smile = At('li smile.png', sprite_highlight('li'))
image li surprise = At('li surprise.png', sprite_highlight('li'))
image li think = At('li think.png', sprite_highlight('li'))

image protag angry = At('protag angry.png', sprite_highlight('protag'))
image protag blush = At('protag blush.png', sprite_highlight('protag'))
image protag closedeyes = At('protag closedeyes.png', sprite_highlight('protag'))
image protag default = At('protag default.png', sprite_highlight('protag'))
image protag happy = At('protag happy.png', sprite_highlight('protag'))
image protag sad = At('protag sad.png', sprite_highlight('protag'))
image protag smile = At('protag smile.png', sprite_highlight('protag'))
image protag surprise = At('protag surprise.png', sprite_highlight('protag'))
image protag think = At('protag think.png', sprite_highlight('protag'))

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
