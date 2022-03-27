# importing libraries
import pygame
import time
import random
from sys import exit
import numpy as np
import random

#_____________________________________________________________________________#
#                                                                             #
#--------------------------   CHANGEABLE SETTINGS   --------------------------#
#_____________________________________________________________________________#
fps_speed = 60

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

shoot_delay = 10
bullet_speed = 3
player_speed = 2
enemy_speed = 2
maximum_enemys = 100
spawnChance = 1 #Works as procent up to 100. Tries to spawn each render cycle

fullscreen = False
window_x, window_y = (600,600)
#------------------------------------------------------------------------------#

if fullscreen: 
    window_x, window_y = pygame.display.set_mode().get_size()
    game_window = pygame.display.set_mode((window_x, window_y))
else: game_window = pygame.display.set_mode((window_x, window_y), pygame.RESIZABLE)

up    = False
down  = False
right = False
left  = False

bullet_list=[]
enemy_list=[]
small_window_x, small_window_y = window_x, window_y
pygame.init()
pygame.display.set_caption('Ett spel, I guess')
fps = pygame.time.Clock()



print("Window size:",window_x,"X",window_y)

def randId(array,IdPos):
    Id = random.randrange(1,10000)
    same = True

    while same:
        existed=False
        for exists in array:
            if exists[IdPos] == Id:
                Id = random.randrange(1,10000)
                existed=True
        if not existed: same=False
    return Id
def trueFalse():
    global ret
    global rand

    rand = random.randrange(0,2)
    if rand != 1: ret=True 
    else: ret=False
    return ret
def findIndex(searchValue,searchArray):
    try:
        return searchArray.index(searchValue)
    except:
        return -1
def existsInArray(refrenceValue,searchArray,searchIndex):
    retVal=False
    for search in searchArray:
        if refrenceValue == search[searchIndex]:
            retVal = True
    return retVal
def playerOutside():
    if player.y > window_y - 30:
        player.y = window_y - 30
    if player.x > window_x - 30:
        player.x = window_x - 30
def moveEntity():
    if len(bullet_list) != 0: 
        for i in bullet_list:
            i.move()
    if len(enemy_list) != 0:
        for ii in enemy_list:
            ii.move()
def renderEntity():
    if len(bullet_list) != 0:
        for j in bullet_list:
            j.render()
    if len(enemy_list) != 0:
        for jj in enemy_list:
            jj.render()



class playerClass():
    def __init__(self):
        self.x = round(window_x/2)
        self.y = round(window_y/2)
        self.canon_direction = [True,True]

    def move(self,direction):
        if direction == [False,False]: # Down
            self.y+=player_speed
        elif direction == [True,True]: # Up
            self.y-=player_speed
        elif direction == [False,True]: # Right
            self.x-=player_speed
        elif direction == [True,False]: # Left
            self.x+=player_speed

    def render(self):
        pygame.draw.rect(game_window, white, pygame.Rect(self.x, self.y, 30, 30))
        if self.canon_direction == [False,False]: # Down
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+10, self.y+30, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+10, self.y+40, 10, 10))
        elif self.canon_direction == [True,True]: # Up
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+10, self.y-10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+10, self.y-20, 10, 10))
        elif self.canon_direction == [False,True]: # Right
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+30, self.y+10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x+40, self.y+10, 10, 10))
        elif self.canon_direction == [True,False]: # Left
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x-10, self.y+10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x-20, self.y+10, 10, 10))
player = playerClass()

class bullet():
    def __init__(self):
        if player.canon_direction == [False,False]: # Down
            self.x = player.x+10
            self.y = player.y+50
            self.direction = [False,False]
        elif player.canon_direction == [True,True]: # Up
            self.x = player.x+10
            self.y = player.y-30
            self.direction = [True,True]
        elif player.canon_direction == [False,True]: # Right
            self.x = player.x+50
            self.y = player.y+10
            self.direction = [False,True]
        elif player.canon_direction == [True,False]: # Left
            self.x = player.x-30
            self.y = player.y+10
            self.direction = [True,False]

    def spawn():
        bullet_list.append(bullet())

    def move(self):
        if self.x < 0 or self.x > window_x or self.y < 0 or self.y > window_y:
            bullet_list.remove(self)

        if self.direction == [False,False]: # Down
            self.y += bullet_speed
        elif self.direction == [True,True]: # Up
            self.y -= bullet_speed
        elif self.direction == [False,True]: # Right
            self.x += bullet_speed
        elif self.direction == [True,False]: # Left
            self.x -= bullet_speed

    def render(self):
        pygame.draw.rect(game_window, blue, pygame.Rect(self.x, self.y, 10, 10))

class enemy():
    def __init__(self):
        i = random.randrange(0,4)
        jx = random.randrange(0,window_x)
        jy = random.randrange(0,window_y)
        print(i,jx,jy)

        if i == 0: # Down
            self.x = jx
            self.y = 30
            self.direction = [False,False]
        elif i == 1: # Up
            self.x = jx
            self.y = window_y-30
            self.direction = [True,True]
        elif i == 2: # Right
            self.x = 30
            self.y = jy
            self.direction = [False,True]
        elif i == 3: # Left
            self.x = window_x-30
            self.y = jy
            self.direction = [True,False]  

    def spawn():
        if random.randrange(0,100) < spawnChance:
            enemy_list.append(enemy())

    def move(self):
        if self.x < -30 or self.x > window_x or self.y < -30 or self.y > window_y:
            enemy_list.remove(self)

        if self.direction == [False,False]: # Down
            self.y += enemy_speed
        elif self.direction == [True,True]: # Up
            self.y -= enemy_speed
        elif self.direction == [False,True]: # Right
            self.x += enemy_speed
        elif self.direction == [True,False]: # Left
            self.x -= enemy_speed

    def render(self):
        pygame.draw.rect(game_window, green, pygame.Rect(self.x, self.y, 30, 30))

    def detectCollision(self):
        for bullet in bullet_list:
            x1,x2 = bullet.x,bullet.x+10
            y1,y2 = bullet.y,bullet.y+10
            xx,yy = range(self.x,self.x+30),range(self.y,self.y+30)


            if x1 in xx or x2 in xx:
                if y1 in yy or y2 in yy:
                    print("Hit")
                    try:
                        enemy_list.remove(self)
                    except:
                        print("Can't kill")
def input():
    global up,down,right,left,window_x,window_y,fullscreen,last_window_x,last_window_y,small_window_x, small_window_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: up   =  True
            if event.key == pygame.K_s: down =  True
            if event.key == pygame.K_a: right=  True
            if event.key == pygame.K_d: left =  True

            if event.key == pygame.K_UP: player.canon_direction   = [True,True]
            if event.key == pygame.K_DOWN: player.canon_direction = [False,False]
            if event.key == pygame.K_LEFT: player.canon_direction = [True,False]
            if event.key == pygame.K_RIGHT: player.canon_direction= [False,True]

            if event.key == pygame.K_ESCAPE or event.key == pygame.K_r:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                bullet.spawn()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: up   =  False
            if event.key == pygame.K_s: down =  False
            if event.key == pygame.K_a: right=  False
            if event.key == pygame.K_d: left =  False

            if event.key == pygame.K_l:
                enemy_list.append(enemy())
            if event.key == pygame.K_F11: 
                print("Screen Size: ", pygame.display.set_mode().get_size())
                print("Last Size: ", small_window_x, small_window_y)
                if fullscreen == False:
                    fullscreen=True
                    game_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    window_x, window_y = pygame.display.get_window_size()
                    playerOutside()
                else: 
                    fullscreen=False
                    game_window = pygame.display.set_mode((small_window_x,small_window_y), pygame.RESIZABLE)
                    window_x, window_y = pygame.display.get_window_size()
                    small_window_x,small_window_y = window_x, window_y
                    playerOutside()


        if event.type == pygame.VIDEORESIZE:
            window_x, window_y = pygame.display.get_window_size()
            if fullscreen == False: small_window_x,small_window_y = window_x, window_y
            playerOutside()

    if up == True:
        if player.y > 0:
            player.move([True,True])
    if down == True:
        if player.y < window_y - 30:
            player.move([False,False])
    if left == True:
        if player.x < window_x - 30:
            player.move([True,False])
    if right == True:
        if player.x > 0:
            player.move([False,True])

while True:
    input()
    enemy.spawn() 

    moveEntity()

    for i in enemy_list:
        i.detectCollision()

    game_window.fill(black)
    player.render()
    renderEntity()

    pygame.display.update()
    fps.tick(fps_speed)