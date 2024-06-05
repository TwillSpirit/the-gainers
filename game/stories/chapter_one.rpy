default coffee_selection = ""

label story_begin:
    scene bg alarm
    $ quick_menu = True
    with Fade(1.0, 1.0, 1.0, color=color.white)

    """{b}WAKEY WAKEY WAKEY YOU SLEEPY HEAD!!!{/b}

    {b}IT'S 7 O'CLOCK AND IT'S A BRAND NEW DAY!!!{/b}
    
    {i}*click{/i}"""

    scene bg dan_room
    with dissolve

    dan.character naked eyes_mid_open mouth_smile "{i}yawn...{/i}"
    dan.character "Hngggggg... {w}Oh boi... {w} What a good sleep it was.~"

    show Dan with dissolve
    dan.character "... {w}......"
    dan.character mouth_open_2 "Ah... {w}right... {w} I still have a lot projects need to be done."
    dan.character mouth_flat "Gosh... {w}I wish I didn't sign for this project. {w}But I have to earn money to stay alive... {w}and last night was a hell of meeting and debugging session."
    
    show Dan:
        flip

    dan.character "..."
    dan.character eyes_closed mouth_open_2 "This flat feels empty without {b}him{/b}."
    dan.character naked eyes_mid_open "He often helped me with this kind of mess."


    hide Dan
    with dissolve
    scene bg graduated_pic
    with dissolve

    dan.character "Me and Gerald are best friend."
    dan.character "We went at the same university."
    dan.character "I am majored at IT, {w}while he is majored at Graphic Design."
    dan.character "Even tho we were not studied the same thing, {w}his interest in programming stuff is quite high. {w}Often he fixed my buggy program."
    dan.character "But after the graduation, {w}he got called that he have to went overseas with his parent."
    dan.character "I tried to call him if he's alright because I quite miss him, {w}but no avail. {w}Because the operator said the number had been expired."
    dan.character "Gosh... {w}I just really wish that he'll come back visit again."

    scene bg dan_room
    show Dan naked eyes_mid_open mouth_flat
    with dissolve

    dan.character "Shut your mouth Dan. "
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
    radio.character "Tired of being called skinny? {w}SAY NO MORE!"
    radio.character "With this ring, {w}You can become into an absolute UNIT! {w}You will become STRONGER! {w}BIGGER! {w}And most importantly... {w}you will NOT be called skinny anymore!"
    radio.character "So grab these ring RIGHT NOW!!! {w} We have tested to tenth of people, {w}and everyone LOVE IT!!! {w} Better grab and sign up right now before it's too late!!"

    dan.character "Ring... "
    extend "that make you stronger... {w} and bigger?"
    dan.character "..."
    dan.character "What a stupid advertisement. {w}No idea of how many folks that fall into that."
    dan.character "But why does it sound so legit tho?"
    dan.character "Ah...... {w}probably a scam."

    show screen simple_splash_screen("After a nice 30 minutes of shower session.")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg dan_room
    hide screen simple_splash_screen
    with Dissolve(0.5)
    show Dan:
        center
        xzoom -1.0
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

    dan.character eyes_open mouth_smile "{i}What coffee should I order?{/i}"

    menu:
        "Cappuccino":
            $ coffee_selection = "Cappucino"
        "Latte":
            $ coffee_selection = "latte"
        "Espresso":
            $ coffee_selection = "Espresso"

    dan.character @ mouth_open "Let's order [coffee_selection] this time.~"

    hide Dan
    with easeoutright

    show screen simple_splash_screen("Several minutes later...")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg coding_session
    hide screen simple_splash_screen
    with Dissolve(0.5)

    $ should_show_side_image = True
    dan.character eyes_happy mouth_open "Alright! "
    dan.character eyes_open mouth_open "My Laptop's ready, "
    extend "My coffee's ready! "
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
    $ should_show_side_image = True
    dan.character eyes_confused mouth_flat "Hmmm....? {w}Unknown number?"
    dan.character "I feel reluctant to answer this number..."
    dan.character "{i}What should I do{/i}"

    menu:
        "Answer the phone":
            jump answer_call
            pass
        "Don't answer the phone":
            jump reject_call
            pass
            #block of code to run
        
    return

label answer_call:
    hide Ringing
    with dissolve
    $ should_show_side_image = True
    dan.character eyes_confused mouth_flat "I'll try to answer it."
    dan.character "{i}*pick up the phone*{/i}"
    dan.character mouth_open_2 "Greetings. {w}Dan is here. {w}May I help you?"
    "???" "Hello man... {w}It's been a while since I hear your voice. {w}Please remain on your spot because I will visit you."
    
    hide Phone
    with dissolve

    dan.character eyes_surprised mouth_open_2 "WAIT-"
    dan.character eyes_surprised mouth_open_2 "..."
    dan.character eyes_confused mouth_open_2 "He hung up the phone..."
    dan.character eyes_confused mouth_flat "Man... {w} Can I have just at least one normal day?"
    dan.character eyes_confused mouth_open_2 "But also... {w}why does it sounds like [gerald.name] {w}but a bit deep?"
    dan.character eyes_closed mouth_open_2 "Let just get back to work Dan. {w}Do not let anything distract you right now."
    window hide
    pause 1.0
    jump gerald_coming
    return

label reject_call:
    dan.character "Yeah no, I'm gonna reject it. {w}Probably some sort of scam or something."

    hide Phone
    hide Ringing
    with dissolve

    dan.character "Now let's get back to work."
    window hide
    pause 1.0
    jump gerald_coming
    return

label gerald_coming:
    $ should_show_side_image = False
    scene black
    with Dissolve(0.1)

    pause 1.0
    
    dan.character "WHAAAA--!!!"
    "???" "Guess who...?~"
    dan.character "GET OFF YOUR HA-"
    dan.character "{i}Wait a minute... {w}That voice... {w}it sounds like the guy on the phone earlier{/i}"
    dan.character "{i}Shit... {w}I'm so scared...{/i}"

    scene bg cafe
    with dissolve
    show Gerald:
        xpos 0.25
    with dissolve

    gerald.character eyes_happy mouth_open "Surprise, tech nerd! "
    extend "It's been a long time huh?~"

    show Gerald mouth_smile
    show Dan eyes_surprised mouth_flat:
        xpos 0.75
        xzoom -1.0
        pause 0.5
        bounce
    with dissolve
    dan.character eyes_surprised mouth_open_2 "NO WAY!!! {w} GERALD?!! {w} IS IT REALLY YOU?!!"

    gerald.character eyes_open @ mouth_open "The one and the only.~"
    dan.character "Gosh! {w}you scared the shit out of me!"
    gerald.character @ eyes_happy mouth_open "Hehehe...~ I'm sorry [dan.name]."
    dan.character "Also... {w}WHAT AN ABSOLUTE UNIT YOU ARE [gerald.name]! {w}Did you take some steroids? {w}Because no way 4 months can get you this result."
    gerald.character eyes_happy mouth_open "Hehehe... {w}Thanks for the compliment nerd. "
    show Gerald eyes_open
    extend "But no. {w}I didn't take any steroid. {w}I have my own way.~"
    dan.character mouth_open "REALLY?! {w}What is it I wanna know!"
    gerald.character eyes_closed mouth_open "It's secret.~"
    dan.character eyes_confused mouth_open_2 "Aw... shucks..."
    gerald.character eyes_happy mouth_smile "Hehehe...~"
    dan.character eyes_open mouth_open "But anyway... "
    show Dan eyes_happy
    dan.character "Gosh I'm so happy to see you again bud!"
    gerald.character eyes_happy mouth_open "Likewise [dan.name]"
    dan.character eyes_confused @ mouth_open "Also, {w}why are you here tho?"
    gerald.character eyes_open mouth_smile "I just miss this city, and also you buddy. "
    show Gerald eyes_happy mouth_open
    extend "So I booked a ticket and I have decided that I will stay in here.~"
    dan.character eyes_happy "Oh great! "
    show Dan eyes_open
    extend "But, "
    show Dan eyes_confused
    extend "where are you staying?"
    gerald.character eyes_open mouth_open "I live in the flat 3 blocks from here. {w}You can come visit your old friend sometimes.~"
    dan.character eyes_happy "Oh absolutely! {w}I can come to your flat every single day if you want.~"
    gerald.character eyes_happy mouth_open "Hahahah...~ Fair.~ "

    gerald.character eyes_open mouth_open "May I join what are you doing right now buddy?"
    dan.character eyes_open mouth_open "Sure thing man! {w}In fact... {w}I need some sort of \"accompany\""
    gerald.character eyes_happy mouth_open "Hehehe... {w}Very well nerdy.~"

    show Dan mouth_smile eyes_open:
        xpos 0.75
        unflip
    
    pause 0.5
    hide Dan
    hide Gerald
    with easeoutright

    show screen simple_splash_screen("END OF CHAPTER I")
    $ quick_menu = False
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(5.0)

    scene black
    hide screen simple_splash_screen
    with Dissolve(0.5)

    """Chapter II in development.
    
    Be patient because we don't have a lot of team right now LMAO."""

    $ persistent.chapter_one_complete = True

    return