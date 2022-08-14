label scene09():

    scene bg backroom with wipedown
    with Pause(0.5)

    show protag neutral at left with dissolve:
        xzoom -1.0
    show reaper neutral at right with dissolve

    protag "So... how are you feeling right now?"
    reaper think "Well..."
    
    if reaper_truth:
        jump .truth
    elif reaper_desire:
        jump .desire
    else:
        jump .joke

    return

label .truth():

    reaper "Hmm... I feel somewhat mixed?"
    reaper neutral @ sad "It's weird, but I'm both sad and a little hopeful."
    reaper "Like yeah, this whole situation sucks, "

    return

label .desire():
    
    return

label .joke():

    return