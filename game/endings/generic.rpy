label generic_ending():
    
    scene black with fade

    # qirin ending blurb
    show qirin neutral at center with dissolve

    if qirin_truth:
        show qirin closedeyes with dissolve

        narrator "[qirin] made a choice to confront their family over their excessive concerns. Things were messy and almost explosive in the beginning, but over time and effort, [qirin] and their parents came to a mutual understanding."
    elif qirin_desire:
        show qirin smile with dissolve

        narrator "[qirin] sought support from their partner and friends, and decided to seek out new friendships and opportunities instead. They drifted from their parents to their slowly growing support network of people who they considered their chosen family."
    elif qirin_joke:
        show qirin shades with dissolve

        narrator "In a fit of mischief, [qirin] booked a flight to the Bahamas to go on a second honeymoon with their partner. They enjoyed the sights and pleasures on their vacation, to the point where they and their partner decided to settle into a new home on the islands."
    else:
        return

    hide qirin

    # reaper ending blurb
    show reaper neutral at center with dissolve

    if reaper_truth:
        show reaper happy with dissolve

        narrator "[reaper] went on a self-discovery journey in the wake of her career being put on hold. She traveled across the world, making friends and memories and experiences. While she never returned to being a reaper, she took her first steps towards inner peace."
    elif reaper_desire:
        show reaper smile with dissolve

        narrator "[reaper] decided to follow her dreams of owning her own business. After much hard work, [reaper] finally established a business of her own - where she was in charge and made the important decisions. She was considered one of the best in her line of work."
    elif reaper_joke:
        show reaper pottery with dissolve

        narrator "After much debating, [reaper] tried out pottery. During her first pottery class, she met someone special and eventually fell in love with both the art and the person. Now, she loves making mugs and teawares alongside her new girlfriend."
    else:
        return

    hide reaper

    # li ending blurb
    show li neutral at center with dissolve

    if li_truth:
        show li smile with dissolve

        narrator "[li] took a chance and tried some speed dating. Though he got along with many of his dates, none of them quite connected. Eventually, he settled down with a lovely person and they've been going steady ever since."
    elif li_desire:
        jump desire_ending.love_ending
    elif li_joke:
        show li fear with dissolve

        narrator "Though he respected [protag], [li] didn't quite take the ominous warning seriously. Eventually, he experienced a string of bad luck whenever birds were around him. He developed a healthy fear of them and now actively avoids birds wherever he goes."
    else:
        return

    return

label .cafe():

    # return to cafe
    scene bg cafe with fade
    show protag smile at center with dissolve

    narrator "Though [protag] read fortunes at the cafe, it doesn't quite the garner a reputation for being a fortune-reading establishment. But they still brew a damn good cup of coffee and serve really cute pastries."

    return