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

    dan 011 "{i}yawn...{/i}"
    dan "Hngggggg... {w}Oh boi... {w} What a good sleep it was.~"

    show Dan with dissolve
    dan "... {w}......"
    dan 001 "Ah... {w}right... {w} I still have a lot projects need to be done."
    dan 021 "Gosh... {w}I wish I didn't sign for this project. {w}But I have to earn money to stay alive... {w}and last night was a hell of meeting and debugging session."
    
    show Dan:
        flip

    dan "..."
    dan 000 "This flat feels empty without {b}him{/b}."
    dan 021 "He often helped me with this kind of mess."


    hide Dan
    with dissolve
    scene bg graduated_pic
    with dissolve

    dan "Me and Gerald are best friend."
    dan "We went at the same university."
    dan "I am majored at IT, {w}while he is majored at Graphic Design."
    dan "Even tho we were not studied the same thing, {w}his interest in programming stuff is quite high. {w}Often he fixed my buggy program."
    dan "But after the graduation, {w}he got called that he have to went overseas with his parent."
    dan "I tried to call him if he's alright because I quite miss him, {w}but no avail. {w}Because the operator said the number had been expired."
    dan "Gosh... {w}I just really wish that he'll come back visit again."

    scene bg dan_room
    show Dan 001
    with dissolve

    dan "Cut it off [persistent.char_name]. {w}The day is still young."
    dan 011 "I'm gonna take a good warm shower now"

    hide Dan
    with easeoutright

    scene bg shower
    with dissolve
    pause (3.0)

    dan "Gonna turn on this radio as well ~"
    window hide
    pause (2.0)

    window show
    radio.character "Tired of being called skinny? {w}SAY NO MORE!"
    radio.character "With this ring, {w}You can become into an absolute UNIT! {w}You will become STRONGER! {w}BIGGER! {w}And most importantly... {w}you will NOT be called skinny anymore!"
    radio.character "So grab these ring RIGHT NOW!!! {w} We have tested to tenth of people, {w}and everyone LOVE IT!!! {w} Better grab and sign up right now before it's too late!!"

    dan "Ring... "
    extend "that make you stronger... {w} and bigger?"
    dan "..."
    dan "What a stupid advertisement. {w}No idea of how many folks that fall into that."
    dan "But why does it sound so legit tho?"
    dan "Ah...... {w}probably a scam."

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

    dan 133 "Ah...~ {w}What a nice shower.~"
    dan 113 "It helps to lift up my mood.~"
    dan 132 "Alrighty! {w}It's time to working on the project.~"
    dan 112 "Might gonna do it in the cafe as well. {w}Gotta love the coffee they make.~"

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

    dan 132 "Finally arrived."
    dan "Time to order and do the work!~"

    dan 112 "{i}What coffee should I order?{/i}"

    menu:
        "Cappuccino":
            $ coffee_selection = "Cappucino"
        "Latte":
            $ coffee_selection = "latte"
        "Espresso":
            $ coffee_selection = "Espresso"

    dan 132 "Let's order [coffee_selection] this time.~"

    hide Dan
    with easeoutright

    show screen simple_splash_screen("Several minutes later...")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg coding_session
    hide screen simple_splash_screen
    with Dissolve(0.5)

    $ should_show_side_image = False
    dan "Alright! "
    dan "My Laptop's ready, {w}My coffee's ready! {w}Let's do this!"

    window hide
    show screen narator_screen(f"{persistent.char_name} is doing his project for straight 1 hour. When suddenly he got a call from an unknown number.")
    with Dissolve(0.5)
    pause(3.0)

    scene bg coding_session
    hide screen narator_screen
    with Dissolve(0.5)
    
    show Phone
    show Ringing
    with dissolve

    pause 1.0
    dan "Hmmm....? {w}Unknown number?"
    dan "I feel reluctant to answer this number..."
    dan "{i}What should I do{/i}"

    menu:
        "Answer the phone":
            jump answer_call
            pass
        "Don't answer the phone":
            jump reject_call
            pass
        
    return

label answer_call:
    hide Ringing
    with dissolve
    dan  "I'll try to answer it."
    "{i}*pick up the phone*{/i}"
    dan  "Greetings. {w}[persistent.char_name] speaking. {w}May I help you?"
    "???" "Hello man... {w}It's been a while since I hear your voice. {w}Please remain on your spot because I will visit you."
    
    hide Phone
    with dissolve

    dan "WAIT-"
    dan "..."
    dan "He hung up the phone..."
    dan "Man... {w} Can I have just at least one normal day?"
    dan "But also... {w}why does it sounds like Gerald {w}but a bit deep?"
    dan "Let just get back to work [persistent.char_name]. {w}Do not let anything distract you right now."
    window hide
    pause 1.0
    jump gerald_coming
    return

label reject_call:
    dan "Yeah no, I'm gonna reject it. {w}Probably some sort of scam or something."

    hide Phone
    hide Ringing
    with dissolve

    dan "Now let's get back to work."
    window hide
    pause 1.0
    jump gerald_coming
    return

label gerald_coming:
    $ should_show_side_image = False
    scene black
    with Dissolve(0.1)

    pause 1.0
    
    dan "WHAAAA--!!!"
    "???" "{bt=3}Guess who...?~{/bt}"
    dan "GET OFF YOUR HA-"
    dan "{i}Wait a minute... {w}That voice... {w}it sounds like the guy on the phone earlier{/i}"
    dan "{i}Shit...{/i} {w}{sc=2}{i}I'm so scared...{/i}{/sc}"
    window hide
    
    pause 1.0

    scene bg cafe
    with dissolve
    show Gerald:
        xpos 0.5
    with dissolve

    gerald 122 "Surprise, tech nerd! "
    extend "It's been a long time huh?~"
    
    show Gerald 111 at move_pos(0.3, 0.5)
    show Dan 124:
        xpos 0.7
        xzoom -1.0
        pause 0.5
        bounce
    with easeinright
    dan 124 "NO WAY!!! {w} GERALD?!! {w} IS IT REALLY YOU?!!"

    gerald 120 "The one and the only.~"
    dan "Gosh! {w}you scared the {sc=2}{b}{color=#ff0000}SHIT OUT OF ME!{/color}{/b}{/sc}"
    gerald 122 "Hehehe...~ I'm sorry [persistent.char_name]."
    dan 124 "Also... "
    show Dan 126 at move_pos(0.6, 0.2)
    extend "WHAT AN ABSOLUTE UNIT YOU ARE MATE! {w}Did you take some steroids or something? {w}Because there is no way 4 months can get you this result."
    show Dan at move_pos(0.7, 0.2)
    gerald 122 "Hehehe... {w}Thanks for the compliment nerd. "
    show Gerald 112
    extend "But no. {w}I didn't take any steroid. {w}I have my own way.~"
    show Dan 134 at bounce
    dan  "REALLY?! {w}What is it I wanna know!"
    gerald 110 "It's secret.~"
    dan 125 "Aw... shucks..."
    gerald 122 "Hehehe...~"
    dan 132 "But anyway... "
    show Dan 133
    dan "Gosh I'm so happy to see you again bud! {w} 4 months but felt like years.~"
    gerald 122 "Likewise [persistent.char_name]"
    dan 135 "Also, {w}why are you here tho?"
    gerald 123 "You know...? {w}I just miss this city, and also you buddy. "
    show Gerald 122
    extend "So I booked a ticket and I have decided that I will stay in here.~"
    dan 133 "Oh great! "
    show Dan 132
    extend "But, "
    show Dan 135
    extend "where are you staying?"
    gerald 121 "I live in the flat 3 blocks from here. {w}You can come visit your old friend sometimes.~"
    dan 133 "Oh absolutely! {w}I can come to your flat every single day if you want.~"
    gerald 122 "Hahahah...~ Fair.~ "

    gerald 123 "Hey! I know you're busy right now but, {w}may I join what are you doing right now buddy?"
    dan "Sure thing man! {w}In fact... {w}I need some sort of {bt=3}\"accompany\"{/bt}"
    show Dan 113
    gerald 122 "Hehehe... {w}Very well {bt=3}nerdy boi.~{/bt}"

    show Dan:
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