init python:
    def changeFont(newFont):
        return SetField(persistent,"gui_font",newFont),SetField(persistent,"pref_text_size", size_dict[newFont][persistent.pref_text_scale]),SetField(persistent,"pref_text_spacing",size_dict[newFont]['line_spacing']),SelectedIf(persistent.gui_font == newFont)
        ###

    def changeScale(newScale):
        return SetField(persistent,"pref_text_scale",newScale),SetField(persistent,"pref_text_size", size_dict[persistent.gui_font][newScale])
    
    ###Size Dictionary
    # Organized in dicts, follow the order below to create your font:size pairings.
    # Since lots of fonts use different vertical heights, it's highly recommended you include a "line_spacing" key for
    # each entry.
    # For advanced usage, if you do a font size slider you can make these minimum and maximum sizes!

    size_dict = {
        # "filepath" : {"size_scale1" : size in pixels, "size_scale2" : size in pixels...},
        # For advanced usage, you can make these dicts hold any optional arguments you want per font.
        "fonts/OpenDyslexic.otf" : {
            "regular" : 22,
            "large" : 26,
            "line_spacing" : -15,
            "line_overlap_split": 10
        },

        "DejaVuSans.ttf" : {
            "regular" : 24,
            "large" : 28,
            "line_spacing" : 0,
            "line_overlap_split": 0
        },

        "fonts/brassmono.ttf" : {
            "regular" : 28,
            "large" : 30,
            "line_spacing" : 0,
            "line_overlap_split": 0
        },

        "fonts/Hyperlegible.ttf" : {
            "regular" : 26,
            "large" : 28,
            "line_spacing" : -4,
            "line_overlap_split": 2
        },
        
        "fonts/Nunito.ttf" : {
            "regular" : 24,
            "large" : 28,
            "line_spacing" : -6,
            "line_overlap_split": 6
        },

    }