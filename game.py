
from pico2d import *

import game_framework
import sys

sys.path.append('../LabsAll/Labs')

import random
import math
import json
import os





name = "MainState"
image = None



velx=0 #벨코즈 머리등장
pix=0;#피들스틱 머리등장
choq=0 #초가스 q 올라오는 y값

characterxr=False
characterxl=False

lifecount=2
hurt=0   #맞음
hurttime=0 #맞은 시간
timer=0
jump=False
jumpturn=False
running=True
characterx=0
charactery=0
type=random.randrange(0,3)%3


class Danger1:
    image =None

    def __init__(self):
        self.x, self.y =0,0
        self.frame=0
        if Danger1.image==None:
            Danger1.image = load_image('image\\danger.png')

    def update(self):
        global timer
        if timer%4==0:
            self.frame=(self.frame+1)%4


    def draw(self):
        global chotypeF, dangerline,timer
        if type==0:
            if timer<150 and timer>40:
                self.image.clip_draw(0,self.frame*50,800,50,400,150,800,200)
            if timer<400 and timer>300:
                self.image.clip_draw(0,self.frame*50,800,50,450,300,700,600)
            if timer<950 and timer>900:
                for i in range(0,7):
                    self.image.clip_draw(0,dangerline[i]*50,800,50,100+200*(chotypeF[i]%4),460-270*(chotypeF[i]//4),200,270)
                    if timer%4==0:
                        dangerline[i]=(dangerline[i]+1)%4
class Chogas:
    image =None

    def __init__(self):
        self.x, self.y =0,300
        if Chogas.image==None:
            Chogas.image = load_image('image\\chogas\\chogas.png')

    def update(self):
        if self.x>-400:
            self.x-=10

    def draw(self):
         self.image.draw(1100+self.x,self.y)#초가스 캐릭터


class Chotype1:
    image =None

    def __init__(self):
        self.x, self.y =0,0
        self.frame=0
        if Chotype1.image==None:
            Chotype1.image = load_image('image\\chogas\\chotype1.png')

    def update(self):
        global timer
        if timer%4==0:
            self.frame=(self.frame+1)%4
        self.y+=25-(timer-150)
    def draw(self):
        global timer,hurt,hurttime,charactery,lifecount
        if timer>150 and timer<300:
            self.image.draw(400,-50+self.y)
        if 75+charactery<self.y and hurt==0:
                lifecount-=1
                hurt=1
                hurttime=timer

class Chotype2:
    image =None

    def __init__(self):
        self.x, self.y =0,0
        self.frame=0
        self.check=0
        if Chotype2.image==None:
            Chotype2.image = load_image('image\\chogas\\chotype2.png')

    def update(self):
        global timer
        if timer%2==0 and self.frame<=7 and self.check==0:
            self.frame=(self.frame+1)
        if self.frame==8:
            self.check=1
        if self.check==1 and self.frame>0 and timer%2==0:
            self.frame=(self.frame-1)
    def draw(self):
        global timer,lifecount,hurt,lifecount,hurttime,characterx
        self.image.clip_draw(self.frame*100,0,100,100,450,325,700,500)

        if 100+characterx>800-(100*self.frame) and hurt==0:
            lifecount-=1
            hurt=1
            hurttime=timer

class Chotype3:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(0, 800), random.randint(100, 700)+600
        if Chotype3.image==None:
            Chotype3.image = load_image('image\\chogas\\chotype3.png')

    def update(self):
        self.y -=5

    def draw(self):
        global characterx,charactery,hurt,lifecount,hurttime,timer
        self.image.clip_draw(0, 0, 50, 100, self.x, self.y)

        if self.x-50<characterx+100 and self.x+50>characterx+100:
            if self.y>75+charactery and self.y-75<75+charactery and hurt==0:
                lifecount-=1
                hurt=1
                hurttime=timer

class Chotype4:
    image =None

    def __init__(self):
        if Chotype4.image==None:
            Chotype4.image = load_image('image\\chogas\\chotype4.png')

    def draw(self):
        global chotypeF,chotype4frame,chotypeF,characterx,charactery,lifecount,hurt,hurttime
        for i in range(0,7):
            self.image.clip_draw(chotype4frame[i]*100,0,100,100,100+200*(chotypeF[i]%4),460-270*(chotypeF[i]//4),200,270)
            if timer%4==0:
                chotype4frame[i]=(chotype4frame[i]+1)%8

            if 100+characterx<250+200*(chotypeF[i]%4) and 100+characterx>50+200*(chotypeF[i]%4) and hurt==0:
                if 75+charactery<560-270*(chotypeF[i]//4) and 75+charactery>290-270*(chotypeF[i]//4):
                    lifecount-=1
                    hurt=1
                    hurttime=timer
########

class Velkoz:
    image =None

    def __init__(self):
        self.x, self.y =0, 250
        if Velkoz.image==None:
            Velkoz.image = load_image('image\\velkoz\\velkoz.png')

    def update(self):
        if self.x>-500:
            self.x-=10

    def draw(self):
        self.image.draw(1100+self.x,self.y)#벨코즈 캐릭터



class Velkoztype1:
    image1=None
    image2=None
    image3=None
    danger=None

    def __init__(self):
        self.x, self.y =random.randint(1,7)*100,0
        self.movex=0
        self.timer=0
        self.frame=0
        self.dangerframe=0
        if Velkoztype1.danger==None:
            Velkoztype1.danger = load_image('image\\danger2.png')
        if Velkoztype1.image1==None:
            Velkoztype1.image1 = load_image('image\\velkoz\\velkoztype1-1.png')
        if Velkoztype1.image2==None:
            Velkoztype1.image2 = load_image('image\\velkoz\\velkoztype1-2.png')
        if Velkoztype1.image3==None:
            Velkoztype1.image3 = load_image('image\\velkoz\\velkoztype1-3.png')

    def update(self):
        global timer
        self.timer+=1
        if self.timer%8==0:
            self.frame=(self.frame+1)%4
        if self.timer==119:
                self.frame=0
        if self.timer==144:
                self.frame=0
        if self.timer>145 and self.timer<225:
                self.movex+=10
        if self.timer>50 and self.timer<120:
            if self.y<700:
                self.y+=10

        if self.timer%4==0 and self.timer<50:
            self.dangerframe=(self.dangerframe+1)%4

    def draw(self):
        global timer,hurt,hurttime,lifecount,characterx,charactery

        if self.timer>10 and self.timer<320:
            if self.timer<50:
                self.danger.clip_draw(self.dangerframe*100,0,100,800,self.x,300)

        if self.timer>50 and self.timer<120:
            self.image1.clip_draw(self.frame*100,0,100,100,self.x,800-self.y)

            if 100+characterx>self.x and 100+characterx<self.x+100 and hurt==0:
                if 75+charactery<800-self.y and 75+charactery>700-self.y:
                    lifecount-=1
                    hurt=1
                    hurttime=timer
        if self.timer>120 and self.timer<145:
            self.image2.clip_draw(self.frame*100,0,100,100,self.x,100)
            if timer%8==0:
                self.frame=(self.frame+1)%3

        if self.timer>145 and self.timer<225:
            self.image3.clip_draw(100,0,100,100,self.x+self.movex,100)
            self.image3.clip_draw(0,0,100,100,self.x-self.movex,100)
            if characterx+100>self.x+self.movex and characterx+100<100+self.x+self.movex and hurt==0:
                if charactery+75<100:
                    lifecount-=1
                    hurt=1
                    hurttime=timer
            if characterx+100>self.x-self.movex and characterx+100<100+self.x-self.movex and hurt==0:
                if charactery+75<100:
                    lifecount-=1
                    hurt=1
                    hurttime=timer

class Velkoztype2:
    image1=None
    image2=None

    def __init__(self):
        self.downx, self.downy =0,0
        self.frame=0

        if Velkoztype2.image1==None:
            Velkoztype2.image1 = load_image('image\\velkoz\\velkoztype2-2.png')
        if Velkoztype2.image2==None:
            Velkoztype2.image2 = load_image('image\\velkoz\\velkoztype2-1.png')
    def update(self):
        global hurt,charactery,lifecount,hurt,hurttime,timer
        if timer>320 and timer<600:
            if 875+self.downy  >525:
                self.downy -=50

            if charactery+75>250 and hurt==0:
                    lifecount-=1
                    hurt=1
                    hurttime=timer
            if timer%8==0:
                self.frame=(self.frame+1)%8
            if timer ==390 or timer==453 or timer==517:
                self.frame=0
    def draw(self):
        global timer,jump,characterx
        self.image1.draw(400,875+self.downy,800,600)

        if (timer>325 and timer<=389) or (timer>453 and timer<=517):
            self.image2.clip_draw(100*self.frame,0,100,100,50,10)
            self.image2.clip_draw(100*self.frame,0,100,100,250,10)
            self.image2.clip_draw(100*self.frame,0,100,100,450,10)
            self.image2.clip_draw(100*self.frame,0,100,100,650,10)

            if timer==389:
                if characterx+75>150 and characterx+75<250:
                    jump=1
                if characterx+75>350 and characterx+75<450:
                    jump=1
                if characterx+75>550 and characterx+75<650:
                    jump=1
                if characterx+75>750 and characterx+75<850:
                    jump=1
        if (timer>389 and timer<=453) or (timer>517 and timer<=581):
            self.image2.clip_draw(100*self.frame,0,100,100,150,10)
            self.image2.clip_draw(100*self.frame,0,100,100,350,10)
            self.image2.clip_draw(100*self.frame,0,100,100,550,10)
            self.image2.clip_draw(100*self.frame,0,100,100,750,10)
            if timer==453:
                if characterx+75>50 and characterx+75<150:
                    jump=1
                if characterx+75>250 and characterx+75<350:
                    jump=1
                if characterx+75>450 and characterx+75<550:
                    jump=1
                if characterx+75>650 and characterx+75<750:
                    jump=1

class Velkoztype3:
    sandglass =None
    beam=None

    def __init__(self):
        self.sandglassx, self.sandglassy =random.randint(50,750),random.randint(120,400)
        self.x,self.y=0,random.randint(-90,300)
        if Velkoztype3.beam==None:
            Velkoztype3.beam = load_image('image\\velkoz\\velkoztype3-1.png')
        if Velkoztype3.sandglass==None:
            Velkoztype3.sandglass = load_image('image\\velkoz\\velkoztype3-2.png')

    def update(self):
        global timer,characterx,charactery,freeze,hurt
        if timer>600 and timer<700:
            if characterx+100>self.sandglassx-50 and characterx+100<self.sandglassx+50:
                if charactery+75<self.sandglassy+30 and charactery+75>self.sandglassy-70:
                    freeze=1
                    hurt=-1
    def draw(self):
        if timer>600 and timer<700:
            self.sandglass.clip_draw(0, 0, 100,100 , self.sandglassx, self.sandglassy)
        else:
            self.beam.clip_draw(0, 0, 1800,600 , self.x, self.y)

class Pidul:
    image =None

    def __init__(self):
        self.x, self.y =0,0
        if Pidul.image==None:
            Pidul.image = load_image('image\\pidul\\pidul.png')


    def update(self):
        if self.x>-500:
            self.x-=10


    def draw(self):
        self.image.draw(950+self.x,250)


class Pidulbat:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),550
        self.frame=0
        self.plusx=5
        self.plusy=5
        if Pidulbat.image==None:
            Pidulbat.image = load_image('image\\pidul\\pidul bat.png')

    def update(self):
        global characterx,charactery,lifecount,hurt,hurttime

        self.x-=self.plusx
        self.y-=self.plusy

        if self.x<50:
            self.plusx*=-1
        if self.x>750:
            self.plusx*=-1
        if self.y>550:
            self.plusy*=-1
        if self.y<110:
            self.plusy*=-1

        if self.plusx>0:
            if self.plusy>0:
                self.frame=0
            else:
                self.frame=3
        else:
            if self.plusy>0:
                self.frame=1
            else:
                self.frame=2

        if characterx+100>self.x-50 and characterx+100<self.x+50 and hurt==0:
            if charactery+75<self.y and charactery+75>self.y-100:
                lifecount-=1
                hurt=1
                hurttime=timer

    def draw(self):
        self.image.clip_draw(100*self.frame, 0, 100,100 , self.x, self.y)

class Movedanger:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),110
        self.frame=0
        if Movedanger.image==None:
            Movedanger.image = load_image('image\\danger.png')
    def update(self):
        global timer,characterx,charactery
        self.frame=(self.frame+1)%4
        if characterx+100>self.x:
            self.x+=15
        elif characterx+100<self.x-50:
            self.x-=15
        if charactery+75>self.y:
            self.y+=15
        else:
            self.y-=15


    def draw(self):
        self.image.clip_draw(0, 50*self.frame, 300,50 , self.x, self.y,100,100)

class Swingbat:
    image =None

    def __init__(self):
        self.x, self.y =random.randint(100,700),random.randint(100,1000)+500
        self.angle=random.randint(0,360)
        if Swingbat.image==None:
            Swingbat.image = load_image('image\\pidul\\swing bat.png')
    def update(self):
        self.angle+=2
        self.x+=10*math.cos(math.pi*(self.angle/180))
        self.y-=3


    def draw(self):
        self.image.clip_draw(0,0, 100,50 , self.x, self.y)


class Bigbox:
    image =None

    def __init__(self):
        self.x, self.y =600,500
        if Bigbox.image==None:
            Bigbox.image = load_image('image\\pidul\\big box.png')

    def update(self):
        global lifecount,hurt,hurttime,characterx,charactery
        if self.y>200:
            self.y-=50
        if characterx+100>self.x-150 and characterx+100<self.x+300 and \
                                charactery+75>self.y-150 and charactery+75<self.y and hurt==0:
            lifecount-=1
            hurt=1
            hurttime=timer

    def draw(self):
        self.image.clip_draw(0,0, 400,300 , self.x, self.y)

class Littlebox:
    image =None

    def __init__(self):
        self.x, self.y =520+random.randint(0,280),210
        self.fall=25+random.randint(0,10)
        if Littlebox.image==None:
            Littlebox.image = load_image('image\\pidul\\little box.png')

    def update(self):
        global characterx, charactery, hurt,hurttime,lifecount
        self.fall-=1
        self.y+=self.fall
        self.x-=7

        if characterx+100>self.x-60 and characterx+100<self.x+50 and  hurt==0:
            if charactery+75<self.y+50 and charactery+75>self.y-50  :
                lifecount-=1
                hurt=1
                hurttime=timer

    def draw(self):
        self.image.clip_draw(0,0, 100,100 , self.x, self.y)



dangerline=[0]*7#초가스 r danger 깜빡이는 프레임
count=0
mousex=0
mousey=0
freeze=0


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

def enter():#안되면 되게해라-앞의 변수 전역 global
    global ground,gameback,life,pidul,character,title
    global chogas,chotype1,chotype2,chotype4,danger,team,chotypeF,checktype4,chotype4frame,chotype3
    global velkoz,danger2,velkozr,velkoztype3,velkoztype1,velkoztype2
    global pidulbat,movedanger,drain,drainframe,fear,swingbat, bigbox, littlebox

    ground = load_image('image\\ground.png')
    gameback = load_image('image\\gameback.png')
    life=load_image('image\\life.png')#생명
    character=load_image('image\\character.png')
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
    movedanger=Movedanger()
    pidulbat=[Pidulbat() for i in range(5)]#튕기는 박쥐 5마리
    chotypeF= [0] * 7
    checktype4=[0]*7
    chotype4frame=[0]*7
    drainframe=0
    bigbox=Bigbox()
    littlebox=[Littlebox() for i in range(20)]
    swingbat=[Swingbat() for i in range(10)]



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
    global mainscreen,freeze
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
                    if not(type==2 and timer>1500 and timer<2100):
                        characterxr=True
                    else:
                        characterxl=True
                if event.key==SDLK_LEFT:
                    if not(type==2 and timer>1500 and timer<2100):
                        characterxl=True
                    else:
                        characterxr=True
                if event.key==SDLK_RETURN:
                    mainscreen=True
            elif event.type==SDL_KEYUP:
                if event.key==SDLK_RIGHT:
                    if not(type==2 and timer>1500 and timer<2100):
                        characterxr=False
                    else:
                        characterxl=False

                if event.key==SDLK_LEFT:
                    if not(type==2 and timer>1500 and timer<2100):
                        characterxl=False
                    else:
                        characterxr=False
        if freeze==1:
            characterxr=False
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
    global timer,lifecount,hurt,type,hurttime,life,character,ground,jump
    global chogas,danger,chotype1,chotype2, chotype3,chotype4,team
    global velkoz,velkoztype1,velkoztype3,danger2,freeze
    global pidul,pidulbat,pidulbatteam,drainframe,movedanger,drain,bigbox,littlebox
    gameback.draw(400,300)#검은 배경

    if type==0:
        timer+=1
        chogas.update()
        chogas.draw()
        if timer<150 and timer>40:
            danger.update()
            danger.draw()
        if timer>150 and timer<=300: #기술 등장
            chotype1.update()
            chotype1.draw()
        if timer>300 and timer<=400:
            danger.update()
            danger.draw()

        if timer>400 and timer<550:  #w 완료
            chotype2.update()
            chotype2.draw()

        if timer>550 and timer<900:#초가스e시작
            for chotype3 in team:
                chotype3.update()
                chotype3.draw()


        if timer>=900:   #초가스 r 시작
            for i in range(0,7):
                if chotypeF[i]==0 and checktype4[i]==0:
                    chotypeF[i]=random.randint(0,7)
                    for j in range(0,i-1):
                        if chotypeF[i]==chotypeF[j]:
                            chotypeF[i]=random.randint(0,7)
                checktype4[i]=1

            if timer<950:
                danger.update()
                danger.draw()

            if timer>950 and timer<980 :
                    chotype4.draw()

        if hurt==1 and timer>=hurttime+100:
            hurt=0
        if timer ==1080:
            timer=0
            type=random.randint(0,3)%3
            while type==0:
                type=random.randint(0,3)%3
            for i in range(0,7):
                chotype4frame[i]=0
                chotypeF[i]=random.randint(0,7)
            hurt=0
            chogas.x=0
            chotype1.y=0
            chotype2.x, chotype2.y =0,0
            chotype2.frame=0
            chotype2.check=0
            for i in range(0,30):
                team[i].x=random.randint(0, 800)
                team[i].y= random.randint(100, 700)+600




    if type==1:
        timer+=1
        velkoz.update()
        velkoz.draw()

        if hurt==1 and timer>=hurttime+100:
            hurt=0

        if timer>10 and timer<320:
            velkoztype1[0].update()
            velkoztype1[0].draw()
        if timer>30 and timer<320:
            velkoztype1[1].update()
            velkoztype1[1].draw()
        if timer>50 and timer<320:
            velkoztype1[2].update()
            velkoztype1[2].draw()
        if timer>70 and timer<320:
            velkoztype1[3].update()
            velkoztype1[3].draw()
        if timer>90 and timer<320:
            velkoztype1[4].update()
            velkoztype1[4].draw()

        ground.draw(400,300)

        if timer>320 and timer<600:
            velkoztype2.update()
            velkoztype2.draw()

        if timer>600 and timer<700:
            velkoztype3[0].update()
            velkoztype3[0].draw()

        if timer>=700 and timer<1340:
            for i in range(0,30):
                if timer>700+(20*i) and timer<720+(20*i):
                    velkoztype3[i].draw()
                    if charactery+75<velkoztype3[i].y+200+100 and charactery+75>velkoztype3[i].y-100+200 and hurt==0:#충돌체크 조금만 더
                        lifecount-=1
                        hurt=1
                        hurttime=timer
            if timer>1320:
                freeze=0

        if timer>1340:
            timer=0
            type=random.randint(0,5)%3
            while type==1:
                type=random.randint(0,5)%3
            hurt=0
            velkoz.x=0
            for i in range(0,5):
                velkoztype1[i].x, velkoztype1[i].y =random.randint(1,7)*100,0
                velkoztype1[i].movex=0
                velkoztype1[i].timer=0
                velkoztype1[i].frame=0
                velkoztype1[i].dangerframe=0
            velkoztype2.downx, velkoztype2.downy =0,0
            velkoztype2.frame=0
            for i in range(0,30):
                velkoztype3[i].sandglassx, velkoztype3[i].sandglassy =random.randint(50,750),random.randint(120,400)
                velkoztype3[i].x,velkoztype3[i].y=0,random.randint(-90,300)



    if type==2:
        timer+=1
        pidul.update()
        pidul.draw()
        if hurt==1 and timer>=hurttime+100:
            hurt=0
        if timer>100:
            for i in range(0,5):
                if timer>100+i*100 and timer<600+i*100:
                    pidulbat[i].update()
                    pidulbat[i].draw()


        if timer>1000 and timer<1500:
            if timer%4==0 and timer<1200:
                movedanger.update()
            if timer<1200:
                movedanger.draw()
            if timer>1200:
                drain.clip_draw(800*drainframe,0,800,800,movedanger.x+300,movedanger.y+300)
                if timer%4==0:
                    drainframe=(drainframe+1)%8
                if characterx+100>movedanger.x-75 and characterx+100<movedanger.x+150 and charactery+75>movedanger.y-50 and hurt==0:
                    lifecount-=1
                    hurt=1
                    hurttime=timer
        if timer>1500 and timer<2100:
            fear.draw(characterx+100,charactery+125,100,100)
            for i in range (0,10):
                swingbat[i].update()
                swingbat[i].draw()

                if characterx+100>swingbat[i].x-50 and characterx+100<swingbat[i].x+75 and hurt==0:
                    if charactery+75<swingbat[i].y and charactery+75>swingbat[i].y-50:
                        lifecount-=1
                        hurt=1
                        hurttime=timer
        if timer>2100 and timer <2900:
            bigbox.update()
            bigbox.draw()

            if timer>2200 :
                for i in range(0,20):
                    if timer>2200+i*25 and timer<2400+i*100:
                        littlebox[i].update()
                        littlebox[i].draw()



        if timer==2900:
            timer=0
            pidul.x=0
            for i in range(0,5):
                pidulbat[i].x=random.randint(100,700)
                pidulbat[i].y=550
                pidulbat[i].frame=0
                pidulbat[i].plusx=5
                pidulbat[i].plusy=5
            movedanger.x==random.randint(100,700)
            movedanger.y=110
            drainframe=0
            bigbox.x=600
            bigbox.y=500
            for i in range(0,10):
                swingbat[i].x=random.randint(100,700)
                swingbat[i].y=random.randint(100,1000)+500
                swingbat[i].angle=random.randint(0,360)
            for i in range(0,20):
                littlebox[i].x=520+random.randint(0,280)
                littlebox[i].y=210
                littlebox[i].fall=25+random.randint(0,10)
            type=random.randint(0,3)%3
            while type==2:
                type=random.randint(0,3)%3


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