label start:
    $ quick_menu = False
    $ should_show_side_image = False    

    scene black
    with Fade(1.0,0.0,1.0,color=color.black)

    if persistent.char_name == "" and persistent.chapter_one_complete == False:
        $ persistent.char_name = renpy.input("What is your name?", "Dan")
        $ persistent.char_name = persistent.char_name.strip()

        if persistent.char_name == "":
            $ persistent.char_name = "Dan"

    elif persistent.chapter_one_complete == True:
        """You know the word \"patient\"?
        
        If you know, go wait for now and touch the grass.
        
        If you don't, you're a dumbhead."""

        return
    

    show screen splash_screen("CHAPTER 1", "BEGINNING")
    with Fade(1.0,1.0,1.0,color=color.white)
    pause(2.0)
    hide screen splash_screen
    jump story_begin
    return