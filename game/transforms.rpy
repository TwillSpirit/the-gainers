transform move_pos(new_pos, time=1.5):
    ease time xcenter new_pos yalign 1.0
transform new_pos (new_pos):
    xcenter new_pos yalign 1.0
transform bolt_pos(new_pos, time=0.8):
    ease time xcenter new_pos yalign 1.0

transform shaking(current_pos):
    xcenter current_pos
    ease 0.05 xoffset 1
    ease 0.05 xoffset -1
    repeat

transform bounce:
    yoffset 0
    easein .15 yoffset -30
    easeout .05 yoffset 0
    yoffset 0

transform flip(time=0.3):
    ease 0.3 xzoom -1.0
transform unflip(time=0.3):
    ease 0.3 xzoom 1.0
