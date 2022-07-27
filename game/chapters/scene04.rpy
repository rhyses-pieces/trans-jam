label scene04():

    scene bg zodiac_covered with wipeup

    menu qirin_choice:

        "Say Statement"
        
        "Choice 1":
            jump .truth
        "Choice 2":
            jump .desire
        "":
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