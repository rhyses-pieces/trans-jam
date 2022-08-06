label scene07():

    play music "audio/day2.ogg" fadein 1.0 loop
    scene bg bedroom with fade

    show protag closedeyes at center with dissolve

    play sound "audio/phone_ring.ogg"
    with Pause(0.25)

    show protag at wag
    play sound "audio/phone_pickup.ogg"

    protag "Mmm... hello?"

    $ reaperName = "Unknown Caller"
    reaper smile right "[protag]?" (who_color="#918196")
    protag "Huh? Who is this?"
    reaper happy "[protag], it's me! {color="#b85b6b"}Minhee{/color}!"
    
    $ reaperName = "Minhee"
    protag neutral @ surprise "Oh my god, [reaper]?! It's been forever since I last heard from you!"
    reaper "I know, right?!"
    reaper neutral @ sad "I'm sorry I wasn't able to keep in contact with you more."
    reaper ""

    return