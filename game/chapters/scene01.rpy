label scene01():

    play music "audio/cafe_bgm.mp3" fadein 1.0 loop
    play sound "audio/cafe_ambience.mp3" fadein 1.0 volume 0.5 loop

    scene bg cafe with fade

    narrator "It's a busy time at CAFE."
    narrator "Coffee cups clink against ceramic trays, patrons chatter over tea, and the owner rings up orders at the register."

    show protag default with dissolve

    protag @ smile "Here's your usual."
    
    $ genericName = "Patron"
    generic "Thank you!"

    narrator "The regular at the counter takes their drink and slips in a dollar in the tip jar before returning to their seat."


    return