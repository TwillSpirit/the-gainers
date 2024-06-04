label story_begin:
    scene bg alarm
    $ quick_menu = True
    with Fade(1.0, 1.0, 1.0, color=color.white)

    """RING, RING, RING! IT'S 7 IN THE MORNING
    
    RAISE AND SHINE TO THE WORLD!
    
    {i}*click{/i}"""

    scene bg dan_room
    with dissolve

    dan.character naked eyes_mid_open mouth_smile "{i}yawn...{/i}"
    dan.character "Man... "
    extend "it was a really nice sleep.~"

    show Dan with dissolve
    dan.character "..."
    dan.character mouth_flat "..."
    dan.character "Right... "
    extend "I still have a lot projects need to be done."
    dan.character "I wish Gerald's here and help me with this project."
    dan.character "But he just disappeared 4 months after we graduated."

    hide Dan
    with dissolve
    scene bg graduated_pic
    with dissolve

    dan.character "Me and Gerald are best friend."
    dan.character "We went at the same university and the same classes"
    dan.character "We both majored at IT."
    dan.character "After the graduation, Gerald got called that he have to went overseas with his parent."
    dan.character "I tried to call him if he's alright because I quite miss him, "
    extend "but no avail."
    dan.character "He always set his phone busy."
    dan.character "I just wish that he'll come visit again."

    scene bg dan_room
    show Dan naked eyes_mid_open mouth_flat
    with dissolve

    dan.character "Enough ranting Dan. "
    extend "The day is still young."
    dan.character mouth_smile "I'm gonna take a good warm shower now"

    hide Dan
    with easeoutright

    scene bg shower
    with dissolve
    pause (3.0)

    dan.character "Gonna turn on this radio as well ~"

    pause (2.0)

    radio.character "Tired of being called skinny? "
    extend "Say no more! "
    radio.character "With this ring, "
    extend "You can grow your muscles! "
    extend "It will help you to become stronger as well! "
    extend "And, you will not be called skinny anymore!~"

    dan.character "Ring... "
    extend "that grow your muscles?"
    dan.character "..."
    dan.character "What a stupid advertisement."
    dan.character "No idea if it's real or not, but that just too good to be true."

    scene bg dan_room
    with dissolve

    show Dan:
        xzoom -1.0
        xanchor -0.5
    with easeinright

    dan.character normal eyes_happy mouth_open "What a good shower.~"
    dan.character mouth_smile "It helps to lift up my mood.~"
    dan.character eyes_open mouth_open "Alright! "
    extend "It's time to do the project.~"
    dan.character mouth_smile "I think I'll working on it in the cafe as well. "
    extend "Gotta love the coffee they make.~"

    hide Dan
    with easeoutleft

    scene black
    with fade

    return