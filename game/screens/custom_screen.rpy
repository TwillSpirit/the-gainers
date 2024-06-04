style splash_screen_vbox:
  xalign 0.5
  yalign 0.5
  spacing 48

style splash_screen_text:
  xalign 0.5
  xfill True
  color color.black
  font "fonts/NovaFlat-Book.ttf"
  size 33

style splash_screen_title is splash_screen_text
style splash_screen_subtitle is splash_screen_text

style splash_screen_title:
  font "fonts/NovaFlat-Bold.ttf"
  size 64

style splash_screen_subtitle:
  font "fonts/NovaFlat-Book.ttf"
  size 128

screen splash_screen(title="Title", subtitle="subtitle"):
  frame:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill True
    background color.white

    vbox:
      style "splash_screen_vbox"
      text "[title]" style "splash_screen_title"
      text "[subtitle]" style "splash_screen_subtitle"


screen narator_screen(text="Lorem ipsum dolor sit amet"):
  frame:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill True
    background "#ffffffcc"

    vbox:
      style "splash_screen_vbox"
      text "[text]" style "splash_screen_text"
      


screen simple_splash_screen(text="This is text"):
  zorder 998
  frame:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill True
    background color.white

    vbox:
      style "splash_screen_vbox"
      text "[text]" style "splash_screen_text"