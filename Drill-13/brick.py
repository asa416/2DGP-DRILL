import random

from pico2d import *

import game_framework
import game_world
import server
import collision


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 100, 200
        self.speed = 200 # 200 pixel per second
        self.child_balls = [] # 발판에 속한 볻들의 리스트

    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x > 1600:
            self.x = 1600
            self.speed = -self.speed
        if self.x < 0:
            self.x = 0
            self.speed = -self.speed

        for ball in server.balls.copy():
            if collision.collide(self, ball):
                self.attach_ball(ball)
                server.balls.remove(ball)
            else:
                for child_ball in self.child_balls:
                    if collision.collide(child_ball, ball):
                        self.attach_ball(ball)
                        server.balls.remove(ball)
                        break

        # 확인한다.. 뭘? 자식볼들의 갯수를..
        if len(self.child_balls) > 10:
            # 부모자식관계를 끊고..
            for child_ball in self.child_balls:
                child_ball.bye()
            # 볼들을 다 보낸다? 어디로? balls 에 다시 보낸다.
            server.balls += self.child_balls
            self.child_balls.clear()
            # brick을 없앤다..
            game_world.remove_object(self)


    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass


    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20

    def attach_ball(self, ball):
        self.child_balls.append(ball)
        ball.set_parent(self) # 볼에 대해서 부모를 정한다.

