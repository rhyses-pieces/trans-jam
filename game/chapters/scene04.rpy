label scene04():

    scene bg zodiac_covered with wipeup
    with Pause(0.5)
    
    protag left "The way I do fortune is by reading where the tea leaves lie on this teacup plate."
    protag @ smile "This plate has a list of all the zodiac signs - may I ask for yours?"
    qirin right "Oh! Um... I was born in the year of the {b}ram{/b}."
    protag "I see. I'll open this and..."

    window hide
    with Pause(1.5)
    $ play_sound(clink)

    scene bg zodiac_qirin with dissolve
    with Pause(1)

    protag think left "Hmmm..."
    protag "(Well, it looks like {i}some{/i} of the tea leaves are covering the {b}ram{/b} sign...)"
    protag neutral "(But a lot of them are gathered in the {b}winter{/b} section.)"
    protag surprise "(There's even some on the {b}ox{/b} sign.)"
    protag sad @ think "(That's pretty ominous.)"
    protag "(It probably means that things with their family won't work out...)"
    protag "(I don't think it's entirely bad though.)"
    protag @ think "(There's also some leaves on {b}summer{/b}, so they might have strength to rise above their circumstances.)"
    protag "(What should I tell them?)"

    stop music fadeout 1.0

    menu qirin_choice:

        "What kind of interpretation do you want to convey?"
        
        "Talk about the potential fallout.":
            jump scene04.truth
        "Lean into what [qirin] wants.":
            jump scene04.desire
        "Just go with whatever.":
            jump scene04.joke

    return

label .truth():

    $ play_music(backroom, fadein=1.0, relative_volume=0.5, loop=True)

    protag sad @ closedeyes "I'll be honest - things don't look great."
    protag "Winter is always a difficult time because of the cold, food shortages, and long nights."
    protag neutral "Similarly, you will experience hardships in the future -{p} Particularly from those born in the year of the ox."
    protag @ stubborn "Their stubborn and unyielding nature will oppose you."
    protag @ closedeyes "But winter does not last forever."
    protag "Whether or not you overcome these challenges, spring will be waiting around the corner."

    $ truthEnding += 1
    $ qirin_truth = True
    
    return

label .desire():

    $ play_music(backroom, fadein=1.0, relative_volume=0.5, loop=True)

    protag neutral "Things may be looking in your favor."
    protag @ smile "Winter represents hardships, but you may find support from people around you."
    protag "Those born in the years of the horse and pig might help you."
    protag "As the seasons change from winter, to spring, and then to summer, your vitality will increase."
    protag @ smile "That is to say, even though things will be tough for a bit, you may be able to forge positive relationships."

    $ desireEnding += 1
    $ qirin_desire = True

    return

label .joke():

    $ play_music(backroom, fadein=1.0, relative_volume=0.5, loop=True)
    
    protag stubborn "Go to the Bahamas."
    protag "Winter implies that the people around you will work hard to prepare for the worst."
    protag neutral "If you interfere with their work, misfortune will befall you."
    protag @ think "So it's better to go on a vacation, specifically to the Bahamas."
    protag "Your energies will be cleansed, refreshed, and revitalized in time for summer."

    $ jokeEnding += 1
    $ qirin_joke = True

    return