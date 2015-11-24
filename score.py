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

font=None

def enter():
    global image,font
    image=load_image('image\\score.png')
    font=load_font("font.ttf",200)


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
                game.timer=0
                game.type=random.randint(0,3)%3
                for i in range(0,7):
                    game.chotype4frame[i]=0
                    game.chotypeF[i]=random.randint(0,7)
                game.hurt=0
                game.chogas.x=0
                game.chotype1.y=0
                game.chotype2.x, game.chotype2.y =0,0
                game.chotype2.frame=0
                game.chotype2.check=0
                for i in range(0,30):
                    game.team[i].x=random.randint(0, 800)
                    game.team[i].y= random.randint(100, 700)+600
                game.freeze=0


                game.velkoz.x=0
                for i in range(0,5):
                    game.velkoztype1[i].x, game.velkoztype1[i].y =random.randint(1,7)*100,0
                    game.velkoztype1[i].movex=0
                    game.velkoztype1[i].timer=0
                    game.velkoztype1[i].frame=0
                    game.velkoztype1[i].dangerframe=0
                game.velkoztype2.downx, game.velkoztype2.downy =0,0
                game.velkoztype2.frame=0
                for i in range(0,30):
                    game.velkoztype3[i].sandglassx, game.velkoztype3[i].sandglassy =random.randint(50,750),random.randint(120,400)
                    game.velkoztype3[i].x,game.velkoztype3[i].y=0,random.randint(-90,300)

                game.pidul.x=0
                for i in range(0,5):
                    game.pidulbat[i].x=random.randint(100,700)
                    game.pidulbat[i].y=550
                    game.pidulbat[i].frame=0
                    game.pidulbat[i].plusx=5
                    game.pidulbat[i].plusy=5
                game.movedanger.x==random.randint(100,700)
                game.movedanger.y=110
                game.drainframe=0
                game.bigbox.x=600
                game.bigbox.y=500
                for i in range(0,10):
                    game.swingbat[i].x=random.randint(100,700)
                    game.swingbat[i].y=random.randint(100,1000)+500
                    game.swingbat[i].angle=random.randint(0,360)
                for i in range(0,20):
                    game.littlebox[i].x=520+random.randint(0,280)
                    game.littlebox[i].y=210
                    game.littlebox[i].fall=25+random.randint(0,10)

                game.lifecount=2
                game.hurttime=0 #맞은 시간
                game.jump=False
                game.jumpturn=False
                game.running=True

                game.character.x,game.character.y=0,0
                game.state=0
                game.dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
                game.count=0
                game.mousex=0
                game.mousey=0
                game.freeze=0
                game.dir=0
                game.lastscore=0
                game.scorenow=0

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
