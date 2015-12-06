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


class Velkoz:
    image =None

    def __init__(self):
        self.x, self.y =data['velkoz']['x'], data['velkoz']['y']
        if Velkoz.image==None:
            Velkoz.image = load_image('image\\velkoz\\velkoz.png')
        self.bgm=load_wav('bgm\\velkoz.wav')
        self.bgm.set_volume(256)


    def update(self):
        if self.x>-500:
            self.x-=10
        if game.type==1:
            if game.timer==1:
                self.bgm.play()



    def draw(self):
        self.image.draw(1100+self.x,self.y)#벨코즈 캐릭터