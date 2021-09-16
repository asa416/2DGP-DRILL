from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while True:
    for i in range(-90, 270 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(235 * math.cos(i / 180 * math.pi) + 400, 235 * math.sin(i / 180 * math.pi) + 325)
        delay(0.01)
    for i in range(400, 780 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, 90)
        delay(0.002)
    for i in range(90, 560 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, i)
        delay(0.002)
    for i in range(20, 780 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800 - i, 560)
        delay(0.002)
    for i in range(90, 560 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(20, 650 - i)
        delay(0.002)
    for i in range(20, 400 + 1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(i, 90)
        delay(0.002)

close_canvas()
