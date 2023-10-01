from pico2d import*

TUK_width, TUK_height = 1280, 1024
open_canvas(TUK_width , TUK_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")


def handle_events():
    global running,x,y,a,b

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            a,b = event.x, TUK_height - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
frame = 0
x,y = TUK_width/2, TUK_height/2
a,b = 0,0
hide_cursor()
while running:
    clear_canvas()
    TUK_Ground.draw(TUK_width//2, TUK_height//2)
    point.draw(a,b)
    character.clip_draw(frame*100,100*1,100,100,x,y)

    update_canvas()

    frame = (frame +1)%8
    handle_events()

close_canvas()