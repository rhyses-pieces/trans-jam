label scene01():

    $ play_music(cafe, fadein=1.0, loop=True)

    scene bg cafe with fade
    
    narrator "It's a busy time at Zodiac Cafe."
    narrator "Coffee cups clink against ceramic trays, patrons chatter over tea, and the owner rings up orders at the register."

    show protag neutral with dissolve

    protag smile "Here's your usual."
    
    $ genericName = "Patron"
    generic "Thank you!"

    narrator "The regular at the counter takes their drink and slips in a dollar in the tip jar before returning to their seat."

    protag "(I'm glad business is doing well today.)"
    protag neutral @ think "(Now if {i}that guy{/i} could stop being late for once...)"

    show protag at move_right with Pause(0.5)
    show li neutral at inL with Pause(0.3)

    li "Hey boss!"

    show protag stubborn at hop
    protag "Dude, you're late!"

    li blush "Heh, sorry."
    protag @ stubborn "This is the last time I'm letting you slide."
    li @ stubborn "Yes sir! I'll be the most punctual employee you'll ever see!"
    protag @ think "... That's what you said last time."
    li "Did I? I don't remember... haha..."
    protag @ closedeyes "*Sigh*"
    protag "Alright. Just get prepped and start working."
    li smile "Okay!"

    return