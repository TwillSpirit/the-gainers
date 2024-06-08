label chapter_two:
  hide screen splash_screen
  play music a_little_game fadein 0.5 volume 1.0 loop
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
  gerald "Oh no it's fine!{w} I'm still full."
  dan eyes_happy "Fine fine ~"

  scene bg cafe
  with dissolve

  $ should_show_side_image = False

  show Dan covered:
    xpos 0.35
    xzoom -1.0
  show Gerald covered:
    xpos 0.65
    xzoom -1.0
  with easeinright

  show Dan:
    xpos 0.35
    unflip

  dan mouth_smile_open "So Gerald.{w} Got something in your mind of what are you gonna do for today or later before I'm leaving?"
  gerald mouth_smile_open "Oh!{w} Actually...{w} I wanna invite you into my flat tonight!.\n"
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

  scene black
  with Dissolve(2.0)
  pause 3.0

  "More dialouge will be add later on...~"

  return