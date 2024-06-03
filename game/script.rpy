label start:
    scene bg beach
    with fade

    """Welcome to the game"""

    show Dan
    with easeinleft

    dan.character  "Welcome to the game."
    dan.character happy talk "Please customise this project as you wish!~"
    dan.character happy -talk "and don't forget to back your code to github!~"
    dan.character -happy talk "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the {b}1960s{/b} with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    
    jump story_begin
    return

