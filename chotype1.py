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

class Chotype1:
    image =None

    def __init__(self):
        self.x, self.y =data['chotype1']['x'],data['chotype1']['y']
        self.frame=data['chotype1']['frame']
        if Chotype1.image==None:
            Chotype1.image = load_image('image\\chogas\\chotype1.png')

    def update(self):
        if game.timer%4==0:
            self.frame=(self.frame+1)%4
        self.y+=25-(game.timer-150)
    def draw(self):
        if game.timer>150 and game.timer<300:
            self.image.draw(400,-50+self.y)
        if 75+game.character.y<self.y and game.hurt==0:
                game.lifecount-=1
                game.hurt=1
                game.hurttime=game.timer
