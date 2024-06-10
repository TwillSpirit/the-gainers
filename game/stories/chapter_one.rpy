default coffee_selection = "" # Store variable for the coffee selection
default pickup_phone = False # Store variable if Dan picking up the phone or not

label chapter_one:
    scene bg alarm
    $ quick_menu = True
    with Fade(1.0, 1.0, 1.0, color=color.white)

    play music tick_tock loop
    """{b}WAKEY WAKEY WAKEY YOU SLEEPY HEAD!!!{/b}

    {b}IT'S 7 O'CLOCK AND IT'S A BRAND NEW DAY!!!{/b}
    """

    stop music
    "{i}*click{/i}"

    scene bg dan_room
    with dissolve

    dan eyes_lazy"{i}yawn...{/i}"
    dan "Hngggggg... {w}Oh boi... {w}What a good sleep it was.~"

    show Dan with dissolve

    dan "... {w}......"
    dan mouth_frown"Ah... {w}right... {w}I still have a lot projects need to be done."
    dan eyes_lazy_confused "Gosh... {w}I wish I didn't sign for this project. {w}But I have to earn money to stay alive... {w}and last night was a hell of meeting and debugging session."
    
    show Dan:
        flip

    play music cinematic_suspense

    dan "..."
    dan eyes_close_confused "This flat feels empty without {b}him{/b}."
    dan "He often helped me with this kind of mess."


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
    show Dan eyes_close_confused
    with dissolve

    dan "Cut it off [persistent.char_name]. {w}The day is still young."
    dan eyes_lazy_confused mouth_smile "I'm gonna take a good warm shower now"

    hide Dan
    with easeoutright

    stop music fadeout 1.0

    scene bg shower
    with dissolve
    play music shower
    pause (3.0)

    dan "Gonna turn on this radio as well ~"
    window hide
    pause (2.0)

    window show
    radio "Tired of being called skinny? {w}SAY NO MORE!"
    radio "With this ring, {w}You can become into an absolute UNIT! {w}You will become STRONGER! {w}BIGGER! {w}And most importantly... {w}you will NOT be called skinny anymore!"
    radio "So grab these ring RIGHT NOW!!! {w}We have tested to tenth of people, {w}and everyone LOVE IT!!! {w}Better grab and sign up right now before it's too late!!"

    dan "Ring... "
    extend "that make you stronger... {w}and bigger?"
    dan "..."
    dan "What a stupid advertisement. {w}No idea of how many folks that fall into that."
    dan "But why does it sound so legit tho?"
    dan "Ah...... {w}probably a scam."

    stop music fadeout 1.0
    show screen simple_splash_screen("After a nice 30 minutes of shower session.")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)

    play music a_little_game
    
    scene bg dan_room
    hide screen simple_splash_screen
    with Dissolve(0.5)
    show Dan covered:
        center
        xzoom -1.0
        pause .5
        bounce
    with easeinright

    dan covered eyes_happy mouth_smile_open "Ah...~ {w}What a nice shower.~"
    dan "It helps to lift up my mood.~"
    dan eyes_open "Alrighty! {w}It's time to working on the project.~"
    dan eyes_open_angry "Might gonna do it in the cafe as well. {w}Gotta love the coffee they make.~"

    hide Dan mouth_smile
    with easeoutleft

    show screen simple_splash_screen("30 minutes later, Dan arrived at his favourite cafe")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)

    show bg cafe
    hide screen simple_splash_screen
    with Dissolve(0.5)
    
    show Dan covered
    with easeinleft

    dan mouth_smile_open "Finally arrived."
    dan "Time to order and do the work!~"

    dan eyes_open_confused "{i}What coffee should I order today?{/i}"

    menu:
        "Cappuccino":
            $ coffee_selection = "Cappucino"
        "Latte":
            $ coffee_selection = "latte"
        "Espresso":
            $ coffee_selection = "Espresso"

    dan eyes_open "Let's order [coffee_selection] this time.~"

    hide Dan
    with easeoutright

    show screen simple_splash_screen("Several minutes later...")
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(2.0)
    
    scene bg coding_session
    hide screen simple_splash_screen
    with Dissolve(0.5)

    $ should_show_side_image = True
    dan covered mouth_smile_open "Alright! "
    dan "My Laptop's ready, {w}My coffee's ready! "
    dan eyes_happy_angry "Let's do this!"

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
    $ should_show_side_image = True
    dan covered eyes_open_confused mouth_frown "Hmmm....? {w}Unknown number?"
    dan "I feel reluctant to answer this number..."
    dan "{i}What should I do{/i}"

    menu:
        "Answer the phone":
            $ pickup_phone = True # Set the variable pickup_phone to True
            jump answer_call
            pass
        "Don't answer the phone":
            $ pickup_phone = False # Set the variable pickup_phone to False
            jump reject_call
            pass
        
    return

label answer_call:
    hide Ringing
    with dissolve
    dan covered eyes_open_confused mouth_frown "I'll try to answer it."
    "{i}*pick up the phone*{/i}"
    dan mouth_frown_open "Greetings. {w}[persistent.char_name] speaking. {w}May I help you?"
    "???" "Hello man... {w}It's been a while since I hear your voice. {w}Please remain on your spot because I will visit you."
    
    hide Phone
    with dissolve

    dan eyes_surprised mouth_wide "WAIT-"
    dan "..."
    dan eyes_open_confused mouth_frown_open "He hung up the phone..."
    dan "Man... {w}Can I have just at least one normal day?"
    dan mouth_frown "But also... {w}why does it sounds like Gerald {w}but a bit deep?"
    dan eyes_close_confused "I'm just gonna continue my job. {w}Do not let anything distract you right now."
    window hide
    pause 1.0
    jump gerald_coming
    return

label reject_call:
    dan covered eyes_close_confused mouth_frown "Yeah no, I'm gonna reject it. {w}Probably some sort of scam or something."

    hide Phone
    hide Ringing
    with dissolve

    dan "Now let's get back to work."
    window hide
    pause 1.0
    jump gerald_coming
    return

label gerald_coming:
    stop music
    $ should_show_side_image = False
    scene black
    with Dissolve(0.1)

    pause 1.0
    
    dan "WHAAAA--!!!"
    "???" "{bt=3}Guess who...?~{/bt}"
    dan "GET OFF YOUR HAND FROM MY FACE!!!"
    "???" "{bt=3}Nope, {w}I will let my hands off whenever I want tech nerd~{/bt}"
    dan "{i}Shit... {w}who the fuck is this guy...{/i}\n{w}{sc=2}{i}Shit... {w} I'm so scared...{/i}{/sc}"
    # dan "{i}Wait a minute... {w}That voice... {w}it sounds like the guy on the phone earlier{/i}"
    window hide
    
    pause 1.0

    scene bg cafe
    with dissolve
    show Gerald covered:
        xpos 0.5
    with dissolve

    gerald eyes_happy mouth_smile_open "Surprise, tech nerd! {w}It's been a long time huh?~"

    play music cinematic_suspense
    
    show Gerald at move_pos(0.3, 0.5)
    show Dan covered eyes_surprised:
        xpos 0.7
        xzoom -1.0
        pause 0.5
        bounce
    with easeinright
    dan mouth_frown_open "NO WAY!!! {w}GERALD?!! {w}THE BROWN DAWG?!!! {w}MY BESTIE?!! {w}FOR REAL?!!"

    gerald eyes_open "The one and the only.~"

    if pickup_phone == True: # If Dan picked up the phone earlier, run this extra dialouge
        dan "So you're the one who called me with unkown number?!"
        gerald "Yeah!~ I wanna give you a surprise so I have to change my number ~"
    
    dan "Gosh! {w}you scared the {sc=2}{b}{color=#ff0000}SHIT OUT OF ME!{/color}{/b}{/sc}"
    gerald eyes_happy mouth_smile"Hehehe...~ I'm sorry [persistent.char_name]."
    dan mouth_frown "Also... "
    show Dan mouth_frown_open at move_pos(0.6, 0.2)
    extend "WHAT AN ABSOLUTE UNIT YOU ARE MATE! {w}Did you take some steroids or something? {w}Because we haven't met for 4 months and there is no way that 4 months can get you this result."
    show Dan eyes_surprised_confused mouth_frown at move_pos(0.7, 0.2)
    gerald mouth_smile_open "Hehehe... {w}Thanks for the compliment nerd. "
    show Gerald eyes_open
    extend "But no. {w}I didn't take any steroid. {w}I have my own way.~"
    show Dan eyes_surprised mouth_smile_open
    dan  "OH REALLY?! {w}What is it I wanna know!"
    gerald eyes_close mouth_smile_open "It's secret.~"
    dan eyes_open_confused mouth_frown_open "Aw... shucks..."
    gerald eyes_happy mouth_smile "Hehehe...~"
    dan eyes_open mouth_smile_open "But anyway... "
    show Dan eyes_happy
    dan "Gosh I'm so happy to see you again bud! {w}4 months but felt like years.~"
    gerald mouth_smile_open "Likewise [persistent.char_name]"
    dan eyes_open_confused "Also, {w}why are you going back to here tho? {w}Got job or something?"
    show Dan mouth_smile
    gerald eyes_open_confused "You know...? {w}I just miss this city, and also you buddy. "
    show Gerald eyes_happy
    extend "So I booked a ticket and I have decided that I will stay in here.~"
    dan eyes_happy mouth_smile_open "Oh great! "
    show Dan eyes_open
    extend "But, "
    show Dan eyes_open_confused
    extend "where are you staying?"
    gerald eyes_open mouth_smile_open "I live in the flat 3 blocks from here. {w}You can come visit your old friend sometimes.~"
    dan eyes_happy "Oh absolutely! {w}I can come to your flat every single day if you want.~"
    gerald eyes_happy mouth_smile "Hahahah...~ Fair.~ "

    gerald eyes_open_confused mouth_smile "Hey! I know you're busy right now but, {w}may I join what are you doing right now buddy? {w}I wanna be close with you again.~"
    dan eyes_happy "Sure thing man! {w}In fact... {w}I need some sort of {bt=3}\"accompany\"{/bt}"
    show Dan mouth_smile
    gerald eyes_happy mouth_smile_open "Hehehe... {w}Very well {bt=3}nerdy boi.~{/bt}"

    show Dan:
        xpos 0.75
        unflip
    
    pause 0.5
    hide Dan
    hide Gerald
    with easeoutright

    show screen simple_splash_screen("END OF CHAPTER I")
    stop music fadeout 1.0
    $ quick_menu = False
    with Fade(0.5, 1.0, 0.5, color="#fff")
    pause(5.0)
    $ persistent.chapter_one_complete = True
    hide screen simple_splash_screen

    show screen splash_screen("CHAPTER 2", "WHEN ITS ALL STARTED")
    with Fade(0.5,1.0,0.5,color=color.white)
    pause(2.0)
    jump chapter_two

    return