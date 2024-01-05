## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        textbutton _("Preferences") action ShowMenu("preferences")

        if not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    outlines [ (absolute(3), "#e3decf", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(3), "#885138", absolute(0), absolute(0)) ]
    selected_outlines [ (absolute(3), "#c7b9a700", absolute(0), absolute(0)) ]

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use title_menu

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    # background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Custom Title Menu ###########################################################
## 
## Customizing the menu in the title screen with image buttons!
## 
## https://www.renpy.org/doc/html/screens.html#imagebutton

screen title_menu():

    style_prefix "title_menu"

    vbox:
        
        hbox:
            imagebutton auto "gui/start %s.png" action Start() alt _("Start")
            imagebutton auto "gui/load %s.png" action ShowMenu("load") alt _("Load")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                imagebutton auto "gui/help %s.png" action ShowMenu("help") alt _("Help")

        hbox:
            imagebutton auto "gui/pref %s.png" action ShowMenu("preferences") alt _("Options")
            imagebutton auto "gui/quit %s.png" action Quit(confirm=True) alt _("Quit")

style title_menu_vbox:
    yoffset -10
    xsize 500
    ysize 150
    align (0.5, 0.5)
    spacing gui.navigation_spacing

style title_menu_hbox:
    xalign 0.5
    spacing 20

style title_menu_image_button:
    hover_sound "audio/select.ogg"
    activate_sound "audio/confirm.ogg"