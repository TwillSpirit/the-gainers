label start:
    scene bg beach
    with fade

    """Welcome to the game"""

    show Twill
    with easeinleft

    twill.character  "Welcome to the game."
    twill.character happy talk "Please customise this project as you wish!~"
    twill.character happy -talk "and don't forget to back your code to github!~"
    
    jump story_begin
    return

