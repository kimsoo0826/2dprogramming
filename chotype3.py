from pico2d import*


import random
sys.path.append('../LabsAll/Labs')

import random
import math
import json
import game

data_file = open('startpoint.txt','r')
data = json.load(data_file)
data_file.close()


class Chotype3:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(0, 800), random.randint(100, 700)+600
        self.bgm=load_wav('bgm\\chogastype3.wav')
        self.bgm.set_volume(128)
        if Chotype3.image==None:
            Chotype3.image = load_image('image\\chogas\\chotype3.png')

    def update(self):
        self.y -=5

    def draw(self):
        self.image.clip_draw(0, 0, 50, 100, self.x, self.y)

        for i in range(0,10):
            if self.x-5-5*i<game.character.x+100 and self.x+5+5*i>game.character.x+100:
                if self.y-72+i*8>75+game.character.y and self.y-80+i*8<75+game.character.y and game.hurt==0:
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer