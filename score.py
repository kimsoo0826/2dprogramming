import sys
sys.path.append('../LabsAll/Labs')

import random
import json
import os
import game_framework
from pico2d import *
import game


name = "score"
image = None

data_file = open('startpoint.txt','r')
data = json.load(data_file)
data_file.close()

font=None

def enter():
    global image,font
    image=load_image('image\\score.png')
    font=load_font("font.ttf",150)


def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key)==(SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key)==(SDL_KEYDOWN, SDLK_RETURN):
                game.timer=data['title']['timer']
                game.type=random.randint(0,3)%3
                for i in range(0,7):
                    game.chotype4frame[i]=0
                    game.chotypeF[i]=random.randint(0,7)
                game.hurt=data['title']['hurt']
                game.chogas.x=data['chogas']['x']
                game.chotype1.y=data['chotype1']['y']
                game.chotype2.x, game.chotype2.y =data['chotype2']['x'],data['chotype2']['y']
                game.chotype2.frame=data['chotype2']['frame']
                game.chotype2.check=data['chotype2']['check']
                for i in range(0,30):
                    game.team[i].x=random.randint(0, 800)
                    game.team[i].y= random.randint(100, 700)+600
                game.freeze=data['title']['freeze']


                game.velkoz.x=data['velkoz']['x']
                for i in range(0,5):
                    game.velkoztype1[i].x, game.velkoztype1[i].y =random.randint(1,7)*100,data['velkoztype1']['y']
                    game.velkoztype1[i].movex=data['velkoztype1']['movex']
                    game.velkoztype1[i].timer=data['velkoztype1']['timer']
                    game.velkoztype1[i].frame=data['velkoztype1']['frame']
                    game.velkoztype1[i].dangerframe=data['velkoztype1']['dangerframe']
                game.velkoztype2.downx, game.velkoztype2.downy =data['velkoztype2']['downx'],data['velkoztype2']['downy']
                game.velkoztype2.frame=data['velkoztype2']['frame']
                for i in range(0,30):
                    game.velkoztype3[i].sandglassx, game.velkoztype3[i].sandglassy =random.randint(50,750),random.randint(120,400)
                    game.velkoztype3[i].x,game.velkoztype3[i].y=0,random.randint(-90,300)

                game.pidul.x=data['pidul']['x']
                for i in range(0,5):
                    game.pidultype1[i].x=random.randint(100,700)
                    game.pidultype1[i].y=data['pidulbat']['y']
                    game.pidultype1[i].frame=data['pidulbat']['frame']
                    game.pidultype1[i].plusx=data['pidulbat']['plusx']
                    game.pidultype1[i].plusy=data['pidulbat']['plusy']
                game.pidultype2.x==random.randint(100,700)
                game.pidultype2.y=data['movedanger']['y']
                game.drainframe=data['title']['drainframe']
                game.pidultype4Bigbox.x=data['bigbox']['x']
                game.pidultype4Bigbox.y=data['bigbox']['y']
                for i in range(0,10):
                    game.pidultype3[i].x=random.randint(100,700)
                    game.pidultype3[i].y=random.randint(100,1000)+500
                    game.pidultype3[i].angle=random.randint(0,360)
                for i in range(0,20):
                    game.pidultype4Littlebox[i].x=520+random.randint(0,280)
                    game.pidultype4Littlebox[i].y=data['littlebox']['y']
                    game.pidultype4Littlebox[i].fall=25+random.randint(0,10)

                game.lifecount=data['title']['lifecount']
                game.hurttime=data['title']['hurttime'] #맞은 시간
                game.jump=False
                game.jumpturn=False
                game.running=True

                game.character.x,game.character.y=data['character']['x'],data['character']['y']
                game.dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
                game.count=data['title']['count']
                game.freeze=data['title']['freeze']
                game.dir=data['title']['dir']
                game.scorenow=data['title']['scorenow']

                game_framework.push_state(game)




def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    font.draw(50,300,'score: %d'%game.scorenow,color=(0,255,0))
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass
