label scene04():

    scene bg zodiac_covered with wipeup
    with Pause(0.5)
    
    protag left "The way I do fortune is by reading where the tea leaves lie on this teacup plate."
    protag @ smile "This plate has a list of all the zodiac signs -- may I ask for yours?"
    qirin right "Oh! Um... I was born in the year of the ram."
    protag "I see. I'll open this and..."

    play sound "audio/clink.mp3"

    window hide

    scene bg zodiac_qirin with dissolve
    with Pause(0.5)

    protag think left "Hmmm..."
    protag "(Well, it looks like the tea leaves are covering {b}ram{/b}...)"
    protag @ neutral "(But a lot of them are gathered in the {b}winter{/b} section.)"
    protag @ sad "(That's pretty ominous.)"
    protag ""

    stop music fadeout 1.0

    menu qirin_choice:

        "What kind of interpretation do you want to convey?"
        
        "Tell the truth.":
            jump .truth
        "Lean into what [qirin] wants.":
            jump .desire
        "Just go with whatever.":
            jump .joke

    return

label .truth():

    # qirin truth interpretation

    $ truthEnding += 1
    
    return

label .desire():

    # qirin desire interpretation

    $ desireEnding += 1

    return

label .joke():

    protag stubborn ""

    $ jokeEnding += 1

    return