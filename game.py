import sys
sys.path.append('../LabsAll/Labs')

import random
import json
import os

from pico2d import *

import game_framework
import title



name = "MainState"
class Chotype3:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(0, 800), random.randint(100, 700)+600
        if Chotype3.image==None:
            Chotype3.image = load_image('chotype3.png')

    def update(self):
        self.y -=5

    def draw(self):
        self.image.clip_draw(0, 0, 50, 100, self.x, self.y)

def handle_events(): #방향키 적용
    global running
    global characterxr
    global characterxl
    global characterx
    global charactery
    global jump
    global jumpturn
    global count
    global mousex
    global mousey
    global mainscreen
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_SPACE:
                 jump+=1
            if event.key==SDLK_RIGHT:
                characterxr=True
            if event.key==SDLK_LEFT:
                characterxl=True
            if event.key==SDLK_RETURN:
                mainscreen=True
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                characterxr=False
            if event.key==SDLK_LEFT:
                characterxl=False
    if characterxr==True:
        if characterx <= 680:
            characterx+=5
    if characterxl==True:
        if characterx >=-80:
            characterx-=5
    if jump!=0 and jump!=2:
        charactery+=20-count
        count+=1
        if(charactery<=0):
            count=0
            charactery=0
            jump=0
    if jump==2:
        jumpturn=True
    if jumpturn==True:
        count=0
        jumpturn=False
        jump+=1

open_canvas()
ground = load_image('ground.png')
gameback = load_image('gameback.png')
life=load_image('life.png')#생명
cho=load_image('chogas.png')#초가스 등장모습
vel=load_image('velkoz.png')#벨코즈 등장모습
pi=load_image('pidul.png')#피들스틱 등장모습
chotype1=load_image('chotype1.png')#초가스 첫번째 스킬
chotype2=load_image('chotype2.png')#초가스 두번째 스킬)
chotype4=load_image('chotype4.png')
danger=load_image('danger.png')
character=load_image('character.png')
title=load_image('title.png')


chox=0 #초가스 머리등장
velx=0 #벨코즈 머리등장
pix=0;#피들스틱 머리등장
choq=0 #초가스 q 올라오는 y값

characterxr=False
characterxl=False
mainscreen=True
lifecount=2
hurt=0   #맞음
hurttime=0 #맞은 시간
timer=0
wcheck=0
jump=False
jumpturn=False
running=True
characterx=0
charactery=0
type= 0 #random.randrange(1,3)%3
count=0;
four=4



dangerframe=0 #위험 프레임\
dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
act=0#초가스r을 움직이기 위해 모든 랜덤값 6개를 다른 숫자로
count=0
wframe=0 #초가스 w 프레임
team = [Chotype3() for i in range(30)] #초가스 e 개수
chotypeF= [0] * 7
checktype4=[0]*7
chotype4frame=[0]*7
mousex=0
mousey=0
chotype3=Chotype3()

while(running):
    handle_events()

    clear_canvas()
    if(mainscreen==False):
        title.draw(400,300)
    if(mainscreen==True):
        gameback.draw(400,300)#검은 배경
        if type==0:
            timer+=1
            cho.draw(1100+chox,300)#초가스 캐릭터
            if chox>-400:
                chox-=10
            if timer<150 and timer>40: #첫번째 경고
                danger.clip_draw(0,dangerframe*50,800,50,400,150,800,200)
                if timer%4==0:
                    dangerframe=(dangerframe+1)%4
            if timer>150 and timer<=300: #기술 등장
                chotype1.draw(400,-50+choq)  #최대높이 350 가려지는 높이 -50
                choq+=25-(timer-150)

                if 75+charactery<choq and hurt==0:
                    lifecount-=1
                    hurt=1
                    hurttime=timer

                if hurt==1 and timer==hurttime+100:
                    hurt=0



            if timer>300 and timer<=400:
                danger.clip_draw(0,dangerframe*50,800,50,450,300,700,600)
                if timer%4==0:
                    dangerframe=(dangerframe+1)%4

            if timer>400 and timer<550:  #w 완료
                #chotype2.clip_draw(0,0,800,600,400,300)
                chotype2.clip_draw(wframe*100,0,100,100,450,325,700,500)
                if timer%2==0 and wframe<=7 and wcheck==0:
                    wframe=(wframe+1)
                if wframe==8:
                    wcheck=1
                if wcheck==1 and wframe>0 and timer%2==0:
                    wframe=(wframe-1)

                if 100+characterx>800-(100*wframe) and hurt==0:
                    lifecount-=1
                    hurt=1
                    hurttime=timer

                if hurt==1 and timer>=hurttime+100:
                    hurt=0

            if timer>550 and timer<900:#초가스e시작
                for chotype3 in team:
                    chotype3.update()
                    chotype3.draw()

                    if chotype3.x-50<characterx+100 and chotype3.x+50>characterx+100:
                        if chotype3.y>75+charactery and chotype3.y-75<75+charactery and hurt==0:
                            lifecount-=1
                            hurt=1
                            hurttime=timer

                    if hurt==1 and timer>=hurttime+100:
                        hurt=0
            if timer>=900:   #초가스 r 시작
                for i in range(0,7):
                    if chotypeF[i]==0 and checktype4[i]==0:
                        chotypeF[i]=random.randint(0,7)
                        for j in range(0,i-1):
                            if chotypeF[i]==chotypeF[j]:
                                chotypeF[i]=random.randint(0,7)
                    checktype4[i]=1

                if timer<950:
                    for i in range(0,7):
                         danger.clip_draw(0,dangerline[i]*50,800,50,100+200*(chotypeF[i]%4),460-270*(chotypeF[i]//4),200,270)
                         if timer%4==0:
                            dangerline[i]=(dangerline[i]+1)%4

                if timer>950 and timer<980 :


                    for i in range(0,7):
                        chotype4.clip_draw(chotype4frame[i]*100,0,100,100,100+200*(chotypeF[i]%4),460-270*(chotypeF[i]//4),200,270)
                        if timer%4==0:
                            chotype4frame[i]=(chotype4frame[i]+1)%8

                    for i in range(0,7):#초가스 r 충돌체크
                        if 100+characterx<250+200*(chotypeF[i]%4) and 100+characterx>50+200*(chotypeF[i]%4) and hurt==0:
                            if 75+charactery<560-270*(chotypeF[i]//4) and 75+charactery>290-270*(chotypeF[i]//4) and hurt==0:
                                lifecount-=1
                                hurt=1
                                hurttime=timer
                if hurt==1 and timer>=hurttime+100:
                    hurt=0
                if timer ==1080:
                    timer=0
                    type=random.randint(1,2)
                    hurt=0



        if type==1:
            vel.draw(1100+velx,250)#벨코즈 캐릭터(
            if velx>-500:
                velx-=10
        if type==2:
            pi.draw(950+pix,250)#피들스틱 캐릭터
            if pix>-500:
                pix-=10

        if hurt==0:
            character.draw(100+characterx,75+charactery,50,40)
        if hurt==1:
            if timer%6==0:
                character.draw(100+characterx,75+charactery,50,40)

        ground.draw(400,300) #땅


        life.clip_draw(266*lifecount,0,266,600,150,560,300,200)



    update_canvas()
    delay(0.01)


close_canvas()