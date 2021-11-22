import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server



from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"







def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)

    server.balls = [Ball() for i in range(200)]
    game_world.add_objects(server.balls, 1)

    server.brick = Brick()
    game_world.add_object(server.brick, 1)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # ball과 잔디의 충돌을 체크하고, 처리해야겠지? 이건 어디서 하면 좋을까??
    # 잔디가 충돌을 체크하도록 해볼게..
    # ball과 소년이 충돌하면? 처리? 누가하면 좋을까??
    # ball과 brick의 처리..





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






