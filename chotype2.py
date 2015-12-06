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

class Chotype2:
    image =None

    def __init__(self):
        self.x, self.y =data['chotype2']['x'],data['chotype2']['y']
        self.frame=data['chotype2']['frame']
        self.check=data['chotype2']['check']
        if Chotype2.image==None:
            Chotype2.image = load_image('image\\chogas\\chotype2.png')

    def update(self):
        if game.timer%2==0 and self.frame<=7 and self.check==0:
            self.frame=(self.frame+1)
        if self.frame==8:
            self.check=1
        if self.check==1 and self.frame>0 and game.timer%2==0:
            self.frame=(self.frame-1)
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,450,325,700,500)

        if 100+game.character.x>800-(100*self.frame) and game.hurt==0:
            game.lifecount-=1
            game.hurt=1
            game.hurttime=game.timer