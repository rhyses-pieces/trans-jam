label scene11():

    play music backroom fadein 1.0 fadeout 2.0 volume 0.5 loop
    scene bg backroom with wipeleft

    show protag at left with dissolve:
        xzoom -1.0
    show li at right with dissolve:
        xzoom -1.0

    narrator "After the two enter the backroom, {nw}"
    show protag happy at doublehop
    with Pause(0.5)
    extend "[protag] begins explaining his tea leaf reading process."
    show protag neutral
    with Pause(0.25)
    show li think at wag
    with Pause(0.25)
    show li smile at hop
    with Pause(0.5)

    li neutral "I think I understand."
    protag @ happy "Awesome! {nw}"
    show protag smile
    extend "Let's get into it. What are you looking for in this reading?"
    li blush "Haha... That's a little embarrassing, but my friend was looking for um..."
    li "Love advice? I guess? It was weird..."
    with Pause(0.25)
    show protag with bow
    protag @ smile "It's not weird at all. I think that's very sweet that you're looking out for your friend."
    protag @ think "What's your favorite tea?"
    li @ smile "I like chai with some milk and sugar."
    with Pause(0.25)
    show protag with bow
    protag neutral @ happy "You got it."

    play sound teacups fadein 1.0

    narrator "While [protag] begins making [li]'s tea, [li] begins to hear something faint."

    play sound windchimes fadein 1.0 fadeout 1.0 volume 0.75

    narrator "Light, chime tones that are almost imperceptible intimately wrap around the two of them."

    li @ blush "(This almost feels like a date...)"

    show li surprise at hop
    play sound teacups fadein 1.0 volume 0.75

    protag @ happy "Here you are!"
    show li blush
    protag @ think "Um. Sorry, are you okay?"
    li @ happy "Haha, yeah, no worries. {nw}"
    show li smile
    extend "I'm fine."

    protag @ think "Hmmm..."
    protag smile @ happy "Well, if you say so!"

    narrator "The two of them enjoy their aromantic, subtly spiced drinks. When they're finished, [li] hands his empty cup to [protag]."
    show protag blush
    show li blush
    extend "Their fingers slightly touch."
    show protag neutral
    narrator "[protag] clears his throat before flipping [li]'s cup over."

    play sound "audio/clink.mp3" volume 0.75

    return