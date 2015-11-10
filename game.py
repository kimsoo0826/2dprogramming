
from pico2d import *

import game_framework
import sys

sys.path.append('../LabsAll/Labs')

import random
import json
import os





name = "MainState"
image = None


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
timer=700
wcheck=0
jump=False
jumpturn=False
running=True
characterx=0
charactery=0
type= 1 #random.randrange(1,3)%3
count=0;
four=4

class Chotype3:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(0, 800), random.randint(100, 700)+600
        if Chotype3.image==None:
            Chotype3.image = load_image('image\\chogas\\chotype3.png')

    def update(self):
        self.y -=5

    def draw(self):
        self.image.clip_draw(0, 0, 50, 100, self.x, self.y)
class Velkozr:
    image =None

    def __init__(self):
        self.x, self.y =0,random.randint(-90,300)
        if Velkozr.image==None:
            Velkozr.image = load_image('image\\velkoz\\velkoz r.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1800,600 , self.x, self.y)

dangerframe=0 #위험 프레임\
dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
act=0#초가스r을 움직이기 위해 모든 랜덤값 6개를 다른 숫자로
count=0
wframe=0 #초가스 w 프레임
mousex=0
mousey=0
velq=[0]*3
velqframe=[0]*3
velwframe=0
velqy=[0]*3
velqx=[0]*3
velw2y=0


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

def enter():#ㅅㅂ 안되면 되게해라-앞의 변수 전역 global
    global image
    global ground,gameback,life,cho,vel,pi,chotype1,chotype2,chotype4,danger,character,title,team,chotypeF,checktype4,chotype4frame,chotype3
    global danger2,velq1,velq2,velq3,velqframe,velw1,velw2,velw2y,velkozr,velteam
    #open_canvas()
    ground = load_image('image\\ground.png')
    gameback = load_image('image\\gameback.png')
    life=load_image('image\\life.png')#생명
    cho=load_image('image\\chogas\\chogas.png')#초가스 등장모습
    vel=load_image('image\\velkoz\\velkoz.png')#벨코즈 등장모습
    pi=load_image('image\\pidul\\pidul.png')#피들스틱 등장모습
    chotype1=load_image('image\\chogas\\chotype1.png')#초가스 첫번째 스킬
    chotype2=load_image('image\\chogas\\chotype2.png')#초가스 두번째 스킬)
    chotype4=load_image('image\\chogas\\chotype4.png')#초가스 네번째 스킬
    velq1=load_image('image\\velkoz\\velkozq.png')#벨코즈 첫번째 스킬
    velq2=load_image('image\\velkoz\\velkozq2.png')#벨코즈 첫번째 스킬
    velq3=load_image('image\\velkoz\\velkozq3.png')#벨코즈 첫번째 스킬
    velw1=load_image('image\\velkoz\\velkozw.png')#벨코즈 두번째 스킬
    velw2=load_image('image\\velkoz\\velkoz w down.png')#벨코즈 두번째 스킬
    danger=load_image('image\\danger.png')
    danger2=load_image('image\\danger2.png')
    character=load_image('image\\character.png')

    velkozr=Velkozr()
    chotype3=Chotype3()
    team = [Chotype3() for i in range(30)] #초가스 e 개수
    velteam=[Velkozr() for i in range(30)]
    chotypeF= [0] * 7
    checktype4=[0]*7
    chotype4frame=[0]*7



def exit():
    global image
    del(image)


def handle_events():
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
            if event.key==SDLK_ESCAPE:
                game_framework.quit()
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



def draw():
    clear_canvas()
    global gameback
    global timer
    global cho,chox,danger,dangerframe
    global chotype1,choq,lifecount,hurt,chotype2,wframe,wcheck,chotype4,velx,vel,pix,pi,character,ground,lifecount,life,type,hurttime,danger2
    global velq,velq1,velq2,velq3,velqframe,velqx,velqy,velw1,velw2y,velwframe,jump,velteam,velkozr
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



        if timer>550 and timer<900:#초가스e시작
            for chotype3 in team:
                chotype3.update()
                chotype3.draw()

                if chotype3.x-50<characterx+100 and chotype3.x+50>characterx+100:
                    if chotype3.y>75+charactery and chotype3.y-75<75+charactery and hurt==0:
                        lifecount-=1
                        hurt=1
                        hurttime=timer


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
        timer+=1
        vel.draw(1100+velx,250)#벨코즈 캐릭터
        if velx>-500:
            velx-=10
        if hurt==1 and timer>=hurttime+100:
            hurt=0
        if timer==5:
            while velq[0]==velq[1] or velq[0]==velq[2] or velq[1]==velq[2]:
                for i in range(0,3):
                    velq[i]=random.randint(0,7)*100

        if timer>10 and timer<320:
            if timer<50:
                danger2.clip_draw(dangerframe*100,0,100,800,velq[0],300)
                if timer%4==0:
                    dangerframe=(dangerframe+1)%4
            if timer>50 and timer<120:
                if velqy[0]<700:
                    velqy[0]+=10
                velq1.clip_draw(velqframe[0]*100,0,100,100,velq[0],800-velqy[0])
                if timer%8==0:
                    velqframe[0]=(velqframe[0]+1)%4
                if timer==119:
                    velqframe[0]=0
                if 100+characterx>velq[0] and 100+characterx<velq[0]+100 and hurt==0:
                    if 75+charactery<800-velqy[0] and 75+charactery>700-velqy[0]:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
            if timer>120 and timer<145:
                if timer==144:
                    velqframe[0]=0
                velq2.clip_draw(velqframe[0]*100,0,100,100,velq[0],100)
                if timer%8==0:
                    velqframe[0]=(velqframe[0]+1)%3

            if timer>145 and timer<225:
                velqx[0]+=10
                velq3.clip_draw(100,0,100,100,velq[0]+velqx[0],100)
                velq3.clip_draw(0,0,100,100,velq[0]-velqx[0],100)
                if characterx+100>velq[0]+velqx[0] and characterx+100<100+velq[0]+velqx[0] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
                if characterx+100>velq[0]-velqx[0] and characterx+100<100+velq[0]-velqx[0] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer

        if timer>50 and timer<320:
            if timer<90:
                danger2.clip_draw(dangerframe*100,0,100,800,velq[1],300)
                if timer%4==0:
                    dangerframe=(dangerframe+1)%4
        if timer>90 and timer<160:
                if velqy[1]<700:
                    velqy[1]+=10
                velq1.clip_draw(velqframe[1]*100,0,100,100,velq[1],800-velqy[1])
                if timer%8==0:
                    velqframe[1]=(velqframe[1]+1)%4
                if timer==159:
                    velqframe[1]=0
                if 100+characterx>velq[1] and 100+characterx<velq[1]+100 and hurt==0:
                    if 75+charactery<800-velqy[1] and 75+charactery>700-velqy[1]:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
        if timer>160 and timer<185:
            if timer==184:
                velqframe[1]=0
            velq2.clip_draw(velqframe[1]*100,0,100,100,velq[1],100)
            if timer%8==0:
                velqframe[1]=(velqframe[1]+1)%3
        if timer>185 and timer<265:
                velqx[1]+=10
                velq3.clip_draw(100,0,100,100,velq[1]+velqx[1],100)
                velq3.clip_draw(0,0,100,100,velq[1]-velqx[1],100)
                if characterx+100>velq[1]+velqx[1] and characterx+100<100+velq[1]+velqx[1] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
                if characterx+100>velq[1]-velqx[1] and characterx+100<100+velq[1]-velqx[1] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer

        if timer>100 and timer<320:
            if timer<140:
                danger2.clip_draw(dangerframe*100,0,100,800,velq[2],300)
                if timer%4==0:
                    dangerframe=(dangerframe+1)%4
            if timer>140 and timer<210:
                if velqy[2]<700:
                    velqy[2]+=10
                velq1.clip_draw(velqframe[2]*100,0,100,100,velq[2],800-velqy[2])
                if timer%8==0:
                    velqframe[2]=(velqframe[2]+1)%4
                if timer==209:
                    velqframe[2]=0
                if 100+characterx>velq[2] and 100+characterx<velq[2]+100 and hurt==0:
                    if 75+charactery<800-velqy[2] and 75+charactery>700-velqy[2]:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
            if timer>210 and timer<235:
                if timer==234:
                    velqframe[2]=0
                velq2.clip_draw(velqframe[2]*100,0,100,100,velq[2],100)
                if timer%8==0:
                    velqframe[2]=(velqframe[2]+1)%3
            if timer>235 and timer<315:
                velqx[2]+=10
                velq3.clip_draw(100,0,100,100,velq[2]+velqx[2],100)
                velq3.clip_draw(0,0,100,100,velq[2]-velqx[2],100)
                if characterx+100>velq[2]+velqx[2] and characterx+100<100+velq[2]+velqx[2] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
                if characterx+100>velq[2]-velqx[2] and characterx+100<100+velq[2]-velqx[2] and hurt==0:
                    if charactery+75<100:
                        lifecount-=1
                        hurt=1
                        hurttime=timer


        ground.draw(400,300)

        if timer>320 and timer<650:
            if 875+velw2y >525:
                velw2y-=50
            velw2.draw(400,875+velw2y,800,600)

            if charactery+75>250 and hurt==0:
                lifecount-=1
                hurt=1
                hurttime=timer

            if timer>325 and timer<=389:
                velw1.clip_draw(100*velwframe,0,100,100,50,10)
                velw1.clip_draw(100*velwframe,0,100,100,250,10)
                velw1.clip_draw(100*velwframe,0,100,100,450,10)
                velw1.clip_draw(100*velwframe,0,100,100,650,10)
                if timer%8==0:
                    velwframe=(velwframe+1)%8
                if timer==389:
                    if characterx+75>150 and characterx+75<250:
                        jump=1
                    if characterx+75>350 and characterx+75<450:
                        jump=1
                    if characterx+75>550 and characterx+75<650:
                        jump=1
                    if characterx+75>750 and characterx+75<850:
                        jump=1





            if timer>389 and timer<=453:
                if timer ==390:
                    velwframe=0
                velw1.clip_draw(100*velwframe,0,100,100,150,10)
                velw1.clip_draw(100*velwframe,0,100,100,350,10)
                velw1.clip_draw(100*velwframe,0,100,100,550,10)
                velw1.clip_draw(100*velwframe,0,100,100,750,10)
                if timer%8==0:
                    velwframe=(velwframe+1)%8
                if timer==453:
                    if characterx+75>50 and characterx+75<150:
                        jump=1
                    if characterx+75>250 and characterx+75<350:
                        jump=1
                    if characterx+75>450 and characterx+75<550:
                        jump=1
                    if characterx+75>650 and characterx+75<750:
                        jump=1

            if timer>453 and timer<=517:
                if timer ==453:
                    velwframe=0
                velw1.clip_draw(100*velwframe,0,100,100,50,10)
                velw1.clip_draw(100*velwframe,0,100,100,250,10)
                velw1.clip_draw(100*velwframe,0,100,100,450,10)
                velw1.clip_draw(100*velwframe,0,100,100,650,10)
                if timer%8==0:
                    velwframe=(velwframe+1)%8
                if timer==517:
                    if characterx+75>150 and characterx+75<250:
                        jump=1
                    if characterx+75>350 and characterx+75<450:
                        jump=1
                    if characterx+75>550 and characterx+75<650:
                        jump=1
                    if characterx+75>750 and characterx+75<850:
                        jump=1

            if timer>517 and timer<=581:
                if timer ==517:
                    velwframe=0
                velw1.clip_draw(100*velwframe,0,100,100,150,10)
                velw1.clip_draw(100*velwframe,0,100,100,350,10)
                velw1.clip_draw(100*velwframe,0,100,100,550,10)
                velw1.clip_draw(100*velwframe,0,100,100,750,10)
                if timer%8==0:
                    velwframe=(velwframe+1)%8
                if timer==581:
                    if characterx+75>50 and characterx+75<150:
                        jump=1
                    if characterx+75>250 and characterx+75<350:
                        jump=1
                    if characterx+75>450 and characterx+75<550:
                        jump=1
                    if characterx+75>650 and characterx+75<750:
                        jump=1
        if timer>=700:
            for i in range(0,30):
                if timer>700+(20*i) and timer<720+(20*i):
                    velteam[i].draw()
                    if charactery+75<velteam[i].y+200 and charactery+75>velteam[i].y-100+200 and hurt==0:#충돌체크 조금만 더
                        lifecount-=1
                        hurt=1
                        hurttime=timer












    if type==2:
        pi.draw(950+pix,250)#피들스틱 캐릭터
        if pix>-500:
            pix-=10

    if hurt==0:
        character.draw(100+characterx,75+charactery,50,40)
    if hurt==1:
        if timer%6==0:
            character.draw(100+characterx,75+charactery,50,40)
    if type!=1:
       ground.draw(400,300) #땅




    life.clip_draw(266*lifecount,0,266,600,150,560,300,200)

    update_canvas()




def update():
    delay(0.01)


def pause():
    pass


def resume():
    pass