from pico2d import *
import random

class Ball:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 599
        self.size = random.randint(0, 1) # 0 small 1 big
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.t = random.randint(1, 50) / 1000
        self.speed = random.randint(1, 10) / 1000

    def update(self):
        if self.t <= 1.0:
            if self.size == 0:
                self.y = (1 - self.t) * self.y + self.t * (30 + 20)
            else:
                self.y = (1 - self.t) * self.y + self.t * (30 + 40)
            self.t += self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0,7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
grass = Grass()
team = [Boy() for i in range(1, 11 + 1)]
balls = [Ball() for i in range(1, 20 + 1)]
running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

