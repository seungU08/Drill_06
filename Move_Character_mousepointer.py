from pico2d import*

TUK_width, TUK_height = 1280, 1024
open_canvas(TUK_width , TUK_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")

running = True
frame = 0
x,y = TUK_width, TUK_height

