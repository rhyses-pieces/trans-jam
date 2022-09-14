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

    reaper "Hmm... I feel kinda sad."
    reaper sad "Losing my job felt like I lost my purpose..."
    reaper @ closedeyes "It feels doubly awful since it was out of my control."
    reaper neutral "And you're telling me I still have hope?"
    reaper sad "I don't know..."
    protag stubborn "You do. You absolutely do have hope."
    protag "You've proven to the heavens and hells - literally! - that you're exceptionally talented."
    protag @ angry "It's their loss. Fuck them."

    show reaper surpise at hop
    reaper "!"
    
    protag neutral "I know that whatever {i}you{/i} decide to do next, you'll be okay."
    protag @ smile "Have more faith in yourself, alright?"
    reaper teary "*sniffle*"
    reaper "You suck. Thank you."
    protag @ happy "Hee hee. Anything for a friend!"

    return

label .desire():

    reaper neutral @ smile "I definitely feel a little better."
    reaper "I've been having a hard time lately, I feel like... things are going to be okay now."
    reaper smile @ happy "Yeah... yeah, maybe I {i}can{/i} do it!"
    reaper "Actually, you know what? I was kinda thinking about starting my own business."
    reaper @ happy "I think this is a good sign as any to start it!"
    protag @ happy "That's awesome!"
    protag smile "I hope I get to be your first customer!"
    reaper smile "Of course!"
    
    return

label .joke():

    reaper "I mean... pottery? Really?"
    protag @ stubborn "Yes. Pottery."
    protag "It's a great way of putting out your creative {i}and{/i} negative energy, you know?"
    protag @ closedeyes "Punching and smashing clay is great stress reliever."
    reaper @ closedeyes "Hmm... I've always wanted to try ceramics."
    protag smile @ happy "See? It can't hurt to try!"
    protag "I have a friend who runs a studio, I'm sure they'll let you get lessons for free."
    reaper neutral @ think "Really? I don't know, that seems kinda -"
    protag "Nah. They wouldn't mind, I promise."
    reaper "Well... if you say so."

    return