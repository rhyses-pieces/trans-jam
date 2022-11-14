label scene10():
    
    play music cafe_bgm fadein 1.0 fadeout 2.0 loop
    scene bg cafe with Fade(0.5, 1, 0.5)

    show protag smile at right with fade
    show reaper smile at left with fade
    
    with Pause(0.5)

    show reaper at hop
    reaper "Thanks so much for the reading!"
    reaper @ think "I think I'll take a mocha to-go."

    show protag at bow
    protag @ happy "Sure thing!"
    show protag with Dissolve(0.2):
        xzoom -1.0
        pause 0.5

    hide protag with dissolve
    hide reaper with dissolve

    narrator "While [protag] is preparing [reaper]'s drink, the door to the cafe opens."

    play sound dooropen

    show li neutral at center:
        xzoom -1.0
        inL()
        pause 0.5

    li @ think "(Huh? Who's that? We don't open for another five minutes...)"

    show li at outL
    with Pause(0.5)
    hide li

    show reaper neutral at center with dissolve
    reaper "?"
    show reaper:
        xzoom -1.0
        pause 0.5
        hop()
        pause 0.5
    reaper @ surprise "!"
    show reaper:
        xzoom 1.0
        pause 0.5
    reaper "Psst. Hey."
    show reaper at move_left
    with Pause(0.5)
    show reaper at left

    show protag neutral at right:
        xzoom -1.0
        inR()
        pause 0.5
        dissolve(0.5)
        xzoom 1.0
        pause 0.5
    
    protag "Hm? What's up?"
    reaper "I think your employee is here..."
    protag @ think "[li] is here? This early?"
    li "Hey boss."
    
    show protag surprise at hop
    show reaper surprise at hop
    with Pause(0.5)

    show reaper neutral at move_center

    show li neutral at left:
        inL()
    
    with Pause(0.5)

    li "Is she a friend of yours?"
    protag smile "Oh! Yeah. We go way back, actually."
    protag neutral "Let me introduce you guys - [reaper], this is [li]. [li], this is [reaper]."
    reaper @ smile "Hello."
    li @ smile "Nice to meet you."
    protag smile "I just finished up with giving [reaper] a reading, and I'm making her a drink."
    reaper smile @ happy "Yup, and then I'll be on my way!"
    protag @ sad "Aw, you're not staying around?"
    reaper "Nah, I've got things to do later."
    protag "Okay. Here's your drink, by the way. Gimme a call later, alright?"
    reaper @ happy "Alright. It was nice seeing you, [protag]!"
    protag @ happy "Yeah, same!"

    show reaper at outL
    with Pause(0.5)
    hide reaper

    play sound dooropen

    narrator "[reaper] takes her drink and makes a beeline for the exit. [protag] is left feeling confused, wondering about the strange change in her attitude."
    narrator "Meanwhile..."

    li "So uh... you guys seem close."
    protag "Yeah, we've been friends for a while."
    protag @ think "Um, everything okay?"
    li @ think "Yeah. Why do you ask?"
    protag "Oh, I was just checking. I wasn't expecting you to come in so early!"
    protag @ smile "Is there anything you want to talk about?"
    li @ blush "O-oh. Ha ha..."
    li "Actually, I was wondering if... you know... you could do a reading on me too."
    protag @ surprise "Huh?"
    li @ blush "Yeah! Um. I have a friend of mine who's going through some stuff..."
    li "And I was wondering if, um, you could do a reading on that?"
    protag @ think "I mean, sure! If you want."
    protag smile "We can hold off on opening the cafe so we can get your reading done."
    protag "How's that sound?"
    li @ blush "T-that sounds good to me..."
    protag @ happy "Alright!"

    return