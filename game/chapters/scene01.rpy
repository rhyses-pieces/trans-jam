label scene01():

    scene bg bedroom
    show protag closedeyes

    narrator "It's about five in the morning when there's a loud knock on the door."

    protag think "Seriously? The sun's not even up yet. Who on earth could that be?"

    show protag:
        xzoom -1.0

    narrator """
    [protag] cautiously makes his way towards the front door to his house, armed with a phone and a healthy set of lungs. He sneaks a glance through the peekhole, only to find...

    {clear}

    ... no one there.

    It's more than a little weird. Whoever was knocking was banging on his door like their life depended on it. The whole neighborhood could've woken up and filed complaints about the noise.
    
    Why wasn't there anyone around?

    {clear}
    """

    show protag closedeyes

    narrator """
    Whatever, it's way too early for this kind of nonsense.
    
    Grumbling, [protag] decides to head back to bed. 
    """

    show protag closedeyes:
        xzoom 1.0

    protag "I need to get out of this place already--"

    show protag at right
    show li default at left

    li "Hi." (who_color="#575c69")

    return