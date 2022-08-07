label scene08():
    
    play music backroom fadein 1.0 fadeout 2.0 volume 0.5 loop
    scene bg backroom with wipeleft

    show protag at left:
        dissolve(0.5)
        xzoom -1.0
    show reaper at right with dissolve(0.5)

    protag "have a seat!"
    reaper "thanks"

    menu reaper_choice:
        "Say Statement"
        "Choice 1":
            jump scene08.truth
        "Choice 2":
            jump scene08.desire
        "\"You should get into pottery.\"":
            jump scene08.joke

    return

label .truth():
    
    $ truthEnding += 1
    $ reaper_truth = True

    return

label .desire():
    
    $ desireEnding += 1
    $ reaper_desire = True

    return

label .joke():
    
    $ jokeEnding += 1
    $ reaper_joke = True

    return