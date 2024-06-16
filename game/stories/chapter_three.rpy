label chapter_three:
  window hide
  # hide screen splash_screen
  # with Fade(1.0, 0.0, 1.0)
  show screen dream_thought_screen('GROW...')
  with Fade(1.0, 0.0, 1.0)
  $ renpy.pause()

  show screen dream_thought_screen('GROW YOURSELF...')
  with Fade(1.0, 0.0, 1.0)
  $ renpy.pause()

  hide screen dream_thought_screen
  show screen dream_thought_screen('GROW BIGGER...', 72)
  with Fade(1.0, 0.0, 1.0)
  $ renpy.pause()
  
  hide screen dream_thought_screen
  show screen dream_thought_screen('GROW STRONGER...', 120)
  with Fade(1.0, 0.0, 1.0)
  $ renpy.pause()


  hide screen dream_thought_screen
  show bg gerald_room_day
  with Fade(2.0, 0.0, 2.0)

  $ quick_menu = True
  dan "Hnggggggh..."
  dan "..."
  dan "What was...{w} that dream...?"
  dan "The only words that I can remember is grow, {w}bigger, {w}stronger..."
  dan "What is that even mean...?"
  dan "I have no idea..."

  window hide
  pause (1.0)
  window show

  dan "Gerald's still sleeping..."
  dan "Should not disturb him... {w}even tho it's already morning..."

  window hide
  pause (1.0)
  window show

  dan "..."
  dan "Why is my body feels heavy...?"

  pause 1.0

  dan "I'm gonna wash my face first"

  "[persistent.char_name] went to Gerald's bathroom just to find out that..."
  "He's changed..."

  scene bg gerald_room_day with hpunch
  dan "AAAAAAAAAAAAAAAAAAAAAAA...!!!!!"
  dan "WHAT THE FUCK!!!"
  dan "WHAT THE FUCK IS THIS!!!"

  scene bg dan_shock
  with Fade(1.0, 0.0, 1.0)

  pause 1.0
  dan "AM I..."
  dan "AM I STILL DREAMING...?!!"
  dan "IS THIS..."
  dan "IS THIS ME?!!"
  dan "IS IT BECAUSE OF THE RING?!"
  if persistent.put_ring == False:
    dan "BUT HOW?!"
    dan "I HAVEN'T PUT IT IN MY FINGER!!"

  "Gerald heard [persistent.char_name] and quickly rush himself into the bathroom."

  gerald "[persistent.char_name.upper()]!!! {w}WHAT'S THE MATTER!!!"

  dan "AH GERALD!!!"

  gerald "Oh my..."
  gerald "[persistent.char_name]... {w}You're HUGE!!"

  dan "GERALD PLEASE TELL ME I'M STILL DREAMING"

  gerald "I wish I could..."
  gerald "But damn look at you bestie ~"
  gerald "You're huge and looks stong as well ~"

  dan "GERALD!!!"

  gerald "Okay okay I'm sorry! {w}Chill out now bestie"

  dan "HOW AM I SUPPOSED TO BE CHILL OUT LIKE THIS GERALD?!!"

  gerald "Come here come here ~"

  scene black
  with Fade(0.5, 0.0, 0.5)

  "Gerald guided [persistent.char_name] out from the bathroom and calm him down"

  dan "Gerald... what's happening to me?!"
  gerald "I don't know man"
  dan "Is it because of that ring?!"
  gerald "Probably?"

  if persistent.put_ring == False:
    dan "But HOW?!"
    dan "I HAVEN'T PUT IT IN MY FINGER!!"
    gerald "That I have no idea at all"

  "Gerald hugged [persistent.char_name] and told him to accept it"
  "Slowy but sure, Gerald calm him down"

  scene bg gerald_room_day
  show Dan naked_buff eyes_open_confused look_s_straight mouth_frown:
    xpos 0.3
  show Gerald naked eyes_open_confused mouth_smile:
    xzoom -1.0
    xpos 0.7
  with Dissolve(1.0)

  dan mouth_frown_open "I just don't get it Gerald..."
  gerald mouth_smile_open "Well me neither..."

  gerald eyes_open "But look at you ~"
  show Gerald at move_pos(0.5)
  show Dan at move_pos(0.2, 2.0)
  gerald "You a re a beast ~"

  "Gerald put his hand onto his massive pecs and give it a nice massage"

  dan "GERALD!!!"

  gerald eyes_close "Shhhh... let me feel it ~"

  dan "{i}Wait...{/i}"
  dan "{i}Why is it feels so good...?{/i}"
  dan "{i}Is this what he felt when I touched him...?{/i}"

  gerald eyes_open "What do you feel bestie?"

  dan "It feels... "
  show Dan mouth_frown
  extend "good...?"
  gerald eyes_happy "There you go...~"
  gerald eyes_open "Try do it by yourself"

  dan "{i}I do what Gerald told me to do...{/i}"
  dan "{i}and it feels amazing...{/i}"

  dan eyes_open "Wow~"
  dan look_s_down "It feels good, what the fuck?"

  gerald eyes_happy "Right?~"

  dan look_down "This pecs ~"
  dan "This abs ~"
  dan "This arm ~"
  dan "and this is... still me"

  gerald "Eyup!"
  gerald eyes_open "Feels good right being a beast?~"

  dan "You're right"
  dan look_straight "It feels..."
  show Dan mouth_frown_open
  extend " AMAZING!!!"

  gerald eyes_happy "You know it!!!"

  show Gerald eyes_open_confused
  dan look_s_straight mouth_wide "WAIT!!!"
  dan "MY CLOTHES!!!"

  hide Dan
  show Gerald eyes_open_confused:
    unflip()
  with easeoutright
  
  pause 2.0

  dan "OH FUCK!!"
  dan "IT DOESN'T FIT ANYMORE"

  return