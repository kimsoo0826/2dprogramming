import sys
sys.path.append('../LabsAll/Labs')

import random
import json
import os
import game_framework
from pico2d import *
import game


name = "Title"
image = None
bgm=None

def enter():
    global image,bgm
    open_canvas()
    image=load_image('image\\title.png')
    bgm=load_music('bgm\\ans.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image,bgm
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
                bgm.stop()
                game_framework.push_state(game)




def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass