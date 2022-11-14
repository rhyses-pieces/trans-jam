label scene07():

    play music "audio/day2.ogg" fadein 1.0 loop
    scene bg bedroom with fade

    show protag closedeyes at center with dissolve

    play sound "audio/phone_ring.ogg"
    with Pause(0.25)

    show protag at wag
    play sound "audio/phone_pickup.ogg"

    protag "Mmm... hello?"

    reaper smile "[protag]?" (who_color="#918196")
    protag "Huh? Who is this?"

    $ reaperName = "Minhee"
    reaper happy "[protag], it's me, [reaper]!"
        
    protag neutral "Oh! [reaper], what's up?"
    protag @ think "It's not like you to call me this early..."
    reaper neutral "Sorry for waking you up."
    reaper @ sad "I wondering if we could meet up or something."
    reaper "Are you free later today?"
    protag @ smile "Of course!"
    protag "Do you want to meet at the cafe?"
    reaper @ smile "Yeah! That sounds great. I'll come drop by."
    protag @ happy "Sounds great! See you then."

    scene bg cafe with Fade(0.5, 1, 0.5)
    play music cafe_bgm fadein 1.0 fadeout 2.0 loop

    show protag at right with dissolve
    with Pause(0.5)
    
    show reaper smile at left:
        inL()
    with Pause(0.5)

    show protag at hop
    protag smile "Hey [reaper]! You made it!"
    reaper happy "[protag]! It's so good to see you."
    protag "Same to you! How've you been?"
    protag neutral @ think "You sounded kinda off on the phone."
    reaper "..."
    reaper sad "Haha. Never been better."
    protag @ fear "Oh jeez. Do you wanna talk about it?"
    reaper "Ha... Well, I lost my job..."
    protag @ surprise "What?! How?!"
    reaper "They said it was something about workforce reduction..."
    protag stubborn "That literally makes no sense!"
    protag @ mad "How do you justify reducing the workforce for the literal {i}afterlife{/i}?"
    narrator "[reaper] works as a grim reaper - the kind thaqt ferries the recently deeased to Heaven or Hell."
    narrator "Or, well. She {i}used{/i} to work as a grim reaper."
    reaper "I dunno... but right now, I'm out of a job."
    protag sad "..."
    protag closedeyes "Hmm..."
    protag neutral "What if I read your fortune?"
    reaper neutral "Huh?"
    protag @ smile "Yeah! Do you wanna try it?"
    reaper @ think "Hmm..."
    reaper smile "Yeah, I'd like that!"
    protag smile @ happy "Awesome!"
    protag "Come on back!"

    with Pause(0.25)
    play sound dooropen

    show protag with Dissolve(0.2):
        xzoom -1.0
        pause 0.5
        outR()
    show reaper:
        pause 0.75
        outR()

    return