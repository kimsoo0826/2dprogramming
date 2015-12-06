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



class Velkoztype1:
    image1=None
    image2=None
    image3=None
    danger=None

    def __init__(self):
        self.x, self.y =random.randint(1,7)*100,data['velkoztype1']['y']
        self.movex=data['velkoztype1']['movex']
        self.timer=data['velkoztype1']['timer']
        self.frame=data['velkoztype1']['frame']
        self.dangerframe=data['velkoztype1']['dangerframe']
        self.bgm1=load_wav('bgm\\velkoztype1and1.wav')
        self.bgm2=load_wav('bgm\\velkoztype1and2.wav')
        self.bgm3=load_wav('bgm\\velkoztype1and3.wav')
        self.bgm1.set_volume(8192)
        self.bgm2.set_volume(8192)
        self.bgm3.set_volume(8192)


        if Velkoztype1.danger==None:
            Velkoztype1.danger = load_image('image\\danger2.png')
        if Velkoztype1.image1==None:
            Velkoztype1.image1 = load_image('image\\velkoz\\velkoztype1-1.png')
        if Velkoztype1.image2==None:
            Velkoztype1.image2 = load_image('image\\velkoz\\velkoztype1-2.png')
        if Velkoztype1.image3==None:
            Velkoztype1.image3 = load_image('image\\velkoz\\velkoztype1-3.png')


    def update(self):
        self.timer+=1
        if self.timer%8==0:
            self.frame=(self.frame+1)%4
        if self.timer==119:
                self.frame=0
        if self.timer==144:
                self.frame=0
        if self.timer>145 and self.timer<225:
            self.movex+=10

        if self.timer>50 and self.timer<120:

            if self.y<700:
                self.y+=10

        if self.timer%4==0 and self.timer<50:
            self.dangerframe=(self.dangerframe+1)%4

    def draw(self):
        if self.timer>10 and self.timer<320:
            if self.timer<50:
                self.danger.clip_draw(self.dangerframe*100,0,100,800,self.x,300)

        if self.timer>50 and self.timer<120:
            self.image1.clip_draw(self.frame*100,0,100,100,self.x,800-self.y)

            if 100+game.character.x>self.x and 100+game.character.x<self.x+100 and game.hurt==0:
                if 75+game.character.y<800-self.y and 75+game.character.y>700-self.y:
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer
        if self.timer>120 and self.timer<145:
            self.image2.clip_draw(self.frame*100,0,100,100,self.x,100)
            if game.timer%8==0:
                self.frame=(self.frame+1)%3

        if self.timer>145 and self.timer<225:
            self.image3.clip_draw(100,0,100,100,self.x+self.movex,100)
            self.image3.clip_draw(0,0,100,100,self.x-self.movex,100)
            if game.character.x+100>self.x+self.movex and game.character.x+100<100+self.x+self.movex and game.hurt==0:
                if game.character.y+75<100:
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer
            if game.character.x+100>self.x-self.movex and game.character.x+100<100+self.x-self.movex and game.hurt==0:
                if game.character.y+75<100:
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer