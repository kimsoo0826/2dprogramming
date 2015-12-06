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

class Pidultype4Bigbox:
    image =None

    def __init__(self):
        self.x, self.y =data['bigbox']['x'],data['bigbox']['y']
        self.bgm=load_wav('bgm\\pidultype4.wav')
        self.bgm.set_volume(32)
        if Pidultype4Bigbox.image==None:
            Pidultype4Bigbox.image = load_image('image\\pidul\\big box.png')

    def update(self):
        if self.y>200:
            self.y-=50
        if game.character.x+100>self.x-150 and game.character.x+100<self.x+300 and \
                                game.character.y+75>self.y-150 and game.character.y+75<self.y and game.hurt==0:
            game.lifecount-=1
            game.hurt=1
            game.hurttime=game.timer
        if game.timer==2101:
            self.bgm.play(3)



    def draw(self):
        self.image.clip_draw(0,0, 400,300 , self.x, self.y)