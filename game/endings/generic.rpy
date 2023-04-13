label generic_ending():
    
    scene black with fade

    # qirin ending blurb
    show qirin neutral at center with dissolve

    if qirin_truth:
        show qirin closedeyes with dissolve

        narrator "[qirin] made a choice to confront their family over their excessive concerns. Things were messy and almost explosive in the beginning, but over time and effort, [qirin] and their parents came to a mutual understanding."
    elif qirin_desire:
        show qirin smile with dissolve

        narrator "[qirin] sought support from their partner and friends, "
    elif qirin_joke:
        show qirin shades with dissolve

        narrator ""
    else:
        return

    hide qirin

    # reaper ending blurb
    show reaper neutral at center with dissolve

    if reaper_truth:
        show reaper happy with dissolve

        narrator ""
    elif reaper_desire:
        show reaper smile with dissolve

        narrator ""
    elif reaper_joke:
        # show reaper clay with dissolve

        narrator ""
    else:
        return

    hide reaper

    # li ending blurb
    show li neutral at center with dissolve

    if li_truth:
        show li smile with dissolve

        narrator ""
    elif li_desire:
        jump desire_ending
    elif li_joke:
        show li think with dissolve

        narrator ""
    else:
        return

    return

label .cafe():

    # return to cafe
    scene bg cafe with fade

    return