label scene09():
    
    if renpy.seen_label(scene08.truth):
        jump .truth
    elif renpy.seen_label(scene08.desire):
        jump .desire
    else:
        jump .joke

    return

label .truth():

    return

label .desire():
    
    return

label .joke():

    return