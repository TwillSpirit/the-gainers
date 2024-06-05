layeredimage Tamcin:
    fit "scale-down"

    group base:
        attribute normal default:
            "tamcin_base"
        attribute arm_up:
            "tamcin_raise_arm"

    group eyes:
        attribute idle default:
            "tamcin_expression_idle"
        attribute blink:
            "tamcin_expression_blink"
        attribute happy:
            "tamcin_expression_happy"

    group mouth:
        attribute shut default:
            "tamcin_mouth_close"
        attribute talk:
            "tamcin_mouth_open"

layeredimage Dan:
    subpixel True
    fit "scale-down"
    xanchor 0.5

    group base:
        attribute normal default:
            "dan_base"
        attribute naked:
            "dan_naked"

    group eyes:
        attribute eyes_open default:
            "dan_eyes_open"
        attribute eyes_mid_open:
            "dan_eyes_mid_open"
        attribute eyes_closed:
            "dan_eyes_close"
        attribute eyes_happy:
            "dan_eyes_happy"
        attribute eyes_surprised:
            "dan_eyes_surprised"
        attribute eyes_confused:
            "dan_eyes_confused"
        attribute eyes_confused_surprised:
            "dan_eyes_confused_surprised"

    group mouth:
        attribute mouth_smile default:
            "dan_mouth_close"
        attribute mouth_flat:
            "dan_mouth_poker"
        attribute mouth_open:
            "dan_mouth_open"
        attribute mouth_open_2:
            "dan_mouth_open_2"


layeredimage side Dan:
    fit "scale-down"
    size (1024,1024)
    xanchor 0.5
    yanchor 0.5
    yoffset 600
    xoffset -250

    group base:
        attribute normal default:
            "dan_base"
        attribute naked:
            "dan_naked"

    group eyes:
        attribute eyes_open default:
            "dan_eyes_open"
        attribute eyes_mid_open:
            "dan_eyes_mid_open"
        attribute eyes_closed:
            "dan_eyes_close"
        attribute eyes_happy:
            "dan_eyes_happy"
        attribute eyes_surprised:
            "dan_eyes_surprised"
        attribute eyes_confused:
            "dan_eyes_confused"
        attribute eyes_confused_surprised:
            "dan_eyes_confused_surprised"

    group mouth:
        attribute mouth_smile default:
            "dan_mouth_close"
        attribute mouth_flat:
            "dan_mouth_poker"
        attribute mouth_open:
            "dan_mouth_open"
        attribute mouth_open_2:
            "dan_mouth_open_2"

layeredimage Gerald:
    subpixel True
    fit "scale-down"
    xanchor 0.5

    group base:
        attribute normal default:
            "gerald_base"
        attribute naked:
            "gerald_naked"

    group eyes:
        attribute eyes_open default:
            "gerald_eyes_open"
        attribute eyes_closed:
            "gerald_eyes_closed"
        attribute eyes_happy:
            "gerald_eyes_happy"

    group mouth:
        attribute mouth_smile default:
            "gerald_mouth_smile"
        attribute mouth_open:
            "gerald_mouth_open"

layeredimage Twill:
    fit "scale-down"

    group base:
        attribute normal default:
            "twill_base"

    group eyes:
        attribute idle default:
            "twill_eyes_open"
        attribute blink:
            "twill_eyes_close"
        attribute happy:
            "twill_eyes_happy"

    group mouth:
        attribute shut default:
            "twill_mouth_close"
        attribute talk:
            "twill_mouth_open"

image Phone:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    "item handphone.png"

image Ringing:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    "item handphone_ring_1"
    pause 0.2
    "item handphone_ring_2"
    pause 0.2
    "item handphone_ring_3"
    pause 0.2
    "item handphone_ring_4"
    pause 0.2
    repeat