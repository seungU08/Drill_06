from pico2d import*

TUK_width, TUK_height = 1280, 1024
open_canvas(TUK_width , TUK_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")

def move_character(p1,p2):
    x1,y1 = p1[0], p1[1]
    x2,y2 = p2[0],p2[1]
    global x,y,frame
    for i in range(0, 100, 2):
        clear_canvas()
        TUK_Ground.draw(TUK_width // 2, TUK_height // 2)
        point.draw(x2,y2)
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        if x1 <= x2:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

        if event.type == SDL_MOUSEMOTION:
            a, b = event.x, TUK_height - 1 - event.y
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05 * t)

def handle_events():
    global running,x,y,a,b,frame
    x1,y1 = x,y
    x2,y2 = 0,0

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            a, b = event.x, TUK_height - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x2, y2 = event.x , TUK_height -1 - event.y
            for i in range(0, 100, 2):
                clear_canvas()
                TUK_Ground.draw(TUK_width // 2, TUK_height // 2)
                point.draw(x2, y2)
                t = i / 100
                x = (1 - t) * x1 + t * x2
                y = (1 - t) * y1 + t * y2
                if x1 <= x2:
                    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                else:
                    character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

                update_canvas()
                frame = (frame + 1) % 8
                delay(0.05 * t)


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
    character.clip_draw(frame*100,100*1,100,100,x,y)
    point.draw(a,b)
    update_canvas()

    frame = (frame +1)%8
    handle_events()

close_canvas()