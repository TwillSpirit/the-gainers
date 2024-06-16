style splash_screen_vbox:
  xalign 0.5
  yalign 0.5
  spacing 48

style splash_screen_text:
  xalign 0.5
  xfill True
  font "fonts/NovaFlat-Book.ttf"
  size 33

style splash_screen_text_light is splash_screen_text
style splash_screen_text_dark is splash_screen_text

style splash_screen_text_light:
  color color.black

style splash_screen_text_dark:
  color color.white

style splash_screen_title is splash_screen_text
style splash_screen_subtitle is splash_screen_text

style splash_screen_title:
  font "fonts/NovaFlat-Bold.ttf"
  color color.black
  size 64

style splash_screen_subtitle:
  font "fonts/NovaFlat-Book.ttf"
  color color.black
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


screen narator_screen(text="Lorem ipsum dolor sit amet", background_color="#ffffffcc", mode="light"):
  frame:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill True
    background background_color

    vbox:
      style "splash_screen_vbox"
      text "[text]" style f"splash_screen_text_{mode}"


screen dream_thought_screen(text="text", font_size=48):
  zorder 998
  frame:
    xalign 0.5
    yalign 0.5
    xfill True
    yfill True
    background '#000000'

    vbox:
      style "splash_screen_vbox"
      text "[text]":
        style "splash_screen_text_dark"
        size font_size
  # add Snow('dot-red.png')


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
      text "[text]" style "splash_screen_text_light"

style credit_text:
  color '#000000'
  font "fonts/OpenSans-Medium.ttf"

style credit_title_text is credit_text
style credit_button_text is credit_text

style credit_title_text:
  size 33

style link is credit_title_text
style link:
  color color.blue.normal
  hover_color color.blue.dark

style credit_hbox:
  spacing 10

style credit_button:
  background color.blue.normal
  xpadding 10
  ypadding 10
  hover_background color.blue.dark

style credit_button_text:
  font "fonts/NovaFlat-Bold.ttf"
  color color.white

style patreon_button is credit_button
style patreon_button_text is credit_button_text
style patreon_button:
  background "#df7132"
  hover_background "#bd5920"

screen credit():
  tag menu

  style_prefix "credit"

  use game_menu(_("Credit"), scroll="viewport"):
    vbox:
      text "Music" style "credit_title_text"

      text "Imagefilm 017 by Sascha Ende\n{a=https://filmmusic.io/song/314-imagefilm-017, color=#ff0000}{=link}Link to download{/=link}{/a}\n{a=https://filmmusic.io/standard-license}{=link}License (CC BY 4.0){/=link}{/a}\n"

      text "Play A Little Game (DECISION) by Sascha Ende\n{a=https://filmmusic.io/song/249-play-a-little-game-decision}{=link}Link to download{/=link}{/a}\n{a=https://filmmusic.io/standard-license}{=link}License (CC BY 4.0){/=link}{/a}\n"

      text "Cinematic Suspense Series Episode 008 by Sascha Ende\n{a=https://filmmusic.io/song/7669-cinematic-suspense-series-episode-008}{=link}Link to download{/=link}{/a}\n{a=https://filmmusic.io/standard-license}{=link}License (CC BY 4.0){/=link}\n{/a}"

      text "Team" style "credit_title_text"

      text "Tamcin: Illustrator & Programmer"
      text "Twill: Story\n"

      text "Social Media" style "credit_title_text"
      hbox:
        textbutton _('Tamcin\'s Twitter / X') action OpenURL("https://x.com/VoidFoxTamcin")

        textbutton _('Tamcin\'s Patreon') action OpenURL("patreon.com/VoidFoxTamcin") style "patreon_button"

        textbutton _('Twill\'s Twitter / X') action OpenURL("https://x.com/twillthespirit")