# importing libraries
import pygame
import time
import random
from sys import exit
import numpy as np
import random
 
fps_speed = 15
window_x, window_y = pygame.display.set_mode().get_size()

print("Window size:",window_x,"X",window_y)

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Ett spel, I guess')

game_window = pygame.display.set_mode((0, 0))

fps = pygame.time.Clock()

shoot_delay_time = 10
shoot_delay = 10

bullet_speed = 20

direction = 'RIGHT'
change_to = direction

body_pos = [100, 800]
body = [[100, 50]]

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
def countArray(array):
    i=0
    for j in array:
        i+=1
    return i
def render():
    player.renderPlayer()
    enemy.renderEnemy()
    tank_bullet.renderBullet()
def moveObjects():
    enemy.moveEnemy()
    tank_bullet.move_bullet()


class enemy:
    enemys = []

    def __init__(self,enemys):
        self.enemys = enemys

    def spawn(timer):
        if timer:
            if random.randrange(0,20) == 0:
                spawnSpawn()
            else:
                spawnSpawn()

            def __spawnSpawn():
                direction = [trueFalse(),trueFalse()] #x,y starting from 11:up 10:left 01:right 00:down
                Id = randId(enemy.enemys, 2)

                newPosX = random.randrange(0,window_x-10)
                newPosY = random.randrange(0,window_y-10)

                if direction == [True,True]:
                    enemy.enemys.append([newPosX,0,direction,Id])
                elif direction == [True,False]:
                    enemy.enemys.append([0,newPosY,direction,Id])
                elif direction == [False,False]:
                    enemy.enemys.append([newPosX,window_y,direction,Id])
                elif direction == [False,True]:
                    enemy.enemys.append([window_x,newPosY,direction,Id])
    
    def moveEnemy():
        if len(enemy.enemys) != 0:
            for theEnemy in enemy.enemys:
                index = findIndex(theEnemy, enemy.enemys)
                if theEnemy[2] == [True,True]:
                    enemy.enemys[index][1]+=10
                    if enemy.enemys[index][1] < 0:
                        enemy.enemys.remove(enemy.enemys[index])
                elif theEnemy[2] == [True,False]:
                    enemy.enemys[index][0]+=10
                    if enemy.enemys[index][1] < 0:
                        enemy.enemys.remove(enemy.enemys[index])
                elif theEnemy[2] == [False,False]:
                    enemy.enemys[index][1]-=10
                    if enemy.enemys[index][1] > window_x:
                        enemy.enemys.remove(enemy.enemys[index])
                elif theEnemy[2] == [False,True]:
                    enemy.enemys[index][0]-=10
                    if enemy.enemys[index][1] > window_y:
                        enemy.enemys.remove(enemy.enemys[index])

    def renderEnemy():
        for theEnemy in enemy.enemys:
            pygame.draw.rect(game_window, blue, pygame.Rect(theEnemy[0], theEnemy[1], 20, 20))

class player:
    up = False
    down = False
    left = False
    right = False
    canon_direction = [False,False] #x,y facing the canon 11:up 10:left 01:right 00:down

    def __init__(self,up,down,left,right,canon_direction):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.canon_direction = canon_direction
        # self.tankBullet = self.tank_bullet()
    
    def renderPlayer():
        pygame.draw.rect(game_window, green, pygame.Rect(body_pos[0], body_pos[1], 30, 30))
            
        if player.canon_direction==[True,True]:
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+10, body_pos[1]-10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+10, body_pos[1]-20, 10, 10))
        elif player.canon_direction==[True,False]:
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]-10, body_pos[1]+10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]-20, body_pos[1]+10, 10, 10))
        elif player.canon_direction==[False,True]:
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+30, body_pos[1]+10, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+40, body_pos[1]+10, 10, 10))
        elif player.canon_direction==[False,False]:
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+10, body_pos[1]+30, 10, 10))
            pygame.draw.rect(game_window, blue, pygame.Rect(body_pos[0]+10, body_pos[1]+40, 10, 10))

    def input():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.up = True
                if event.key == pygame.K_s:
                    player.down = True
                if event.key == pygame.K_a:
                    player.left = True
                if event.key == pygame.K_d:
                    player.right = True

                if event.key == pygame.K_UP:
                    player.canon_direction=[True,True]
                if event.key == pygame.K_DOWN:
                    player.canon_direction=[False,False]
                if event.key == pygame.K_LEFT:
                    player.canon_direction=[True,False]
                if event.key == pygame.K_RIGHT:
                    player.canon_direction=[False,True]

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_SPACE:
                    if shoot_delay == 0:
                        tank_bullet.shoot()
                if event.key == pygame.K_r:
                    enemy.enemys=[[100,900,[True,True],1]]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.up = False
                if event.key == pygame.K_s:
                    player.down = False
                if event.key == pygame.K_a:
                    player.left = False
                if event.key == pygame.K_d:
                    player.right = False

    def player_movement():
        if player.up:
            if body_pos[1] > 0:
                body_pos[1] -= 10
        if player.down:
            if body_pos[1] < window_y - 30:
                body_pos[1] += 10
        if player.left:
            if body_pos[0] > 0:
                body_pos[0] -= 10
        if player.right:
            if body_pos[0] < window_x - 30:
                body_pos[0] += 10
    
class tank_bullet:
    direction = [False,False] #x,y facing the canon 11:up 10:left 01:right 00:down
    bullets = []

    def __init__(self,direction,bullets):
        self.direction = directionv
        self.bullets = bullets

    def shoot():
        global shoot_delay
        global shoot_delay_time
        shoot_delay=shoot_delay_time
        Id = randId(tank_bullet.bullets,3)
    
        if player.canon_direction==[True,True]:
            tank_bullet.bullets.append([body_pos[0]+10, body_pos[1]-30, [True,True], Id])
        elif player.canon_direction==[True,False]:
            tank_bullet.bullets.append([body_pos[0]-30, body_pos[1]+10, [True,False], Id])
        elif player.canon_direction==[False,True]:
            tank_bullet.bullets.append([body_pos[0]+50, body_pos[1]+10, [False,True], Id])
        elif player.canon_direction==[False,False]:
            tank_bullet.bullets.append([body_pos[0]+10, body_pos[1]+50, [False,False], Id])
    
    def renderBullet():
        if len(tank_bullet.bullets) != 0:
            for bullet in tank_bullet.bullets:
                pygame.draw.rect(game_window, white, pygame.Rect(bullet[0],bullet[1], 10, 10))

    def move_bullet():
        if len(tank_bullet.bullets) != 0:
            for bullet in tank_bullet.bullets:
                index = findIndex(bullet, tank_bullet.bullets)

                if bullet[2]==[True,True]:
                    tank_bullet.bullets[index][1]-=bullet_speed
                    if tank_bullet.bullets[index][1] < 0:
                        tank_bullet.bullets.remove(tank_bullet.bullets[index])
                elif bullet[2]==[True,False]:
                    tank_bullet.bullets[index][0]-=bullet_speed
                    if tank_bullet.bullets[index][1] < 0:
                        tank_bullet.bullets.remove(tank_bullet.bullets[index])
                elif bullet[2]==[False,True]:
                    tank_bullet.bullets[index][0]+=bullet_speed
                    if tank_bullet.bullets[index][1] > window_x:
                        tank_bullet.bullets.remove(tank_bullet.bullets[index])
                elif bullet[2]==[False,False]:
                    tank_bullet.bullets[index][1]+=bullet_speed
                    if tank_bullet.bullets[index][1] > window_y:
                        tank_bullet.bullets.remove(tank_bullet.bullets[index])

# tank_bullet.bullets=[[100,900,[True,True],2]]
# enemy.enemys=[[100,900,[True,True],1]]

while True:
    player.input()
    player.player_movement()
    
    body.pop()
    body.insert(0, list(body_pos))

    game_window.fill(black)

    # enemy.spawn(True)

    # checkCollision(tank_bullet.bullets, enemy.enemys)

    render()
    moveObjects()

    if shoot_delay != 0:
        shoot_delay-=1

    pygame.display.update()
    fps.tick(fps_speed)