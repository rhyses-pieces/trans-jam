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
    show protag:
        xzoom 1.0
        move_right
        Pause(0.5)
    show qirin hooded at inL with Pause(1)

    qirin "..." (who_color="#918196")

    show protag at hop
    protag "Oh! That one's got an appointment with me."

    hide qirin with dissolve
    show protag:
        xzoom -1.0
        move_left
        Pause(0.5)
    show li at inR with Pause(1)

    protag "Do you mind manning the register while I take this?"
    li @ smile "Sure thing, boss!"
    protag @ smile "Thanks [li]!"

    show li at outR
    show protag at move_right with Pause(0.5)
    show qirin at inL with Pause(1)

    qirin "H-hi, I'm here for my fortune to be told." (who_color="#918196")
    protag @ happy "Hey! Sorry for the wait. Come on in!"

    show protag at outR
    show qirin at outR

    # footsteps play

    return