label scene08():
    
    scene bg backroom with wipeleft

    protag "have a seat!"
    reaper "thanks"

    menu reaper_choice:
        "Say Statement"
        "Choice 1":
            jump .truth
        "Choice 2":
            jump .desire
        "\"You should get into pottery.\"":
            jump .joke

    return

label .truth():
    
    $ truthEnding += 1

    return

label .desire():
    
    $ desireEnding += 1

    return

label .joke():
    
    $ jokeEnding += 1

    return