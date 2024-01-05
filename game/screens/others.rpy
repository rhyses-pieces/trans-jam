## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"
        
        frame:
            vbox:
                spacing 15

                hbox:

                    textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    # hbox:
    #     label "Shift+A"
    #     text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_frame is gui_frame:
    xfill True
    ypadding 25
style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

################################################################################
## Credit Screen
################################################################################

transform credits_scroll(speed):
    ypos 900
    linear speed ypos -900

screen credits():
    style_prefix "credits"

    add gui.game_menu_background

    frame at credits_scroll(25):
        xalign 0.5

        vbox:
            label "Credits" style "credits_header"

            null height 20

            vbox:
                text "Art, Programming, Writing" style "credits_title"
                
                hbox:
                    vbox:
                        text "Rhys"

            null height 10

            vbox:
                text "Editing" style "credits_title"

                hbox:
                    vbox:
                        text "Andy Paradoxic"
                    vbox:
                        text "unlockthelore"
            
            null height 10

            # vbox:
            #     text "Testing"

            #     hbox:
            #         vbox:
            #             text "Andy Paradox"
            #         vbox:
            #             text "Dom"

            vbox:
                text "BGM" style "credits_title"

                hbox:
                    vbox:
                        textbutton "Kevin MacLeod" action OpenURL("https://incompetech.com/")
                    vbox:
                        textbutton "Mayra" action OpenURL("https://mayragandra.itch.io/freeambientmusic")
                
                hbox:
                    vbox:
                        textbutton "Nid" action OpenURL("https://ryusuke0215.itch.io/piano-music2")
                    vbox:
                        textbutton "potat0master" action OpenURL("https://potat0master.itch.io/free-background-music-for-visual-novels-bgm-pack-1")
                    
            null height 10

            vbox: 
                text "SFX" style "credits_title"

                hbox:
                    vbox:
                        textbutton "dmochas-assets" action OpenURL("https://dmochas-assets.itch.io/dmochas-bleeps-pack")
                    vbox:
                        textbutton "SoupTonic" action OpenURL("https://souptonic.itch.io/souptonic-sfx-pack-1-ui-sounds")
            
            null height 10

            vbox:
                text "Programming Assets" style "credits_title"

                hbox:
                    vbox:
                        textbutton "SoDaRa" action OpenURL("https://github.com/SoDaRa/Auto-Highlight")
                    vbox:
                        textbutton "NPCKC" action OpenURL("https://npckc.itch.io/caption-tool-for-renpy")

                hbox:
                    vbox:
                        textbutton "tofurocks" action OpenURL("https://tofurocks.itch.io/renpy-history")
                    vbox:
                        textbutton "nyaatrap" action OpenURL("https://github.com/nyaatrap/renpy-utilities")

    timer 25 action [Hide("credits", Fade(1, 0, 0.5)), Return()]

style credits_button is gui_button
style credits_button is gui_button_text

style credits_frame:
    padding (25, 20)

style credits_hbox:
    xalign 0.5
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    spacing 20

style credits_header_text:
    size 60
    text_align 0.5

style credits_header:
    xalign 0.5

style credits_title:
    xalign 0.5
    size 40
    bold True

style credits_text is gui_text:
    text_align 0.5

style credits_button_text:
    text_align 0.5
    idle_color "#fff"
    hover_color "#885138"
    outlines [ (absolute(3), "#885138", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(3), "#e3decf", absolute(0), absolute(0)) ]