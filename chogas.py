from pico2d import*

import random
sys.path.append('../LabsAll/Labs')

import random
import math
import json

data_file = open('startpoint.txt','r')
data = json.load(data_file)
data_file.close()

class Chogas:
    image =None

    def __init__(self):
        self.x, self.y =data['chogas']['x'], data['chogas']['y']
        if Chogas.image==None:
            Chogas.image = load_image('image\\chogas\\chogas.png')
        self.bgm=load_wav('bgm\\chogas.wav')
        self.bgm.set_volume(128)

    def update(self):
        if self.x>-400:
            self.x-=10

    def draw(self):
         self.image.draw(1100+self.x,self.y)#초가스 캐릭터




