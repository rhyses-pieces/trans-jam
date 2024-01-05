# Dropdown menu screen 
# source: https://patreon.renpy.org/dev-2022-05.html#drop-down-menus
# create a class for the dropdown 
init python:
    @renpy.pure
    class Dropdown(Action):
        """
        This is an action that displays a drop-down menu based on the labels
        and actions given to it as arguments. This takes an even number of
        arguments, with arguments grouped into pairs.

        `odd arguments`
            The first, third, fifth, and other odd numbered arguments are the
            labels for the drop-down menu, expected to be strings.

        `even arguments`
            The second, fourth, sixth, and other even numbered arguments are
            the actions to be taken when the corresponding label is selected.
        """

        def __init__(self, *args):

            # Group the arguments into pairs.
            labels = args[0::2]
            actions = args[1::2]
            self.entries = list(zip(labels, actions))

        def __call__(self):

            # When activated, capture the focus, then show the drop down screen.
            renpy.capture_focus("dropdown")
            renpy.show_screen("dropdown", entries=self.entries)
            renpy.restart_interaction()

# define the dropdown screen
screen dropdown(entries):
    style_prefix "drop"
    zorder 999

    dismiss action Hide()

    nearrect:
        focus "dropdown"
        
        frame:
            style "empty"
            background "#e3decf"
            padding (10, 10)

            has vbox

            for label, action in entries:
                textbutton label action [ Hide(), action ]

style drop_button:
    idle_background "#e3decf"
    hover_background "#fff"
    selected_background "#885138"
    xsize 281

style drop_button_text:
    selected_color "#fff"

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    # comment out below to make preference purely custom
    # use game_menu(_("Preferences"), scroll="viewport"):
    
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        align (0.5, 0.5)
        xpadding 50
        ypadding 50

        vbox:

            hbox:
                box_wrap True
                align (0.5, 0.5)

                hbox:
                    vbox:
                        style_prefix "check"
                        label _("Accessibility")
                        
                        textbutton _("Sound Captions") action ToggleVariable("persistent.sound_captions")
                        textbutton _("Image Captions") action ToggleVariable("persistent.image_captions")

                        # Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
                        if renpy.variant("pc"):
                            textbutton _("Self-Voicing") action Preference("self voicing", "toggle")
                    
                    vbox:
                        #Change Font
                        textbutton "Font":
                            background "#e3decf"
                            xsize 160
                            action Dropdown(
                                "{font=fonts/brassmono.ttf}Brass Mono", [changeFont("fonts/brassmono.ttf"),SelectedIf(persistent.gui_font == "fonts/brassmono.ttf")],
                                "{font=fonts/Hyperlegible.ttf}Atkinson Hyperlegible", [changeFont("fonts/Hyperlegible.ttf"),SelectedIf(persistent.gui_font == "fonts/Hyperlegible.ttf")],
                                "{font=fonts/Nunito.ttf}Nunito", [changeFont("fonts/Nunito.ttf"),SelectedIf(persistent.gui_font == "fonts/Nunito.ttf")],
                                "{font=fonts/OpenDyslexic.otf}Open Dyslexic", [changeFont("fonts/OpenDyslexic.otf"),SelectedIf(persistent.gui_font == "fonts/OpenDyslexic.otf")],
                                "{font=DejaVuSans.ttf}DejaVu Sans", [changeFont("DejaVuSans.ttf"),SelectedIf(persistent.gui_font == "DejaVuSans.ttf")],
                            )
                        vbox:
                            #Change Font Size
                            label _("Text Size")
                            style_prefix "radio"
                            textbutton _("Regular") action [changeScale(newScale="regular"),SelectedIf(persistent.pref_text_scale == "regular")]
                            textbutton _("Large") action [changeScale(newScale="large"),SelectedIf(persistent.pref_text_scale == "large")]

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                
                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True
                xalign 0.5

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height (4 * gui.pref_spacing)

            textbutton _("Return") action Return()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450