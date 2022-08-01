label scene05():

    scene bg backroom with wipedown
    with Pause(0.5)

    show protag neutral at left with dissolve
    show qirin neutral at right with dissolve

    protag "Was this helpful for you?"
    
    if truthEnding > 0:
    
        qirin sad "It... it made me think, that's for sure."

        jump .truth
    
    elif desireEnding > 0:
    
        qirin smile @ happy "It was! Thank you so much."

        jump .desire
    
    else:
    
        qirin think "... the Bahamas?"

        jump .joke
    
    protag @ smile "It was a pleasure doing business with you."

    return

label .truth():

    protag sad "I'm sorry. I know it's painful to hear the truth."
    protag "Family can get... complicated."
    protag neutral @ smile "But at the end of the day, family doesn't have to {i}only{/i} be blood-related."
    protag "However things turn out, I think you'll be fine."
    qirin "..."
    qirin smile "Thank you for your honesty. I really appreciate it."

    return

label .desire():
    
    protag sad "(I don't know if I'm making the right decision or not.)"
    protag "(Lying to their face feels bad, but it's not like I can tell them that things will go south no matter what...)"
    protag neutral "(Maybe this is for the best.)"

    return

label .joke():

    protag @ stubborn "Yes. The Bahamas."
    protag "I think you'll be able to find "
    
    return