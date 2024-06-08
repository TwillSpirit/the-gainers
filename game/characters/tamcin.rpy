define tamcin = Character(name="Tamcin", image="Tamcin", color="#282b35")

layeredimage Tamcin:
  fit "scale-down"

  group base:
    attribute normal default:
      "tamcin_base"
    attribute arm_up:
      "tamcin_raise_arm"

  group eyes:
    attribute eyes_open default:
      "tamcin_expression_idle"
    attribute eyes_close:
      "tamcin_expression_blink"
    attribute eyes_happy:
      "tamcin_expression_happy"

  group mouth:
    attribute mouth_smile default:
      "tamcin_mouth_close"
    attribute mouth_smile_open:
      "tamcin_mouth_open"