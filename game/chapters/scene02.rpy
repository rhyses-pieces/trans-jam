label scene02():
    
    scene bg cafe with Fade(0.5, 1, 0.5)

    narrator "Later in the day..."

    show protag default at left with dissolve
    show li default at right with dissolve

    li "..."
    li "Hey [protag]?"
    
    show protag:
        xzoom -1.0
    
    protag "Yeah?"
    li "I think there's a \"customer\" waiting for you."

    hide li with dissolve
    show protag at move_right with Pause(0.5)
    show qirin hooded at inL with Pause(1)

    

    return