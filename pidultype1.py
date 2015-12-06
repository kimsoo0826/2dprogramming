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



class Pidultype1:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),550
        self.frame=0
        self.plusx=5
        self.plusy=5
        self.bgm=load_wav('bgm\\pidultype1.wav')
        self.bgm.set_volume(32)
        if Pidultype1.image==None:
            Pidultype1.image = load_image('image\\pidul\\pidul bat.png')

    def update(self):
        self.x-=self.plusx
        self.y-=self.plusy

        if self.x<50:
            self.plusx*=-1
        if self.x>750:
            self.plusx*=-1
        if self.y>550:
            self.plusy*=-1
        if self.y<110:
            self.plusy*=-1

        if self.plusx>0:
            if self.plusy>0:
                self.frame=0
            else:
                self.frame=3
        else:
            if self.plusy>0:
                self.frame=1
            else:
                self.frame=2

        if game.character.x+100>self.x-50 and game.character.x+100<self.x+50 and game.hurt==0:
            if game.character.y+75<self.y and game.character.y+75>self.y-100:
                game.lifecount-=1
                game.hurt=1
                game.hurttime=game.timer

    def draw(self):
        self.image.clip_draw(100*self.frame, 0, 100,100 , self.x, self.y)