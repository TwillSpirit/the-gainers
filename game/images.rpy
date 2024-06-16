layeredimage Twill:
    fit "scale-down"

    group base:
        attribute normal default:
            "twill_base"

    group eyes:
        attribute eyes_open default:
            "twill_eyes_open"
        attribute eyes_close:
            "twill_eyes_close"
        attribute eyes_happy:
            "twill_eyes_happy"

    group mouth:
        attribute mouth_smile default:
            "twill_mouth_close"
        attribute mouth_open:
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

# Image for scene
image bg alarm:
    "scene/bg alarm.png"
image bg beach:
    "scene/bg beach.png"
image bg city:
    "scene/bg city.png"
image bg coding_session:
    "scene/bg coding_session.png"
image bg dan_gerald_talk:
    "scene/bg dan_gerald_talk.png"
image bg dan_room:
    "scene/bg dan_room.png"
image bg gerald_room_day:
    "scene/bg gerald_room_day.png"
image bg gerald_room_night:
    "scene/bg gerald_room_night.png"
image bg graduated_pic:
    "scene/bg graduated_pic.png"
image bg shower:
    "scene/bg shower.png"
image bg corridor:
    "scene/bg corridor.png"
image bg pecs:
    "scene/scene pecs_massage.png"
image bg dan_shock:
    "scene/dan_shock.png"