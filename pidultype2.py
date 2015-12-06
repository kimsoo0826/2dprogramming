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



class Pidultype2:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),data['movedanger']['y']
        self.frame=data['movedanger']['frame']
        self.bgm=load_wav('bgm\\pidultype2.wav')
        self.bgm.set_volume(32)
        if Pidultype2.image==None:
            Pidultype2.image = load_image('image\\danger.png')
    def update(self):
        self.frame=(self.frame+1)%4
        if game.character.x+100>self.x:
            self.x+=15
        elif game.character.x+100<self.x-50:
            self.x-=15
        if game.character.y+75>self.y:
            self.y+=15
        else:
            self.y-=15

        if game.timer==1196:
            self.bgm.play(2)
    def draw(self):
        self.image.clip_draw(0, 50*self.frame, 300,50 , self.x, self.y,100,100)