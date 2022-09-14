label scene05():

    scene bg backroom with wipedown
    with Pause(0.5)

    show protag neutral at left with dissolve:
        xzoom -1.0
    show qirin neutral at right with dissolve:
        xzoom -1.0

    protag "Was this helpful for you?"
    
    if qirin_truth:
        qirin sad "It... it made me think, that's for sure."
        jump .truth
    elif qirin_desire:
        qirin smile @ happy "It was! Thank you so much."
        jump .desire
    else:
        qirin think "... the Bahamas?"
        jump .joke
    
    protag @ smile "It was a pleasure doing business with you."
    qirin neutral "Likewise. Thanks again for the reading."

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
    
    protag neutral @ happy "I'm glad."
    protag "..."
    protag sad "(I don't know if I'm making the right decision or not.)"
    protag "(I may have skewed the interpretation a little to make them feel better, but...)"
    protag neutral "(I don't know. Maybe this is for the best.)"

    return

label .joke():

    protag @ stubborn "Yes. The Bahamas."
    protag "The southernly direction leans towards positivity for you."
    qirin "...Okay? If you say so, I guess..."
    qirin "Actually, wait. Now that you mention it.."
    qirin neutral @ happy "My partner mentioned wanting to go somewhere tropical!"
    protag @ happy "It all works out!"
    
    return