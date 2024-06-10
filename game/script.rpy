# If this game is under development stage, set it to False
# If this game is ready for production, set it to True
define is_production = False

label start:
    $ quick_menu = False
    $ should_show_side_image = False

    stop music fadeout 1.0
    scene black
    with Fade(1.0,0.0,1.0,color=color.black)

    # Checking if the user just start playing the game
    # If it's the first time, ask user to input their name or any name they want it
    if persistent.chapter_one_complete == False:
        $ persistent.char_name = renpy.input("What is your name? If you let it empty, your default name will be \"Dan\"", "Dan")
        $ persistent.char_name = persistent.char_name.strip()

        # If user input string is empty, just set the name into default Dan
        if persistent.char_name == "":
            $ persistent.char_name = "Dan"

    # If it's still under development, make sure that the chapter is selectable
    if is_production == False:
        if persistent.chapter_one_complete == True:
            menu:
                "Select the chapter"
                "Chapter 1":
                    jump chapter_one
                "Chapter 2":
                    jump chapter_two

    # While the game is not under development stage anymore this script will be run
    show screen splash_screen("CHAPTER 1", "BEGINNING")
    with Fade(1.0,1.0,1.0,color=color.white)
    pause(2.0)
    hide screen splash_screen
    jump story_begin
    return