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

define protag = Character('Jonghyun', color="#afcfb3", callback=[protagBleep,name_callback], cb_name="protag")
define li = Character('Noel', color="#f171af", callback=[liBleep, name_callback], cb_name="li")
define narrator = Character(callback=name_callback, cb_name=None)

# define sprites for subtle highlights
image li angry = At('li angry.png', sprite_highlight('li'))
image li blush = At('li blush.png', sprite_highlight('li'))
image li default = At('li default.png', sprite_highlight('li'))
image li happy = At('li happy.png', sprite_highlight('li'))
image li sad = At('li sad.png', sprite_highlight('li'))
image li smile = At('li smile.png', sprite_highlight('li'))
image li think = At('li think.png', sprite_highlight('li'))

image protag angry = At('protag angry.png', sprite_highlight('protag'))
image protag blush = At('protag blush.png', sprite_highlight('protag'))
image protag default = At('protag default.png', sprite_highlight('protag'))
image protag happy = At('protag happy.png', sprite_highlight('protag'))
image protag sad = At('protag sad.png', sprite_highlight('protag'))
image protag smile = At('protag smile.png', sprite_highlight('protag'))
image protag think = At('protag think.png', sprite_highlight('protag'))

# The game starts here.

label start:

    scene bg bedroom
    show protag smile

    protag "You've created a new Ren'Py game."

    show protag:
        xzoom -1.0

    protag "Once you add a story, pictures, and music, you can release it to the world!"

    show protag default at left
    show li default at right
    
    li "Oh hey, what's up?"
    
    menu:
        "I've been..."
        "... alright.":
            jump neutral
        "... great!":
            jump happy

label happy:
    show protag happy
    protag "Feeling great!"

    show li happy
    li "That's awesome!"
    
    jump end

label neutral:
    show protag smile
    protag "Nothing much. You?"
    
    show li smile
    li "Doing good, thanks!"

    jump end

label end:
    show protag smile
    show li smile
    protag "I guess we can end it here."
    li "Alright, I'll see you later then."

    return
