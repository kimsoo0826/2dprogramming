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


class Pidultype4Littlebox:
    image =None

    def __init__(self):
        self.x, self.y =520+random.randint(0,280),data['littlebox']['y']
        self.fall=25+random.randint(0,10)
        if Pidultype4Littlebox.image==None:
            Pidultype4Littlebox.image = load_image('image\\pidul\\little box.png')

    def update(self):
        self.fall-=1
        self.y+=self.fall
        self.x-=7

        if game.character.x+100>self.x-60 and game.character.x+100<self.x+50 and  game.hurt==0:
            if game.character.y+75<self.y+50 and game.character.y+75>self.y-50  :
                game.lifecount-=1
                game.hurt=1
                game.hurttime=game.timer

    def draw(self):
        self.image.clip_draw(0,0, 100,100 , self.x, self.y)