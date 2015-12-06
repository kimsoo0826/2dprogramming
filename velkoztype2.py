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


class Velkoztype2:
    image1=None
    image2=None

    def __init__(self):
        self.downx, self.downy =data['velkoztype2']['downx'],data['velkoztype2']['downy']
        self.frame=data['velkoztype2']['frame']
        self.bgm=load_wav('bgm\\velkoztype2.wav')
        self.bgm.set_volume(4096)

        if Velkoztype2.image1==None:
            Velkoztype2.image1 = load_image('image\\velkoz\\velkoztype2-2.png')
        if Velkoztype2.image2==None:
            Velkoztype2.image2 = load_image('image\\velkoz\\velkoztype2-1.png')


    def update(self):
        if game.timer>320 and game.timer<600:
            if 875+self.downy  >525:
                self.downy -=50

            if game.character.y+75>250 and game.hurt==0:
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer
            if game.timer%8==0:
                self.frame=(self.frame+1)%8
            if game.timer ==390 or game.timer==453 or game.timer==517:
                self.frame=0
        if game.timer==453 or game.timer==581:
                self.bgm.play()
                if game.character.x+75>80 and game.character.x+75<180:
                    game.jump=1
                if game.character.x+75>280 and game.character.x+75<380:
                    game.jump=1
                if game.character.x+75>480 and game.character.x+75<580:
                    game.jump=1
                if game.character.x+75>680 and game.character.x+75<780:
                    game.jump=1
        if game.timer==389 or game.timer==517:
                self.bgm.play()
                if game.character.x+75>-20 and game.character.x+75<80:
                    game.jump=1
                if game.character.x+75>180 and game.character.x+75<280:
                    game.jump=1
                if game.character.x+75>380 and game.character.x+75<480:
                    game.jump=1
                if game.character.x+75>580 and game.character.x+75<680:
                    game.jump=1
    def draw(self):
        self.image1.draw(400,875+self.downy,800,600)

        if (game.timer>325 and game.timer<=389) or (game.timer>453 and game.timer<=517):
            self.image2.clip_draw(100*self.frame,0,100,100,50,10)
            self.image2.clip_draw(100*self.frame,0,100,100,250,10)
            self.image2.clip_draw(100*self.frame,0,100,100,450,10)
            self.image2.clip_draw(100*self.frame,0,100,100,650,10)
        if (game.timer>389 and game.timer<=453) or (game.timer>517 and game.timer<=581):
            self.image2.clip_draw(100*self.frame,0,100,100,150,10)
            self.image2.clip_draw(100*self.frame,0,100,100,350,10)
            self.image2.clip_draw(100*self.frame,0,100,100,550,10)
            self.image2.clip_draw(100*self.frame,0,100,100,750,10)
