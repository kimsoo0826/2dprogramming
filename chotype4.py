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


class Chotype4:
    image =None

    def __init__(self):
        if Chotype4.image==None:
            Chotype4.image = load_image('image\\chogas\\chotype4.png')
        self.bgm=load_wav('bgm\\chogastype4.wav')
        self.bgm.set_volume(512)

    def draw(self):
        for i in range(0,7):
            self.image.clip_draw(game.chotype4frame[i]*100,0,100,100,100+200*(game.chotypeF[i]%4),460-270*(game.chotypeF[i]//4),200,270)
            if game.timer%4==0:
                game.chotype4frame[i]=(game.chotype4frame[i]+1)%8

            if 100+game.character.x<250+200*(game.chotypeF[i]%4) and 100+game.character.x>50+200*(game.chotypeF[i]%4) and game.hurt==0:
                if 75+game.character.y<560-270*(game.chotypeF[i]//4) and 75+game.character.y>290-270*(game.chotypeF[i]//4):
                    game.lifecount-=1
                    game.hurt=1
                    game.hurttime=game.timer