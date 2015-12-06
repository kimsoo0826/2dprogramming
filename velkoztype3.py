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


class Velkoztype3:
    sandglass =None
    beam=None

    def __init__(self):
        self.sandglassx, self.sandglassy =random.randint(50,750),random.randint(120,400)
        self.x,self.y=data['velkoztype3']['x'],random.randint(-90,300)
        self.bgm1=load_wav('bgm\\velkoztype3.wav')
        self.bgm1.set_volume(4096)
        self.bgm2=load_wav('bgm\\sandglass.wav')
        self.bgm2.set_volume(4096)
        if Velkoztype3.beam==None:
            Velkoztype3.beam = load_image('image\\velkoz\\velkoztype3-1.png')
        if Velkoztype3.sandglass==None:
            Velkoztype3.sandglass = load_image('image\\velkoz\\velkoztype3-2.png')

    def update(self):
        if game.timer>600 and game.timer<700:
            if game.character.x+100>self.sandglassx-50 and game.character.x+100<self.sandglassx+50:
                if game.character.y+75<self.sandglassy+30 and game.character.y+75>self.sandglassy-70:
                    self.bgm2.play()
                    game.freeze=1
                    game.hurt=-1
    def draw(self):
        if game.timer>600 and game.timer<700:
            self.sandglass.clip_draw(0, 0, 100,100 , self.sandglassx, self.sandglassy)
        else:
            self.beam.clip_draw(0, 0, 1800,600 , self.x, self.y)