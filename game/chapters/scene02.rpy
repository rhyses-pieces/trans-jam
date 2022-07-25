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
        pause 0.5
        move_right
    show protag with Pause(1.25)
    show qirin hooded at inL with Pause(0.75)

    qirin "..." (who_color="#918196")

    show protag at hop
    protag "Oh! That one's got an appointment with me."

    hide qirin with dissolve
    show protag:
        xzoom -1.0
    show protag at move_left with Pause(0.75)
    show li default at right:
        inR()
    show li with Pause(0.5)

    protag "Do you mind manning the register while I take this?"
    li @ smile "Sure thing, boss!"
    protag @ smile "Thanks [li]!"

    show li at outR with Pause(0.5)
    hide li
    show protag:
        move_right
        pause 0.5
        xzoom 1.0
    show protag with Pause(0.75)
    show qirin hooded at inL with Pause(0.5)

    qirin "H-hi, I'm here for my fortune to be told." (who_color="#918196")
    protag @ happy "Hey! Sorry for the wait. Come on in!"

    show protag at outR
    show qirin at outR

    # footsteps play

    return