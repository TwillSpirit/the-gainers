label start:
    $ quick_menu = False
    show screen splash_screen("CHAPTER 1", "BEGINNING")
    with Fade(1.0,1.0,1.0,color=color.white)
    pause(2.0)
    hide screen splash_screen
    jump story_begin
    return