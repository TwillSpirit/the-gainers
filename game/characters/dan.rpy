# define sounds = ['audio/typewritting_sounds/B1.ogg', 'audio/typewritting_sounds/B2.ogg', 'audio/typewritting_sounds/B3.ogg', 'audio/typewritting_sounds/B4.ogg', 'audio/typewritting_sounds/B5.ogg']
define sounds = ['audio/typewritting_sounds/B1.ogg']

init python:
  def type_sound(event, interact=True, **kwargs):
    if not interact:
      return

    if event == "show": #if text's being written by character, spam typing sounds until the text ends
      renpy.sound.play(renpy.random.choice(sounds), loop=True, channel="sound")

    elif event == "slow_done" or event == "end":
      renpy.sound.stop(channel="sound")

define dan = Character(name="[persistent.char_name]", image="Dan", color="#a58338", callback=type_sound)
define radio = Character(name="Radio",  color="#282835")

init:
  layeredimage Dan:
    fit "scale-down"
    xanchor 0.5
    xcenter 0.5
    
    group base:
      attribute naked default:
        "characters/dan/base_01.png"
      attribute covered:
        "characters/dan/base_02.png"
      attribute naked_buff:
        "characters/dan/base_11.png"
      attribute covered_buff:
        "characters/dan/base_12.png"

    group eyes:
      attribute eyes_close:
        "characters/dan/eyes_01.png"
      attribute eyes_close_confused:
        "characters/dan/eyes_02.png"
      attribute eyes_close_angry:
        "characters/dan/eyes_03.png"
      attribute eyes_open default:
        "characters/dan/eyes_11.png"
      attribute eyes_open_confused:
        "characters/dan/eyes_12.png"
      attribute eyes_open_angry:
        "characters/dan/eyes_13.png"
      attribute eyes_surprised:
        "characters/dan/eyes_21.png"
      attribute eyes_surprised_confused:
        "characters/dan/eyes_22.png"
      attribute eyes_surprised_angry:
        "characters/dan/eyes_23.png"
      attribute eyes_happy:
        "characters/dan/eyes_31.png"
      attribute eyes_happy_confused:
        "characters/dan/eyes_32.png"
      attribute eyes_happy_angry:
        "characters/dan/eyes_33.png"
      attribute eyes_lazy:
        "characters/dan/eyes_41.png"
      attribute eyes_lazy_confused:
        "characters/dan/eyes_42.png"
      attribute eyes_lazy_angry:
        "characters/dan/eyes_43.png"

    group mouth:
      attribute mouth_frown:
        "characters/dan/mouth_01.png"
      attribute mouth_smile default:
        "characters/dan/mouth_02.png"
      attribute mouth_frown_open:
        "characters/dan/mouth_11.png"
      attribute mouth_smile_open:
        "characters/dan/mouth_12.png"
      attribute mouth_wide:
        "characters/dan/mouth_13.png"


  layeredimage side Dan:
    fit "scale-down"
    xanchor 0.5
    yanchor 0.5
    yalign 1.0
    xoffset 150
    
    group base:
      attribute naked default:
        "characters/dan/base_01.png"
      attribute covered:
        "characters/dan/base_02.png"
      attribute naked_buff:
        "characters/dan/base_11.png"
      attribute covered_buff:
        "characters/dan/base_12.png"

    group eyes:
      attribute eyes_close:
        "characters/dan/eyes_01.png"
      attribute eyes_close_confused:
        "characters/dan/eyes_02.png"
      attribute eyes_close_angry:
        "characters/dan/eyes_03.png"
      attribute eyes_open default:
        "characters/dan/eyes_11.png"
      attribute eyes_open_confused:
        "characters/dan/eyes_12.png"
      attribute eyes_open_angry:
        "characters/dan/eyes_13.png"
      attribute eyes_surprised:
        "characters/dan/eyes_21.png"
      attribute eyes_surprised_confused:
        "characters/dan/eyes_22.png"
      attribute eyes_surprised_angry:
        "characters/dan/eyes_23.png"
      attribute eyes_happy:
        "characters/dan/eyes_31.png"
      attribute eyes_happy_confused:
        "characters/dan/eyes_32.png"
      attribute eyes_happy_angry:
        "characters/dan/eyes_33.png"
      attribute eyes_lazy:
        "characters/dan/eyes_41.png"
      attribute eyes_lazy_confused:
        "characters/dan/eyes_42.png"
      attribute eyes_lazy_angry:
        "characters/dan/eyes_43.png"

    group mouth:
      attribute mouth_frown:
        "characters/dan/mouth_01.png"
      attribute mouth_smile default:
        "characters/dan/mouth_02.png"
      attribute mouth_frown_open:
        "characters/dan/mouth_11.png"
      attribute mouth_smile_open:
        "characters/dan/mouth_12.png"
      attribute mouth_wide:
        "characters/dan/mouth_13.png"