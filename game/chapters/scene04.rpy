label scene04():

    scene bg zodiac_covered with wipeup
    with Pause(0.5)
    
    protag left "The way I do fortune is by reading where the tea leaves lie on this teacup plate."
    protag @ smile "This plate has a list of all the zodiac signs -- may I ask for yours?"
    qirin right "Oh! Um... I was born in the year of the ram."
    protag "I see. I'll open this and..."

    window hide

    scene bg zodiac_qirin with dissolve
    with Pause(0.5)

    protag think left "Hmmm..."
    protag "(Well, it looks like the tea leaves are covering ram...)"

    menu qirin_choice:

        "This fortune says..."
        
        "Choice 1":
            jump .truth
        "Choice 2":
            jump .desire
        "\"... you should go to the Bahamas.\"":
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

    # qirin joke interpretation

    $ jokeEnding += 1

    return