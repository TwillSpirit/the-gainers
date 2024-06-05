transform move_pos(new_pos, time=1.5):
    ease time xcenter new_pos yalign 1.0
transform new_pos (new_pos):
    xcenter new_pos yalign 1.0
transform bolt_pos(new_pos, time=0.8):
    ease time xcenter new_pos yalign 1.0

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -30
    easeout .175 yoffset 0
    yoffset 0

transform flip(time=0.3):
    ease 0.3 xzoom -1.0
transform unflip(time=0.3):
    ease 0.3 xzoom 1.0
