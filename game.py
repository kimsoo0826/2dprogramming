
from pico2d import *

import score
import game_framework
import sys

from chogas import Chogas
from danger1 import Danger1
from chotype1 import Chotype1
from chotype2 import Chotype2
from chotype3 import Chotype3
from chotype4 import Chotype4
from velkoz import Velkoz
from velkoztype1 import Velkoztype1
from velkoztype2 import Velkoztype2
from velkoztype3 import Velkoztype3
from pidul import Pidul
from pidultype1 import Pidultype1
from pidultype2 import Pidultype2
from pidultype3 import Pidultype3
from pidultype4Bigbox import Pidultype4Bigbox
from pidultype4Littlebox import Pidultype4Littlebox

sys.path.append('../LabsAll/Labs')

import random
import math
import json
import os






name = "MainState"
image = None

data_file = open('startpoint.txt','r')
data = json.load(data_file)
data_file.close()

current_time=get_time()

lifecount=data['title']['lifecount']
hurt=data['title']['hurt']   #맞음
hurttime=data['title']['hurttime'] #맞은 시간
timer=data['title']['timer']
scorenow=data['title']['scorenow']
jump=False
jumpturn=False
running=True
RIGHT_STATE,LEFT_STATE,STAND_STATE=data['title']['RIGHT_STATE'],data['title']['LEFT_STATE'],data['title']['STAND_STATE']
type=2#random.randrange(0,3)%3


class Ground:

    def __init__(self):
        self.image=load_image('image\\ground.png')
        self.bgm=load_music('bgm\\ans.mp3')
        self.bgm.set_volume(16)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400,300)


class Character:

    PIXEL_PER_METER=(10.0/0.1)
    RUN_SPEED_KMPH=20.0
    RUN_SPEED_MPM=(RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS * PIXEL_PER_METER)


    image =None


    def __init__(self):
        self.x, self.y =data['character']['x'],data['character']['y']
        self.state=data['character']['state']
        if Character.image==None:
            Character.image = load_image('image\\character.png')


    def update(self,frame_time):
        global dir,RIGHT_STATE,LEFT_STATE
        distance=Character.RUN_SPEED_PPS*frame_time



        if not(timer>1500 and timer<=2100):
            if self.state==RIGHT_STATE:
                self.x=min(690,self.x+dir*distance/2)
            if self.state==LEFT_STATE:
                self.x=max(-90,self.x+dir*distance/2)
        else:
            if self.state==LEFT_STATE:
                self.x=min(690,self.x+(-1*dir*distance/2))
            if self.state==RIGHT_STATE:
                self.x=max(-90,self.x+(-1*dir*distance/2))


    def draw(self):
        self.image.draw(100+self.x,75+self.y,50,40)

########

dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
count=data['title']['count']
freeze=data['title']['freeze']
dir=data['title']['dir']

ground=None
gameback=None
life=None
cho=None
vel=None
pi=None
chotype1=None
chotype2=None
chotype4=None
danger=None
character=None
title=None
team = None
chotypeF= None
checktype4=None
chotype4frame=None
chotype3=None
font=None
bgm=None
ground=None

def enter():
    global ground,gameback,life,pidul,character,title,font
    global chogas,chotype1,chotype2,chotype4,danger,team,chotypeF,checktype4,chotype4frame,chotype3
    global velkoz,danger2,velkozr,velkoztype3,velkoztype1,velkoztype2
    global pidultype1,pidultype2,drain,drainframe,fear,pidultype3, pidultype4Bigbox, pidultype4Littlebox
    global bgm



    ground = Ground()
    gameback = load_image('image\\gameback.png')
    life=load_image('image\\life.png')#생명
    font=load_font("font.ttf",20)
    character=Character()
    danger=Danger1()
    chogas=Chogas()
    velkoz=Velkoz()
    pidul=Pidul()
    chotype1=Chotype1()
    chotype2=Chotype2()
    chotype3=Chotype3()
    team = [Chotype3() for i in range(30)] #초가스 e 개수

    chotype4=Chotype4()
    velkoztype1=[Velkoztype1() for i in range(0,5)]
    velkoztype2=Velkoztype2()
    velkoztype3=[Velkoztype3() for i in range(30)]

    drain=load_image('image\\pidul\\pidul w.png')#피들스틱 흡수
    fear=load_image('image\\pidul\\fear.png')#피들스틱 공포
    pidultype2=Pidultype2()
    pidultype1=[Pidultype1() for i in range(5)]#튕기는 박쥐 5마리
    chotypeF= [0] * 7
    checktype4=[0]*7
    chotype4frame=[0]*7
    drainframe=data['title']['drainframe']
    pidultype4Bigbox=Pidultype4Bigbox()
    pidultype4Littlebox=[Pidultype4Littlebox() for i in range(20)]
    pidultype3=[Pidultype3() for i in range(10)]



def exit():
    global image
    del(image)


def handle_events():
    global running
    global character
    global jump
    global dir,RIGHT_STATE,LEFT_STATE,STAND_STATE
    global jumpturn
    global count
    global mainscreen,freeze
    global lifecount
    if lifecount==-1:
        game_framework.push_state(score)
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        if freeze==0:
            if event.type==SDL_KEYDOWN :
                if event.key==SDLK_ESCAPE:
                    game_framework.quit()
                if event.key==SDLK_SPACE:
                    jump+=1
                if event.key==SDLK_RIGHT:
                    character.state=RIGHT_STATE
                    dir+=1
                elif event.key==SDLK_LEFT:
                    character.state=LEFT_STATE
                    dir-=1
            if event.type==SDL_KEYUP:
                if event.key==SDLK_RIGHT:
                    character.state=LEFT_STATE
                    dir-=1
                if event.key==SDLK_LEFT:
                    character.state=RIGHT_STATE
                    dir+=1
        if freeze==1:
            dir=0
    if jump!=0 and jump!=2:
        character.y+=20-count
        count+=1
        if(character.y<=0):
            count=0
            character.y=0
            jump=0
    if jump==2:
        jumpturn=True
    if jumpturn==True:
        count=0
        jumpturn=False
        jump+=1



def draw():
    clear_canvas()
    global gameback
    global timer,lifecount,hurt,type,hurttime,life,character,ground,jump
    global chogas,danger,chotype1,chotype2, chotype3,chotype4,team
    global velkoz,velkoztype1,velkoztype3,danger2,freeze
    global pidul,pidultype1,pidultype1team,drainframe,pidultype2,drain,pidultype4Bigbox,pidultype4Littlebox
    gameback.draw(400,300)#검은 배경



    if type==0:
        chogas.draw()
        if timer<150 and timer>40:
            danger.draw()
        if timer>150 and timer<=300: #기술 등장
            chotype1.draw()
        if timer>300 and timer<=400:
            danger.draw()
        if timer>400 and timer<550:  #w 완료
            chotype2.draw()
        if timer>550 and timer<900:#초가스e시작
            for chotype3 in team:
                chotype3.draw()
        if timer<950:
            danger.draw()
        if timer>950 and timer<980 :
            chotype4.draw()




    if type==1:
        velkoz.draw()

        if timer>10 and timer<320:
            velkoztype1[0].draw()
        if timer>30 and timer<320:
            velkoztype1[1].draw()
        if timer>50 and timer<320:
            velkoztype1[2].draw()
        if timer>70 and timer<320:
            velkoztype1[3].draw()
        if timer>90 and timer<320:
            velkoztype1[4].draw()

        ground.draw()

        if timer>320 and timer<600:
            velkoztype2.draw()

        if timer>600 and timer<700:
            velkoztype3[0].draw()

        if timer>=700 and timer<1340:
            for i in range(0,30):
                if timer>700+(20*i) and timer<720+(20*i):
                    velkoztype3[i].draw()

    if type==2:
        pidul.draw()

        if timer>100:
            for i in range(0,5):
                if timer>100+i*100 and timer<600+i*100:
                    pidultype1[i].draw()


        if timer>1000 and timer<1500:
            if timer<1200:
                pidultype2.draw()
            if timer>1200:
                drain.clip_draw(800*drainframe,0,800,800,pidultype2.x+300,pidultype2.y+300)

        if timer>1500 and timer<2100:
            fear.draw(character.x+100,character.y+125,100,100)
            for i in range (0,10):
                pidultype3[i].draw()

        if timer>2100 and timer <2900:
            pidultype4Bigbox.draw()

            if timer>2200 :
                for i in range(0,20):
                    if timer>2200+i*25 and timer<2400+i*100:
                        pidultype4Littlebox[i].draw()


    if hurt==0:
        character.draw()
    if hurt==1:
        if timer%6==0:
            character.draw()
    if type!=1:
       ground.draw() #땅

    life.clip_draw(266*lifecount,0,266,600,150,560,300,200)
    font.draw(50,500,'score: %d'%scorenow,color=(0,255,0))
    update_canvas()


def get_frame_time():

    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
    global gameback,dir,scorenow,bgm,chogasbgm,current_time
    global timer,lifecount,hurt,type,hurttime,life,character,ground,jump,jumpturn
    global chogas,danger,chotype1,chotype2, chotype3,chotype4,team
    global velkoz,velkoztype1,velkoztype3,danger2,freeze
    global pidul,pidultype1,pidultype1team,drainframe,pidultype2,drain,pidultype4Bigbox,pidultype4Littlebox,scorenow


    frame_time=get_frame_time()

    if lifecount==-1:
        game_framework.push_state(score)


    scorenow+=1
    character.update(frame_time)
    if hurt==1 and timer>=hurttime+100:
            hurt=0

    if type==0:
        timer+=1
        chogas.update()
        if timer==1:
            chogas.bgm.play()

        if timer>150 and timer<=300: #기술 등장
            chotype1.update()
        if timer>400 and timer<550:  #w 완료
            chotype2.update()
        if timer>550 and timer<900:#초가스e시작
            for chotype3 in team:
                chotype3.update()
                if timer==551:
                    team[0].bgm.play(5)


        if timer<950:
            if timer==940:
                chotype4.bgm.play()
            danger.update()
            if timer>=900:   #초가스 r 시작
                for i in range(0,7):
                    if chotypeF[i]==0 and checktype4[i]==0:
                        chotypeF[i]=random.randint(0,7)
                    for j in range(0,i-1):
                        if chotypeF[i]==chotypeF[j]:
                            chotypeF[i]=random.randint(0,7)
                    checktype4[i]=1
        if timer ==1080:
            timer=data['title']['timer']
            type=random.randint(0,3)%3
            while type==0:
                type=random.randint(0,3)%3
            for i in range(0,7):
                chotype4frame[i]=0
                chotypeF[i]=random.randint(0,7)
            hurt=data['title']['hurt']
            chogas.x=data['chogas']['x']
            chotype1.y=data['chotype1']['y']
            chotype2.x, chotype2.y =data['chotype2']['x'],data['chotype2']['y']
            chotype2.frame=data['chotype2']['frame']
            chotype2.check=data['chotype2']['check']
            for i in range(0,30):
                team[i].x=random.randint(0, 800)
                team[i].y= random.randint(100, 700)+600

    if type==1:
        timer+=1
        velkoz.update()
        if timer>10 and timer<320:
            if timer==51:
                velkoztype1[0].bgm1.play()
            if timer==121:
                velkoztype1[0].bgm2.play()
            if timer==146:
                velkoztype1[0].bgm3.play()
            velkoztype1[0].update()
        if timer>30 and timer<320:
            if timer==71:
                velkoztype1[1].bgm1.play()
            if timer==141:
                velkoztype1[1].bgm2.play()
            if timer==166:
                velkoztype1[1].bgm3.play()
            velkoztype1[1].update()
        if timer>50 and timer<320:
            if timer==91:
                velkoztype1[2].bgm1.play()
            if timer==161:
                velkoztype1[2].bgm2.play()
            if timer==186:
                velkoztype1[2].bgm3.play()
            velkoztype1[2].update()
        if timer>70 and timer<320:
            if timer==111:
                velkoztype1[3].bgm1.play()
            if timer==181:
                velkoztype1[3].bgm2.play()
            if timer==206:
                velkoztype1[3].bgm3.play()
            velkoztype1[3].update()
        if timer>90 and timer<320:
            if timer==51:
                velkoztype1[4].bgm1.play()
            if timer==121:
                velkoztype1[4].bgm2.play()
            if timer==146:
                velkoztype1[4].bgm3.play()
            velkoztype1[4].update()
        if timer>320 and timer<600:
            velkoztype2.update()
        if timer>600 and timer<700:
            velkoztype3[0].update()
        if timer>=700 and timer<1340:
            for i in range(0,30):
                if timer>700+(20*i) and timer<720+(20*i):
                    if timer==701+(20*i):
                        velkoztype3[i].bgm1.play()
                    if character.y+75<velkoztype3[i].y+200+100 and character.y+75>velkoztype3[i].y-100+200 and hurt==0:#충돌체크 조금만 더
                        lifecount-=1
                        hurt=1
                        hurttime=timer
            if timer>1320:
                freeze=0

        if timer>1340:
            timer=data['title']['timer']
            type=random.randint(0,5)%3
            while type==1:
                type=random.randint(0,5)%3
            hurt=data['title']['hurt']
            velkoz.x=data['velkoz']['x']
            for i in range(0,5):
                velkoztype1[i].x, velkoztype1[i].y =random.randint(1,7)*100,0
                velkoztype1[i].movex=data['velkoztype1']['movex']
                velkoztype1[i].timer=data['velkoztype1']['timer']
                velkoztype1[i].frame=data['velkoztype1']['frame']
                velkoztype1[i].dangerframe=data['velkoztype1']['dangerframe']
            velkoztype2.downx, velkoztype2.downy =data['velkoztype2']['downx'],data['velkoztype2']['downy']
            velkoztype2.frame=data['velkoztype2']['frame']
            for i in range(0,30):
                velkoztype3[i].sandglassx, velkoztype3[i].sandglassy =random.randint(50,750),random.randint(120,400)
                velkoztype3[i].x,velkoztype3[i].y=data['velkoztype3']['x'],random.randint(-90,300)

    if type==2:
        timer+=1
        pidul.update()
        if timer>100:
            for i in range(0,5):
                if timer>100+i*100 and timer<600+i*100:
                    if timer==101+i*100:
                        pidultype1[i].bgm.play()
                    pidultype1[i].update()
        if timer>1000 and timer<1500:
            if timer%4==0 and timer<1200:
                pidultype2.update()
            if timer>1200:
                if timer%4==0:
                    drainframe=(drainframe+1)%8
                if character.x+100>pidultype2.x-50 and character.x+100<pidultype2.x+100 and\
                                        character.y+75>pidultype2.y and character.y+75<pidultype2.y+100 and hurt==0:
                    lifecount-=1
                    hurt=1
                    hurttime=timer
        if timer>1500 and timer<=2100:
            for i in range (0,10):
                pidultype3[i].update()
                if character.x+100>pidultype3[i].x-50 and character.x+100<pidultype3[i].x+75 and hurt==0:
                    if character.y+75<pidultype3[i].y and character.y+75>pidultype3[i].y-50:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
        if timer>2100 and timer <2900:
            pidultype4Bigbox.update()
            if timer>2200:
                for i in range(0,20):
                    if timer>2200+i*25 and timer<2400+i*100:
                        pidultype4Littlebox[i].update()

        if timer==2900:
            timer=data['title']['timer']
            pidul.x=data['pidul']['x']
            for i in range(0,5):
                pidultype1[i].x=random.randint(100,700)
                pidultype1[i].y=data['pidulbat']['y']
                pidultype1[i].frame=data['pidulbat']['frame']
                pidultype1[i].plusx=data['pidulbat']['plusx']
                pidultype1[i].plusy=data['pidulbat']['plusy']
            pidultype2.x==random.randint(100,700)
            hurt=data['title']['hurt']
            pidultype2.y=data['movedanger']['y']
            drainframe=data['title']['drainframe']
            pidultype4Bigbox.x=data['bigbox']['x']
            pidultype4Bigbox.y=data['bigbox']['y']
            for i in range(0,10):
                pidultype3[i].x=random.randint(100,700)
                pidultype3[i].y=random.randint(100,1000)+500
                pidultype3[i].angle=random.randint(0,360)
            for i in range(0,20):
                pidultype4Littlebox[i].x=520+random.randint(0,280)
                pidultype4Littlebox[i].y=data['littlebox']['y']
                pidultype4Littlebox[i].fall=25+random.randint(0,10)
            type=random.randint(0,5)%3
            while type==2:
                type=random.randint(0,5)%3

    delay(0.01)


def pause():
    pass


def resume():
    pass