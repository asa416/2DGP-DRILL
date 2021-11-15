from pico2d import *

import game_framework
import random

PIXEL_PER_METER = 10.0 / 0.2 # 참새 크기 10~20cm
FLY_SPEED_KMPH = 40.0 # 참새 속도 29~40km/h
FLY_SPEED_PPS = FLY_SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
# 참새라서 날개짓은 빠르게 하도록

class Bird:
    image = None

    def __init__(self, x, y, dir):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.frame = random.randint(0, 14)
        # 5마리 모두 날개짓이 다르게 보이도록
        if dir > x:
            self.dir = 1
        else:
            self.dir = -1
        self.velocity = FLY_SPEED_PPS * self.dir
        self.x, self.y = x, y
        self.w, self.h = 50, 50 # 약 15cm

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if self.x > 1600:
            self.dir *= -1
            self.velocity = FLY_SPEED_PPS * self.dir
        elif self.x < 0:
            self.dir *= -1
            self.velocity = FLY_SPEED_PPS * self.dir

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, self.w, self.h)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 0, 'h', self.x, self.y, self.w, self.h)

