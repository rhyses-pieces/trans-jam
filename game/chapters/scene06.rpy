label scene06():

    play music cafe_bgm fadein 1.0 loop
    play audio cafe_ambiance fadein 1.0 volume 0.5 loop

    scene bg cafe with Fade(0.5, 1, 0.5)

    show protag smile at inR with Pause(0.5)
    
    protag neutral @ closedeyes "All in a day's work!"

    show li neutral:
        xzoom -1.0
        inL()
    with Pause(0.5)
    
    li @ think "What was that about?"
    protag ""
    
    return