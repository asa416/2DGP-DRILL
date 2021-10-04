from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global xdir, ydir
    global mx, my
    global index
    global xdis, ydis
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - event.y + 1
            xdis, ydis = mx - x, my - y
            if x < mx:
                index = 1
                xdir = 1
            elif x > mx:
                index = 0
                xdir = -1
            else:
                xdir = 0
            if y < my:
                ydir = 1
            elif y > my:
                ydir = -1
            else:
                ydir = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = [0, 0]
index = 0 # 0 left 1 right
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2  # 마우스 커서 위치
xdir, ydir = 0, 0
xdis, ydis = 0, 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(mx, my)
    character.clip_draw(frame[index] * 100, 100 * index, 100, 100, x, y)
    update_canvas()
    frame[index] = (frame[index] + 1) % 8

    if (xdir == -1 and x > mx) or (xdir == 1 and x < mx):
        x += (xdis / 10)
    if (ydir == 1 and y < my) or (ydir == -1 and y > my):
        y += (ydis / 10)
    delay(0.05)
    handle_events()

close_canvas()
