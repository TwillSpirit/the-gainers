label chapter_two:
  hide screen splash_screen
  play music a_little_game fadein 0.5 loop
  scene bg dan_gerald_talk
  $ quick_menu = True
  with Fade(1.0, 1.0, 1.0, color=color.white)
  
  window show
  $ should_show_side_image = True
  
  gerald covered eyes_open_confused mouth_smile_open "Say...{w} are you still doing this shitty coding project thing, nerd?"
  
  dan covered eyes_close_confused mouth_frown_open "Oh shush.{w} This is the only job I'm good at. {w}Besides, {w}I need to earn money so I don't become a homeless dude with no food."
  
  gerald eyes_close_confused "Dang, {w}chill out nerdy boi.~ {w}I was joking."
  
  window hide
  pause 2.0
  window show
  
  gerald eyes_open_confused mouth_frown "... {w}...... {w}........."
  gerald eyes_close_confused mouth_frown_open "Mh, {w}this is pretty boring, man..."
  
  dan "{i}sigh...{/i}{w} What do you expect when you're hanging out with a nerd like me?"
  
  gerald eyes_open_confused "What?! {w}No no no no! {w}I didn't say that you are boring! {w}It's the vibe in this city"
  gerald mouth_frown "It's... {w}lacking some sort of fun activity."
  
  dan "Now that you mention it. {w}You're right... {w}after the new mayor was elected, {w}everything just kinda went silent."
  
  gerald mouth_frown_open "Oh?{w} The city got a new mayor?"
  
  dan mouth_frown "Mhm."
  dan eyes_lazy_confused mouth_frown_open "I've already met with him but... {w} he's..."
  
  gerald mouth_frown  "..."
  gerald mouth_frown_open "he's...?"
  
  dan mouth_frown "He doesn't give off that cool vibe as the last one..."
  
  gerald eyes_close_confused mouth_frown "Ah... {w}that must suck then."
  
  dan eyes_close_confused mouth_frown "You tell me."

  window hide
  pause 2.0
  window show

  dan eyes_lazy_angry mouth_frown "Why the hell won't this freaking code work?!"
  
  gerald eyes_open_confused mouth_frown "Hmm...{w}\nCan I see it?"
  
  dan eyes_close_confused  "Sure..."

  window hide
  pause 3.0
  window show

  gerald eyes_open mouth_frown_open "Ah..!\n{w}You forgot to write 'semicolon' in this line!"
  
  dan eyes_surprised mouth_frown_open "WAIT WHA-?"

  window hide
  pause 1.0
  window show

  scene bg dan_gerald_talk with hpunch
  
  dan covered eyes_surprised_angry mouth_frown_open "OH FOR FUCKS SAKE!!! YOU'RE RIGHT!!"
  
  gerald covered eyes_open_confused mouth_smile_open "Hey hey hey!{w} Chill out [persistent.char_name]. {w}You're just not careful enough."
  
  dan "..."
  dan eyes_close_confused mouth_frown "Damn it...{w} it's all because of the stupid semicolon..."
  dan mouth_frown_open "You're so good at spotting errors..."
  
  gerald "Hey!{w} You taught me how to code and do all the basic troubleshooting."
  
  dan mouth_frown "That's why I'm feeling so embarrassed..."

  gerald "Don't be like that bestie.~"

  window hide
  pause 1.0
  window show

  gerald "May I know what is this project for tho?"
  
  dan "Oh... {w}A company nearby wants me to make them a website..."
  
  gerald eyes_open "Oh I see.~"
  gerald "I can help you with the design if you want!"
  
  dan eyes_open mouth_frown_open "Oh no no no, {w}It's fine Gerald\n{w}They already gave me the mockup, so now I just need transform it into an actual website."
  
  gerald "Oh I see I see"

  window hide
  pause 3.0
  window show

  dan eyes_close mouth_smile_open "And... done~!"
  dan eyes_close_confused "Man, that was a whole lot of stuff"
  
  gerald eyes_open mouth_smile_open "So you're finally finished with this project, right?"
  
  dan eyes_happy_confused "Yeah, {w}I just need to host it later and send it to the company."
  
  gerald eyes_happy "AYYY!!! LET'S GOOO!!"

  dan eyes_open "Oh yeah I forgot!{w} Do you wanna eat something Gerald?"
  
  gerald  "No no no it's fine~ {w}I already had something in the way here~"
  
  dan eyes_happy "Alright alright~"
  dan eyes_open "I think I'm gonna head back home now."
  
  gerald eyes_open "Sure thing~"

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

  dan eyes_happy mouth_smile_open "Hey man, thanks a ton for accompanying me and helping me with this project and the error.~"
  
  gerald eyes_happy mouth_smile_open "Ay~ {w}no problem nerd boi.~\n{w}I'm glad that I was able to help you again."
  
  dan eyes_open mouth_smile_open "Say Gerald.{w} Do you have anything in mind of what you're gonna do today, after I leave?"
  
  gerald eyes_open mouth_smile_open "Oh!{w} Well actually...{w} I wanna invite you to my flat tonight!.\n"
  
  show Gerald eyes_happy
  
  extend "For a \"Panties Sleepover\" like we used to do before~."
  
  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce
    
  dan "{i}gasp!{/i} {w}You still wanna do that?!"
  
  gerald "I just miss our good ol' quality time, nerd boi.{w} So... {w}{bt=2}wanna come and join...?~{/bt}"
  
  show Dan eyes_happy_angry mouth_smile_open:
    xpos 0.35
    bounce
    
  dan "FUCK YEAH MAN!!!{w} I'M SO DOWN FOR THAT!!!"
  
  gerald mouth_smile "Hehehe...{w} I knew you would join for that shit.~"
  gerald mouth_smile_open "Meet me at my flat, room 133, got that [persistent.char_name]?"
  
  dan eyes_open_angry "YOU BET!"

  window hide

  scene black
  with Dissolve(2.0)
  pause 3.0

  scene bg corridor
  with Dissolve(2.0)
  pause 0.5

  show Dan covered eyes_happy:
    xpos 0.5
  with easeinleft

  dan eyes_happy_angry mouth_smile_open "{bt=3}Hey Gerald...~~{/bt}\n{w}{bt=3}Your nerdy boi has come for the sleepover...~{/bt}"

  gerald "{bt=3}Come in, tech nerd~~{/bt}{w}\n{bt=3}The door is unlocked~{/bt}"

  dan "{bt=3}Coming in~!{/bt}"

  hide Dan
  with easeoutright

  scene bg gerald_room_night
  with Fade(1.0,0.0,1.0)

  pause 1.0

  show Dan covered eyes_happy:
    xpos 0.35
  with easeinleft


  dan eyes_open_confused mouth_smile "Uhm... "
  dan mouth_smile_open "Gerald? Where are you?"

  gerald "In the closet,{w} please wait a sec."
  dan "Ohh okay~"

  dan mouth_smile "{i}Damn, {w}his room is way tidier than mine. {w}Guess the tidy doggo never changes...~{/i}"
  dan mouth_smile "{i}This room's layout is almost the same as mine. {/i}"
  
  show Dan eyes_happy_confused
  
  extend "What a coincidence~"

  gerald "I'm about to come out~. {w}Ready~?"

  dan eyes_happy mouth_smile_open "Always am~"

  stop music fadeout 1.0
  pause 1.0

  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce

  dan "WOA--"
  dan "GE- {w}GERALD?!!"

  show Gerald:
    xpos 0.65
    xzoom -1.0
  with easeinright

  play music cinematic_suspense fadein 0.5 loop

  gerald eyes_happy mouth_smile_open "Hey hey~\n{w}Like what you see?~"

  dan "So this is what you looks like... {w}without the clothes...?"
  dan "Dude... {w}{sc=3}YOU'RE A FUCKING BEAST!!!{/sc}"

  gerald eyes_close "I am indeed ~"

  show Gerald eyes_open mouth_smile
  
  show Dan eyes_surprised mouth_frown_open:
    xpos 0.35
    bounce

  dan mouth_wide "W-WAIT! {w}I'M NOT READY YET!!!"

  show Gerald eyes_open_confused

  hide Dan
  with easeoutleft

  pause 1.0

  show Dan eyes_surprised:
    xpos 0.35
  with easeinleft

  dan mouth_smile "Th- {w=0.5}There we go..."

  show Dan:
    shaking(0.35)

  dan eyes_surprised_confused "{i}Oh fuck...{w}\nI forgot that he's fucking jacked now.{w}\nBack then when he was still normal, I had no problem with it, but now...{w}\nMh... Why did I sign up for this crap...?{w}\nI can't turn back time now...{/i}"

  gerald eyes_open_confused mouth_smile_open "You alright nerd? {w}You're shaking..."

  show Gerald mouth_smile

  show Dan eyes_surprised_confused mouth_smile_open:
    xpos 0.35
    bounce
    shaking(0.35)

  dan "Ah..!{w} Yes..!{w} I'm okay.. {w}I'm alright.. {w}I'm fine... It's all good..."

  gerald mouth_smile_open "Oh [persistent.char_name]...~\n{w}I know what you're thinking right now...~{w}\nYou wanna test and see if this real or not, right...?~"

  show Dan eyes_surprised_confused mouth_frown_open:
    xpos 0.35
    bounce
  
  dan "WHAT?! "
  show Dan:
    xpos 0.35
    bounce
  extend "NO NO NO NO... I DON-{nw}"

  gerald eyes_close_confused mouth_smile_open "Come on..~ {w}You can't lie to your bestie y'know.~ {w}That's kinda rude"

  dan mouth_frown "{i}Hngggg...{/i}"  
  dan eyes_close_angry mouth_wide "FINE!!! {w}CAN I TOUCH YOUR HUGE BODY? "

  show Dan eyes_open_angry

  extend "I have never seen a jacked guy in this city and so close, alright?!"

  gerald eyes_close_confused mouth_smile_open "Geez... {w}chill out nerd...~"
  gerald eyes_happy "Heh, yes, yes you can...~ {w}Please check it out yourself ~"

  window hide
  scene bg pecs
  with Dissolve(1.0)

  pause 1.0
  $ should_show_side_image = True

  window show
  dan eyes_surprised mouth_frown "Oh fuck...\n{w}They are so soft yet so firm..."

  gerald eyes_happy "I know right?"

  dan eyes_surprised_confused mouth_frown_open "What is this muscle called?"

  gerald "They are called pectorals.~"

  dan "Pectorals?"

  gerald "Eyup! {w}But the internet often called it as a moobs"

  dan "Moobs?"

  gerald "Eyup! {w}It stands for Man Boobs"

  dan eyes_surprised mouth_wide "THE FUCK?!!"

  gerald eyes_close_confused "I know it's weird right? {w}The internet is quite... {i}'internetsting'{/i}."

  dan mouth_frown_open "Tell me more about muscles!"

  gerald mouth_smile_open "Whoa...~ {w}Someone is interested eh?~"

  dan eyes_close_angry "Just fucking tell me already!"

  gerald mouth_smile_open "Geez...~ {w}Chill out~"
  gerald eyes_open "Alright so...~"
  gerald "The ones you're touching are called pectorals or pecs for short ~\n{w}The shoulders are called Deltoids ~\n{w}You've got the classic abs right below the pecs ~\n{w}The muscles that look like wings between my back and front are called Lats ~\n{w}The one that connected between my abs and lats are called obliques\n{w}Aaand on my upper arms you have the classic biceps and triceps ~"

  dan eyes_surprised "Whoa... {w}That's a lot of muscles."

  gerald eyes_happy "Definitely ~"

  scene bg gerald_room_night
  show Dan eyes_open mouth_smile:
    xpos 0.35
  show Gerald:
    xpos 0.65
    xzoom -1.0
  with Dissolve(1.0)
  $ should_show_side_image = False
  
  dan eyes_happy_confused "Okay...~ {w}now that you let me do that I feel more relieved..."
  
  gerald eyes_happy mouth_smile_open "Hehehe! {w}Happy to help you again!"

  show Gerald eyes_open:
    xpos 0.65
    xzoom -1.0
    bounce

  gerald "Oh right! {w}I have cooked some food for both of us!"

  dan eyes_surprised mouth_frown_open "HUH?"

  gerald eyes_happy mouth_smile "Mhm! {w}Your favourite classic fried rice with a lotta eggs, {w}and 2 whole chickens ~"

  ### New Line
  dan "Gerald, that's a lot!"

  gerald "Nah, {w=0.5}I need to feed my bestie because I know you can eat a lot ~\n{w}Because I heard from other folks that you can eat entire turkey alone!\n{w}So I wanna see how do you handle it ~"
  ### End New Line

  dan eyes_happy_confused mouth_smile_open "Man I feel so honored to get all of that from you... {w}I don't think I deserve this"

  gerald eyes_happy mouth_smile_open "Oh don't be like that, nerd boy!"
  gerald eyes_open "Shall we eat now? {w}We can do a story trade as well like the old days ~"

  dan eyes_happy mouth_smile_open "Absolutely! I'm so ready to get myself bloated~"

  gerald eyes_happy_confused "Wow... {w}Calm down ~"
  gerald eyes_happy "Alright! {w}Come here nerd ~"

  window hide

  hide Gerald
  hide Dan
  show screen narator_screen('Dan could\'t resist his appetite as soon as he sees the foods', mode="dark", background_color="#000000") # New Line
  with Fade(1.0, 0.0, 1.0)
  pause 3.0
  scene black
  hide screen narator_screen
  with Fade(1.0, 0.0, 1.0)
  
  # Start New Line

  gerald "WAIT!{w} THAT'S A LOT!!!"

  dan "I can handle it ~\n{w}Don't you worry ~"

  scene bg dinner
  with Fade(1.0, 0.0, 1.0)

  gerald "HOLY SHIT!!!{w} YOU POLISHED IT OFF!!!"

  dan "Heh ~\n{bt=2}This is nothing ~{/bt}"

  gerald "Dude... {w=0.5} YOUR BELLY! {w}IT'S FUCKING HUGE!"

  dan "{bt=2}Hehehe ~{/bt}"
  dan "You have never see me like this, haven't you?~"

  gerald "I know you can eat a lot... {w}BUT I DIDN'T KNOW YOU COULD EAT THIS A LOT ANF WOULD BECOME LIKE THIS"

  dan "{bt=2}Heh ~{/bt}"

  gerald "[persistent.char_name]... {w} I'm geniunely worried right now... {w}Are you okay... ?"

  dan "Yeah I'm fine ~\n{w}It was a delicious meal I ever had in months ~\n{w}The fact that it was made by you make it more special ~"

  gerald "Uhmm... {w=0.5}Thanks for the compliment nerd, but... {w}are you really okay...?"

  dan "I'm okay Gerald, don't worry ~\n{w}I will not explode I promise ~"
  dan "But I might need your help because my legs couldn't hold my weight haha ~"

  gerald "Sure sure! {w}Anything that makes you comfortable!"

  dan "{i}For the first time I saw his face really worried about me.\n{w}Maybe I did it way too much.\n{w}But, he really cares about me.{/i}"

  show bg night_talk
  with Fade(1.0, 0.0, 1.0)

  pause 1.0

  dan "Hey Gerald, {w}sorry for making you worry about me."

  gerald "It's okay! {w}I'm just {w=0.5}not used to see you like this."

  dan "Yeah I shouldn't do it that much, {w}But I got carried away because it was so good ~"

  gerald "Well... {w}I'm glad you like it nerd ~"

  dan "Yeah... ~\n{w}{i}*burp*{/i} Oh, I'm so sorry."

  gerald "Don't think about it! {w}It's a normal reaction come on."

  dan "Hehe, fine fine ~"

  window hide
  pause 2.0
  window show
  
  gerald "..."
  gerald "Hey Dan."
  
  dan "Yeah?"

  gerald "Wanna do story trade?"

  dan "Uh..."

  window hide

  menu:
    "Do a story trade":
      jump story_trade
    "Keep your story secret":
      pass
    

  "More dialouges will be add very soon! Just cope with what we have here right now :3"

  scene black
  with Dissolve(1.0)
  return

label story_trade:
  dan "Sure Gerald! {w}Let's hear your first ~"

  gerald "Okay! {w}So... I bet you still wonder do I got this muscles really fast."

  dan "I do actually"

  gerald "Okay, {w}I'm gonna tell you now because I can't shut my mouth about this anymore"
  gerald "So in the radio, {w}I heard about a ring that can make you stronger, bigger, and muscular"
  gerald "At first I didn't believe it, {w}because it sounds like a scam. {w}But I'm really curious so I bought one. {w}It was cheap tho, {w}just cost 5 dollars."
  gerald "Anf then I went to my house over there. {w}As soon as I put the ring on my finger, {w}I felt the big energy just rushing into my blood. {w}My heart beat so fast"
  gerald "It was a bit painful, {w}but I can clearly see my muscles start growing bigger {w=0.5}and bigger"
  gerald "and when it stopped, {w}I felt really exhausted and basically faint"
  gerald "and when I woke up, {w}I've turned into a muscle beast like you witnessing right now"

  dan "Wait- {w}So you're telling me that ring thing is real?!"

  gerald "Hundred percent is real dude!"
  gerald "Even when I put it off the ring, {w}my body size just remain like this"

  dan "Sounds like a black magic"

  gerald "I know right?!"
  gerald "I still have the ring if you want to use it!"

  dan "What! No!"

  gerald "Why?"

  dan "You said it was a painful process, {w}and you know I hate if the word pain is included."

  gerald "Awh.. okay okay"
  gerald "I mean fair tho,{w} right now you have the big belly, {w}it just could make it even worse."

  dan "There you go! You know it ~"

  pause 2.0

  dan "{i}*yawn*{/i}{w} I'm sorry Gerald, but your nerd boi is quite sleepy..."

  gerald "Oh? {w}Alright! {w}It's a bit late for you yeah?"

  dan "Mhm"

  gerald "Rest in my bed nerd, I can sleep on the couch over there. {w}Don't you worry about me okay?"

  dan "Bro... {w}Thanks for all of you did"

  gerald "Anything for bestie"