import pgzrun
import random

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X,CENTER_Y)
TITLE = 'Recycle choice'
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ['bottle','bag','chips','battery']

game_over = False
game_comp = False
current_level = 1
items = []
animations = []

def draw():
    screen.clear()
    screen.blit('bg',(0,0))

def update():
    pass

pgzrun.go()