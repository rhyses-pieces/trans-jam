label scene06():

    play music cafe_bgm fadein 1.0 fadeout 2.0 loop

    scene bg cafe with Fade(0.5, 1, 0.5)

    narrator "After [qirin] left through the backdoor, [protag] walks out of the backroom."

    show protag smile at right:
        inR()
    with Pause(0.5)
    
    protag neutral @ closedeyes "All in a day's work..."

    show li neutral:
        xzoom -1.0
        inL()
    with Pause(0.5)
    
    li @ think "What was that about?"
    protag "Oh! Hey [li]."
    protag @ blush "I forgot I never told you much about what I do back there."
    protag "You remember the one lady who kinda looked like a lion?"
    li fear "Jeez, why bring her up? I was so scared when I first saw the lady!"
    protag "Aw, hey, Mrs. Lee is nice! She wouldn't hurt a fly."
    protag @ think "... I mean, well, unless you lied in front of her. Then she'd get {i}real{/i} mad."
    li neutral @ think "You're not doing a good job of making her seem less scary."
    protag @ happy "Anyways!"
    protag "She's a haechi. You know, the scaly lion-dogs who stab liars with their horns?"
    li fear "..."
    li "Oh my god. This explains so much. That's why she seems so intense."
    protag "That's 'cause she cares a lot! She was the first person who asked me read their fortune."
    protag @ smile "She wanted to know if her daughter would do alright in school."
    protag @ happy "After that, she really helped getting my fortunetelling gig off the ground!"
    protag @ smile "That's why most of our customers are kinda supernatural. The cafe's for normal humans like me."
    li closedeyes "... This explains so much."
    protag @ happy "You said that already, haha."
    li think "Why do you do it though?"
    li neutral @ sad "I'm sure some of us have already caused some problems for you humans..."
    protag smile "Nah, I've never had a problem."
    protag "I mean, you never had a problem with me being trans, right?"
    li @ think "Why should I? You're just you. Being trans isn't a bad thing at all. Not sure why people assume it is."
    protag "Exactly. Just 'cause you're supernatural doesn't automatically mean you're bad."
    
    return