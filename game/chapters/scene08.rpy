label scene08():
    
    play music backroom fadein 1.0 fadeout 2.0 volume 0.5 loop
    scene bg backroom with wipeleft

    play sound doorclose

    show protag at left with dissolve:
        xzoom -1.0
    show reaper at right with dissolve

    protag @ smile "What kind of tea do you prefer?"
    reaper @ smile "I like rooibos tea!"
    protag "Alright, coming right up."
    narrator "[protag] and [reaper] had been friends since [protag]'s first accidental stumble into the supernatural world."
    narrator "Though [reaper] had never asked for her fortune to be read, she's known of [protag]'s fortunetelling business for quite some time now."
    
    play sound teacups fadein 1.0

    protag "Here's your tea."
    reaper @ happy "Thanks!"

    play sound windchimes fadein 1.0 fadeout 1.0 volume 0.75

    narrator "There are unseen chimes gently playing soft, high-pitched notes for the invisible breeze to carry away."
    narrator "But there are no windchimes in the room - just two people enjoying their drinks."

    stop sound fadeout 1.0

    scene bg zodiac_covered with wipeup
    with Pause(1)
    play sound "audio/clink.mp3"
    scene bg zodiac_reaper with dissolve

    protag think left "Huh..."
    protag "You were born in the year of the {b}tiger{/b}, right?"
    reaper right "Yep. Why?"
    protag @ smile "It's so I have a better understanding of what this means to you."
    protag "(That's weird.)"
    protag "(I can't seem to make sense of this...)"

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