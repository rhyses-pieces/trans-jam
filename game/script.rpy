# Declare characters used by this game. The color argument colorizes the
# name of the character.

define protag = Character('Jonghyun', color="#afcfb3")
define li = Character('Noel', color="#f171af")

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
