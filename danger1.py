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

class Danger1:
    image =None

    def __init__(self):
        self.x, self.y =data['danger1']['x'],data['danger1']['y']
        self.frame=data['danger1']['frame']
        self.timer=data['danger1']['timer']
        self.bgm1=load_wav('bgm\\chogastype1.wav')
        self.bgm1.set_volume(128)
        self.bgm2=load_wav('bgm\\chogastype2.wav')
        self.bgm2.set_volume(128)
        if Danger1.image==None:
            Danger1.image = load_image('image\\danger.png')

    def update(self):
        self.timer+=1
        if self.timer%4==0:
            self.frame=(self.frame+1)%4


    def draw(self):
        if game.type==0:
            if game.timer<150 and game.timer>40:
                self.image.clip_draw(0,self.frame*50,800,50,400,150,800,200)
                if game.timer==80:
                    self.bgm1.play()
            if game.timer<400 and game.timer>300:
                self.image.clip_draw(0,self.frame*50,800,50,450,300,700,600)
                if game.timer==390:
                    self.bgm2.play()
            if game.timer<950 and game.timer>900:
                for i in range(0,7):
                    self.image.clip_draw(0,game.dangerline[i]*50,800,50,100+200*(game.chotypeF[i]%4),460-270*(game.chotypeF[i]//4),200,270)
                    if game.timer%4==0:
                        game.dangerline[i]=(game.dangerline[i]+1)%4