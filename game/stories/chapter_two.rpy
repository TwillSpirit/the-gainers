label chapter_two:
  hide screen splash_screen
  play music a_little_game fadein 0.5 loop
  scene bg dan_gerald_talk
  $ quick_menu = True
  with Fade(1.0, 1.0, 1.0, color=color.white)
  
  window show
  $ should_show_side_image = True
  
  gerald covered eyes_open_confused mouth_open "Say...{w} Are you still doing this shitty coding project thing nerd?"
  
  dan covered eyes_close_confused mouth_frown_open "Oh shut up.{w} This is the only job which I'm good at it. {w}Besides, {w}I need to earn money so I don't become homeless and starving."
  
  gerald eyes_close_confused "Dang, {w} chill out nerdy boi.~ {w}I was joking around with you."
  
  window hide
  pause 2.0
  window show
  
  gerald eyes_open_confused mouth_frown "... {w}...... {w}........."
  
  gerald eyes_close_confused mouth_frown_open "Dang, {w}this is pretty boring man..."
  
  dan "{i}sigh...{/i}{w} What do you expect when you're hangout from a nerd like me man?"
  
  gerald eyes_open_confused "What?! {w}No no no no! {w}I didn't mean you! {w}But the vibe in this city"
  
  gerald mouth_frown "It's... {w}lacking of fun activity."
  
  dan "Now that you mention it. {w}It is actually... {w}after the new mayor elected, {w}everything just kinda stop."
  
  gerald mouth_frown_open "Oh?{w} The city got new mayor?"
  
  dan mouth_frown "Mhm."
  
  dan eyes_lazy_confused mouth_frown_open "Don't get me wrong, {w}But I've already met with him...{w} and..."
  
  gerald mouth_frown  "..."
  
  gerald mouth_frown_open "and...?"
  
  dan mouth_frown "He doesn't pass the vibe like the old one..."
  
  gerald eyes_close_confused mouth_frown "Ah... {w}must be suck right?"
  
  dan eyes_close_confused mouth_frown "You tell me."

  window hide
  pause 2.0
  window show

  dan eyes_lazy_angry mouth_frown "Why the hell this code won't works?!"
  
  gerald eyes_open_confused mouth_frown "Hmm...{w}\nCan I see it?"
  
  dan eyes_close_confused  "Sure..."

  window hide
  pause 3.0
  window show

  gerald eyes_open mouth_frown_open "Ah..!\n{w}You forgot to put semicolon in this line!"
  
  dan eyes_surprised mouth_frown_open "WAIT WHA-?"

  window hide
  pause 1.0
  window show

  scene bg dan_gerald_talk with hpunch
  
  dan covered eyes_surprised_angry mouth_frown_open "OH FOR FUCK SAKE!!! IT WAS!!"
  
  gerald covered eyes_open_confused mouth_smile_open "Hey hey hey!{w} Chill out [persistent.char_name]. {w}You're just not careful enough."
  
  dan "..."
  
  dan eyes_close_confused mouth_frown "Damn it...{w} it just because of the stupid semicolon..."
  
  dan mouth_frown_open "You're so good at spotting error..."
  
  gerald "Hey!{w} You teached me how to code and do basic troubleshooting."
  
  dan mouth_frown "Now I feel so emmbarased..."

  gerald "Don't be like that bestie.~"

  window hide
  pause 1.0
  window show

  gerald "May I know what is this project for tho?"
  
  dan "Oh... {w}A company nearby wants me to build them a website..."
  
  gerald eyes_open "Oh I see.~"
  
  gerald "I can help you with the design if you want!"
  
  dan eyes_open mouth_frown_open "Oh no no no, {w}It's fine Gerald\n{w}They already hand me the mockup and I just need transform it into an actual website."
  
  gerald "Oh I see I see"

  window hide
  pause 3.0
  window show

  dan eyes_close mouth_smile_open "And... done...~"
  
  dan eyes_close_confused "Man that's a hell of stuff"
  
  gerald eyes_open mouth_smile_open "So you're finished with this project right now?"
  
  dan eyes_happy_confused "Yeah, {w}just gonna host it later and will give it to the company."
  
  gerald eyes_happy "AYE!!! LET'S GOOO!!"

  dan eyes_open "Oh yeah I forgot!{w} Do you wanna eat something Gerald?"
  
  gerald  "No no no it's fine~ {w}I'm already full~"
  
  dan eyes_happy "Fine fine ~"

  dan eyes_open "I think I'm gonna head out to home now."
  
  gerald eyes_open "Alright~"

  scene bg cafe
  with Dissolve(1.0)

  $ should_show_side_image = False

  show Dan covered:
    xpos 0.35
    xzoom -1.0
  show Gerald covered:
    xpos 0.65
    xzoom -1.0
  with easeinright

  pause 0.5

  show Dan:
    xpos 0.35
    unflip

  dan eyes_happy mouth_smile_open "Man, thanks a ton for you to accompany me with this project and help me a bit with the error.~"
  
  gerald eyes_happy mouth_smile_open "Ay~ {w}no problem nerd boi.~\n{w}I'm glad that I can help you again."
  
  dan eyes_open mouth_smile_open "Say Gerald.{w} Got something in your mind of what are you gonna do for today or later before I'm leaving?"
  
  gerald eyes_open mouth_smile_open "Oh!{w} Actually...{w} I wanna invite you into my flat tonight!.\n"
  
  show Gerald eyes_happy
  
  extend "Into a \"Panties Sleepover\" like we used to do before."
  
  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce
    
  dan "{i}gasp!{/i} {w}You still wanna do that?!"
  
  gerald "I just miss our good quality time nerd boi.{w} So... {w} {bt=2}wanna come and join...~{/bt}"
  
  show Dan eyes_happy_angry mouth_smile_open:
    xpos 0.35
    bounce
    
  dan "FUCK YEAH MAN!!!{w} I'M DOWN FOR THAT!!!"
  
  gerald mouth_smile "Hehehe...{w} I knew you would join for that shit.~"
  
  gerald mouth_smile_open "Meet me at my flat room 133, aight [persistent.char_name]?"
  
  dan eyes_open_angry "BET!"

  window hide

  # gerald "Alright!{w} I'm gonna headed out first. {w}See ya there nerd!"

  # dan eyes_happy "See ya there Gerald!"

  # hide Gerald
  # with easeoutleft

  # pause 2.0

  # show Dan eyes_surprised mouth_frown_open:
  #   ease xcenter 0.5
  #   bounce

  # dan "WAIT!!{w} I FORGOT THAT NOW HE IS SO JACKED!!!"

  # dan eyes_surprised_confused "OH FUCK, OH FUCK, OH FUCK, OH FUCK\n{w}WHY DID I SIGN FOR THIS?!!!"

  scene black
  with Dissolve(2.0)
  pause 3.0

  scene bg corridor
  with Dissolve(2.0)
  pause 0.5

  show Dan covered eyes_happy:
    xpos 0.5
  with easeinleft

  dan eyes_happy_angry mouth_smile_open "{bt=3}YOooooo... Gerald...~~{/bt}\n{w}{bt=3}Your nerdy boi has come for a sleepover...~~{/bt}"

  gerald "{bt=3}Come in Nerdy Boi~~{/bt}{w}\n{bt=3}The door is unlocked~~{/bt}"

  dan "{bt=3}Coming in~~{/bt}"

  hide Dan
  with easeoutright

  scene bg gerald_room_night
  with Fade(1.0,0.0,1.0)

  pause 1.0

  show Dan covered eyes_happy:
    xpos 0.35
  with easeinleft


  dan eyes_open_confused mouth_smile "Uhmmm... "
  dan mouth_smile_open "Where are you Gerald?"

  gerald "In the closet,{w} please wait a bit."
  dan "Oh okay~"

  dan mouth_smile "{i}Dang, {w}his room is better than mine. {w}He never changed being the tidy dog...~{/i}"
  
  dan mouth_smile "{i}But this room's layout is almost the same as mine. {/i}"
  
  show Dan eyes_happy_confused
  
  extend "What a coincidence~"

  gerald "I'm about to come out, {w}You ready?"

  dan eyes_happy mouth_smile_open "Always am~"

  stop music fadeout 1.0
  pause 1.0

  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce

  dan "WHAA--"

  dan "GE- {w}GERALD?!!"

  show Gerald:
    xpos 0.65
    xzoom -1.0
  with easeinright

  play music cinematic_suspense fadein 0.5 loop

  gerald eyes_happy mouth_smile_open "Hey hey~\n{w}Like what you see huh?~"

  dan "So this is... {w}what you looks like... {w}without the clothes...?"

  dan "Man... {w}{sc=3}YOU ARE A FUCKING BEAST!!!{/sc}"

  gerald eyes_close "I am indeed ~"

  show Gerald eyes_open mouth_smile
  
  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce

  dan "WAIT! {w}I'M NOT READY YET!!!"

  show Gerald eyes_open_confused

  hide Dan
  with easeoutleft

  pause 1.0

  show Dan eyes_surprised:
    xpos 0.35
  with easeinleft

  dan mouth_smile "There we go..."

  dan eyes_surprised_confused "{i}Oh fuck...{w}\nI forgot that he's so fucking jacked now.{w}\nBack then he's still normal and I have no problem with it...{w}\nWhy did I sign up for this crap...?{w}\nI can't rollback the time now...{/i}"

  gerald eyes_open_confused mouth_smile_open "You okay nerd?"

  show Gerald mouth_smile

  show Dan eyes_surprised_confused mouth_smile_open:
    xpos 0.35
    bounce

  dan "Ah..!{w} Yes..!{w} I'm okay.. {w}I'm alright.. {w}I'm fine.."

  gerald mouth_smile_open "Oh [persistent.char_name]...~\n{w}I know what are you thinking right now...~{w}\nYou wanna test it if this real or not right...~"

  show Dan eyes_surprised_confused mouth_frown_open:
    xpos 0.35
    bounce
  
  dan "WHAT?! "
  show Dan:
    xpos 0.35
    bounce
  extend "NO NO NO NO... I DON-{nw}"

  gerald eyes_close_confused mouth_smile_open "Come on..~ {w}You can't lie to your bestie y'know.~ {w} That's rude"

  dan mouth_frown "{i}Hngggg...{/i}"
  
  dan eyes_close_angry mouth_frown_open "FINE!!! {w}CAN I TOUCH IT? "

  show Dan eyes_open_angry

  extend "I have never seen jacked guy in this city and this close alright?!"

  gerald eyes_close_confused mouth_smile_open "Geez... {w}chill out nerd...~"

  gerald eyes_happy "Yes, you can...~ {w}Please check it by yourself"

  window hide
  scene bg pecs
  with Dissolve(1.0)

  pause 1.0
  $ should_show_side_image = True

  window show
  dan eyes_surprised mouth_frown "Oh fuck...\n{w}This is so soft yet so firm..."

  gerald eyes_happy "I know right?"

  dan eyes_surprised_confused mouth_frown_open "What is this muscle part called?"

  gerald "They are called pectorals.~"

  dan "Pectorals?"

  gerald "Eyup! {w}But the internet often called it as a moobs"

  dan "Moobs?"

  gerald "Eyup! {w}It stands for Man Boobs"

  dan eyes_surprised "WHAT THE FUCK?!!"

  gerald eyes_close_confused "I know it's weird right? {w}but the internet just {i}interneting{/i}."

  dan "Tell me about more muscle part!"

  gerald mouth_smile_open "Whoa...~ {w}Someone is interested eh?~"

  dan eyes_close_angry "Just fucking tell me already!"

  gerald mouth_smile_open "Geez...~ {w}Chill out~"

  gerald eyes_open "Okay so...~"

  gerald "The one you're touching are called pectorals or pecs for short ~\n{w}The shoulders are called Deltoids ~\n{w}And you got the classic abs ~\n{w}Between my back and front that looks like wings is called Lats ~\n{w}The one that connected between my abs and lats are called obliques\n{w}In my upper arms you got the classic biceps and triceps ~"

  dan eyes_surprised "Whoa... {w}That's a lot of muscles."

  gerald eyes_happy "Absolutely is ~"

  scene bg gerald_room_night
  show Dan eyes_open mouth_smile:
    xpos 0.35
  show Gerald:
    xpos 0.65
    xzoom -1.0
  with Dissolve(1.0)
  $ should_show_side_image = False
  
  dan eyes_happy_confused "Okay...~ {w}now my mind is relieved after you let me do that"
  
  gerald eyes_happy mouth_smile_open "Hehehe! {w}Glad to help you again!"

  show Gerald eyes_open:
    xpos 0.65
    xzoom -1.0
    bounce

  gerald "Oh right! {w}I have cooked some food for both of us!"

  dan eyes_surprised mouth_frown_open "WHAT?"

  gerald eyes_happy mouth_smile "Mhm!"

  dan eyes_happy_confused mouth_smile_open "Man I feel so honoured to get all of that from you..."

  gerald eyes_happy mouth_smile_open "Oh don't be like that nerd!"

  gerald eyes_open "Shall we eat now?"

  dan eyes_happy mouth_smile_open "Absolutely! I'm ready to bloated myself~"

  scene black
  with Fade(1.0, 0.0, 1.0)

  pause 1.0

  "More dialouges will be add very soon!"

  scene black
  with Dissolve(1.0)
  return