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

class Pidul:
    image =None

    def __init__(self):
        self.x, self.y =data['pidul']['x'],data['pidul']['y']
        self.bgm=load_wav('bgm\\pidul.wav')
        self.bgm.set_volume(32)
        if Pidul.image==None:
            Pidul.image = load_image('image\\pidul\\pidul.png')


    def update(self):
        if self.x>-500:
            self.x-=10
        if game.timer==1:
            self.bgm.play()


    def draw(self):
        self.image.draw(950+self.x,250)