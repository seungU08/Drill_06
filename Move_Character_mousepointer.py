from pico2d import*

TUK_width, TUK_height = 1280, 1024
open_canvas(TUK_width , TUK_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")

def point_follow_mouse():
    pass
def handle_events():
    pass
running = True
frame = 0
x,y = TUK_width/2, TUK_height/2

while running:
    clear_canvas()
    TUK_Ground.draw(TUK_width//2, TUK_height//2)
    character.clip_draw(frame*100,100*1,100,100,x,y)
    point_follow_mouse()
    update_canvas()

    frame = (frame +1)%8
    handle_events()

close_canvas()