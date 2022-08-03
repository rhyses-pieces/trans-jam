label scene03():
    
    play music backroom fadein 1.0 volume 0.5 loop
    stop audio fadeout 1.0
    scene bg backroom with wipeleft

    with Pause(0.75)

    play sound dooropen

    show qirin hooded at right:
        xzoom -1.0
        inR()

    with Pause(1.0)

    protag neutral left "Don't worry, you're safe here! Please, take a seat."
    qirin "Okay..." (who_color="#918196")

    play sound doorclose

    show qirin neutral with dissolve
    with Pause(0.5)
    $ qirinName = "Riley"

    narrator "The customer takes off their hood, revealing a small horn jutting out from their forehead."
    narrator "Their name is [qirin], and they come from a family of qirin."
    narrator "Since their kind are known to be creatures of good luck, they usually disguise themself to avoid notice from unsavory characters."

    show qirin at bow with Pause(0.5)
    show protag neutral at left:
        xzoom -1.0
        inL()
        pause 0.5
        bow()
    with Pause(1.5)
    
    protag @ smile "Nice to meet you, [qirin]! So, what brings you here?"
    qirin "Well, you see, I just recently moved out of my parents' house..."
    qirin @ sad "And I thought things would get better, but they've been bombarding me with calls and texts."
    qirin "It's gotten to the point that I can't do anything without them asking me where I am every five minutes."
    qirin sad "I even got into an argument with them recently about it."
    qirin "It's driving me insane. I love them and all, but this is too much..."
    protag @ sad "I'm sorry to hear about that."
    protag "So what kind of fortune are you looking for in this situation?"
    qirin neutral @ think "I guess... I'm wondering if there's a chance if I can work things out with my family."
    protag "Of course. The way I tell fortunes is a little different than most."
    protag @ smile "First, we start with enjoying a cup of tea."
    protag "What's your favorite kind?"
    qirin  @ think "Oh! Um... I like matcha tea."
    protag @ smile "You got it!"
    protag @ blush "Sorry it won't be the powder kind, but I need tea leaves for this to work."
    qirin @ smile "No worries."

    play audio windchimes fadein 1.0 volume 0.75

    narrator "As [protag] prepares a cup of tea for [qirin], there's a faint sound of windchimes jingling lightly in the breeze even though they're indoors."
    
    play sound teacups
    stop audio fadeout 1.0
    
    narrator "They sit and chat for a bit while [qirin] sips at their drink."
    qirin smile "(I don't know what I expected, but this is really nice.)"

    narrator "They finish their drink not long after, and [protag] motions for their cup. [qirin] hands it over, curious about what's next."
    narrator "[protag] suddenly flips the cup upside down on a strange looking teacup tray."
    qirin think "Huh...?"

    play sound clink

    return