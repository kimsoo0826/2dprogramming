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

class Pidultype3:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),random.randint(100,1000)+500
        self.angle=random.randint(0,360)
        self.bgm=load_wav('bgm\\pidultype3.wav')
        self.bgm.set_volume(32)
        if Pidultype3.image==None:
            Pidultype3.image = load_image('image\\pidul\\swing bat.png')
    def update(self):
        self.angle+=2
        self.x+=10*math.cos(math.pi*(self.angle/180))
        self.y-=3

        if game.timer==1501:
            self.bgm.play()

    def draw(self):
        self.image.clip_draw(0,0, 100,50 , self.x, self.y)