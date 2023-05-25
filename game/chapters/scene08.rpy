label scene08():
    
    $ play_music(backroom, fadein=1.0, fadeout=2.0, relative_volume=0.5, loop=True)
    scene bg backroom with wipeleft

    $ play_sound(doorclose)

    show protag at left with dissolve:
        xzoom -1.0
    show reaper at right with dissolve

    protag @ smile "What kind of tea do you prefer?"
    reaper @ smile "I like rooibos tea!"
    protag "Alright, coming right up."

    narrator "[protag] and [reaper] had been friends since [protag]'s first accidental stumble into the supernatural world."
    narrator "Though [reaper] had never asked for her fortune to be read, she's known of [protag]'s fortunetelling business for quite some time now."
        
    $ play_sound(teacups, fadein=1.0)

    protag "Here's your tea."
    reaper @ happy "Thanks!"

    $ play_sound(windchimes, fadein=1.0, relative_volume=0.75)

    narrator "There are unseen chimes gently playing soft, high-pitched notes for the invisible breeze to carry away."
    narrator "But there are no windchimes in the room - just two people enjoying their drinks."

    stop sound fadeout 1.0

    scene bg zodiac_covered with wipeup
    with Pause(1)
    $ play_sound(clink)
    scene bg zodiac_reaper with dissolve

    protag think left "Huh..."
    protag "You were born in the year of the {b}rabbit{/b}, right?"
    reaper right "Yep. Why?"
    protag @ smile "It's so I have a better understanding of what this means to you."
    protag "(The way these tea leaves are laid out is weird.)"
    protag neutral "(They're all gathered heavily around the {b}rooster{/b}.)"
    protag @ think "(I wonder if that had anything to do with her work...)"
    protag "(In any case, the way these leaves are clumped in {b}autumn{/b} makes it seem like things might be stale for her.)"
    protag "(But that doesn't mean the end of the world. She's smart and hardworking.)"
    protag @ smile "(The leaves in the {b}spring{/b} section gives me hope.)"
    protag think "(I wonder what I should say to her...)"

    menu reaper_choice:
        "What should you say to her?"
        "Be honest.":
            jump scene08.truth
        "Tell her what she wants to hear.":
            jump scene08.desire
        "\"You should get into pottery.\"":
            jump scene08.joke

    return

label .truth():

    protag closedeyes "I had a hard time parsing your reading, but here's what I can say about it."
    protag neutral "Autumn represents twilight - when harvest takes place and life withers before the winter season."
    protag think "Those born under the sign of the rooster could stand in your way, forcing you to take a direction you may not have taken otherwise."
    protag sad "This might mean that there won't be as many opportunities heading your way as you'd like..."
    protag neutral @ smile "But that doesn't mean it's a bad thing. It's a good time to reflect and discover new things about yourself."
    
    $ truthEnding += 1
    $ reaper_truth = True

    return

label .desire():

    protag "I think... things will be looking up for you."
    protag think "Here, spring represents new beginnings, hope, the thawing of winter."
    protag smile "In addition, you might find help from those born under the signs of the pig and ox."
    protag "This is a chance for you to discover your potential, in a sense!"
    protag neutral "Even though you're going through a setback, success will find its way to you. You just need to work for it."
    
    $ desireEnding += 1
    $ reaper_desire = True

    return

label .joke():

    protag closedeyes "..."
    protag neutral "... Pottery."
    reaper think "... Pardon?"
    protag "The leaves on here are scattered between autumn and spring. The one thing those two seasons have in common..."
    protag stubborn "... is mud."
    protag "So you should go into pottery."
    protag "The fortune said so."
    
    $ jokeEnding += 1
    $ reaper_joke = True

    return