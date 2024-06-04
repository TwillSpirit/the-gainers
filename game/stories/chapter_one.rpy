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
    dan.character "We went at the same university."
    dan.character "I am majored at IT."
    dan.character "While he is majored at Graphic Design."
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
    window hide
    pause (2.0)

    window show
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

    show screen simple_splash_screen("After a nice 30 minutes of shower session.")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg dan_room
    hide screen simple_splash_screen
    with Dissolve(0.5)
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

    show screen simple_splash_screen("30 minutes later, Dan arrived at his favourite cafe")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)

    show bg cafe
    hide screen simple_splash_screen
    with Dissolve(0.5)
    
    show Dan
    with easeinleft

    dan.character mouth_open "Finally arrived."
    dan.character eyes_happy "Time to order and do the work!~"

    hide Dan
    with easeoutright

    show screen simple_splash_screen("Several minutes later...")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg coding_session
    hide screen simple_splash_screen
    with Dissolve(0.5)

    dan.character "Alright! "
    extend "Let's do this!"

    window hide
    show screen narator_screen("Dan is doing his project for straight 1 hour. When suddenly he got a call from an unknown number.")
    with Dissolve(0.5)
    pause(3.0)

    scene bg coding_session
    hide screen narator_screen
    with Dissolve(0.5)
    
    show Phone
    show Ringing
    with dissolve

    pause 1.0
    dan.character "Hmmm....?"
    dan.character "Unknown number?"
    dan.character "I feel reluctant to answer this number..."
    dan.character "{i}What should I do{/i}"

    menu:
        "Answer the phone":
            pass
        "Don't answer the phone":
            jump reject_call
            pass
            #block of code to run
        

    return

label reject_call:
    dan.character "Yeah no, I'm gonna reject it. "
    extend "Probably some sort of scam or something."

    hide Phone
    hide Ringing
    with dissolve

    dan.character "Now let's get back to work."
    window hide
    pause 1.0
    jump gerald_coming
    return

label gerald_coming:
    scene black
    with Dissolve(0.1)

    pause 1.0
    
    dan.character "WHAAAA--!!!"
    "???" "Guess who...?~"
    dan.character "GET OFF YOUR HA-"
    dan.character "{i}Wait a minute... {/i}"
    extend "{i}That voice... {/i}"
    extend "{i}it sounds like ... {/i}"
    extend "{i}Gerald...? {/i}"
    dan.character "{i}No way... {/i}"
    extend "{i}is it really him? {/i}"

    scene bg cafe
    with dissolve
    show Gerald at left
    with dissolve

    gerald.character eyes_happy mouth_open "Surprise, tech nerd! "
    extend "It's been a long time huh?~"

    show Gerald mouth_smile
    show Dan:
        left
        xzoom -1.0
        xanchor -1.0
    with dissolve
    dan.character mouth_open "NO WAY!!! "
    extend "IT'S REALLY YOU!!!"

    gerald.character eyes_open mouth_open "The one and the only.~"
    dan.character eyes_happy mouth_open "Gosh! "
    extend "You have zero idea how much I miss you my friend!"
    gerald.character eyes_closed mouth_open "Yeah, "
    extend "I'm sorry for my sudden disappearance. "
    extend "Should have contact you earlier."
    dan.character eyes_open mouth_open "Also, why are you here tho? "
    gerald.character eyes_open "I just miss this city, and also you buddy. "
    extend "So I booked a ticket and I have decided that I will stay in here.~"