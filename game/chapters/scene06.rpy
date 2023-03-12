label scene06():

    play_music(cafe, fadein=1.0, fadeout=2.0, loop=True)

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
    li "All I know is that you usually have tea with certain customers in the back..."
    protag "Eheh, I read their fortunes through tea leaves! They just go to the back for privacy."
    li @ surprise "Oh! That makes sense. {nw}"
    show li think
    extend "I think I remember seeing one of them with rabbit ears...?"
    protag "That's right. They're part of the mythological population in the city -- like you and me!"
    protag "Back when I was younger, one of my family friends was a shaman."
    protag smile "I thought she was super cool, even though she got a lot of flack for it."
    protag "She actually taught me a few things about fortune-telling!"
    li smile @ happy "Oh! That's so cool!"
    li "Did she also teach you how to do it through reading tea leaves?"
    protag happy "Naw. I learned that on my own for funsies."
    li neutral @ fear "...???"
    protag neutral "Anyways, it seems like things are winding down in the cafe. Let's start closing up shop."
    li "Alright."
    li @ think "(I don't know if I've understood [protag] better...)"
    li @ smile "(Eh, whatever. He's still pretty fun to hang around.)"

    narrator "The day draws to a close, with another surprise waiting tomorrow..."

    stop music fadeout 1.0
    
    return