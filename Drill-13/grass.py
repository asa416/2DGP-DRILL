from pico2d import *
import server
import collision

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        # 볼들과 잔디의 충돌을 누가? 잔디가 체크한다...
        for ball in server.balls:
            if collision.collide(ball, self):
                ball.stop()
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        # fill here
        draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return 0, 0, 1600-1, 50
