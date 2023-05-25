label scene02():
    
    scene bg cafe with Fade(0.5, 1, 0.5)

    narrator "Later in the day..."

    show protag neutral at left with dissolve
    show li neutral at right with dissolve

    li "..."
    li "Hey [protag]?"
    
    show protag with dissolve:
        xzoom -1.0
    
    protag "Yeah?"
    li "I think there's someone waiting for you."

    window hide

    hide li with dissolve
    show protag with Dissolve(0.2):
        xzoom 1.0
        pause 0.5
        move_right
    with Pause(0.75)
    show protag at right
    show qirin hooded at inL with Pause(0.5)

    qirin "..." (who_color="#918196")

    show protag at hop
    protag "Oh! That one's got an appointment with me."

    window hide

    hide qirin with dissolve
    show protag with Dissolve(0.2):
        xzoom -1.0
        pause 0.5
        move_left
    with Pause(0.75)
    show protag at left
    show li neutral at right:
        inR()
    with Pause(0.5)

    protag "Do you mind manning the register while I take this?"
    li @ smile "Sure thing, boss!"
    protag @ smile "Thanks [li]!"

    window hide

    show li at outR with Pause(0.5)
    hide li
    show protag with Dissolve(0.2):
        xzoom 1.0
        pause 0.5
        move_right
    with Pause(0.75)
    show protag at right
    show qirin hooded at inL with Pause(0.5)

    qirin "H-hi, I'm here for my fortune to be told." (who_color="#918196")
    protag @ happy "Hey! Sorry for the wait. Come on in!"

    window hide

    with Pause(0.25)
    $ play_sound(dooropen)

    show protag with Dissolve(0.2):
        xzoom -1.0
        pause 0.5
        outR()
    show qirin:
        pause 0.75
        outR()

    with Pause(1.25)

    # footsteps play

    return