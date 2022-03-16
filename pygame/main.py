# importing libraries
import pygame
import time
import random
from sys import exit
import numpy as np
import random
 
fps_speed = 15
window_x, window_y = pygame.display.set_mode().get_size()

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

shoot_delay = 10
direction = 'RIGHT'
change_to = direction

body_pos = [100, 800]
body = [[100, 50]]

def shoot_bullet():
    if shoot_delay == 0:
        tank_bullet.shoot()
        shoot_delay = 10

class tank_bullet:
    direction = [False,False] #x,y facing the canon 11:up 10:left 01:right 00:down
    bullets = []

    def __init__(self,direction,bullets):
        self.direction = direction
        self.bullets = bullets

    def shoot():
        Id = random.randrange(1,1000)
        same = True

        while same:
            existed=False
            for exists in tank_bullet.bullets:
                if exists[3] == Id:
                    Id = random.randrange(1,1000)
                    existed=True
            if not existed: same=False
      
        if player.canon_direction==[True,True]:
            tank_bullet.bullets.append([body_pos[0]+10, body_pos[1]-30, [True,True], Id])
        elif player.canon_direction==[True,False]:
            tank_bullet.bullets.append([body_pos[0]-30, body_pos[1]+10, [True,False], Id])
        elif player.canon_direction==[False,True]:
            tank_bullet.bullets.append([body_pos[0]+50, body_pos[1]+10, [False,True], Id])
        elif player.canon_direction==[False,False]:
            tank_bullet.bullets.append([body_pos[0]+10, body_pos[1]+50, [False,False], Id])
    
    def move_bullet():
        def find(m):
            for x, new_val in enumerate(tank_bullet.bullets):
                try:
                    y = new_val.index(m)
                except ValueError:
                    continue
                yield x, y

        if np.array(tank_bullet.bullets).size != 0:
            for bullet in tank_bullet.bullets:
                pygame.draw.rect(game_window, white, pygame.Rect(bullet[0],bullet[1], 10, 10))
                index = [z for z in find(bullet[3])][0][0]

                if bullet[2]==[True,True]:
                    tank_bullet.bullets[index][1]-=10
                    if tank_bullet.bullets[index][1] < 0:
                        tank_bullet.bullets.pop(index)
                elif bullet[2]==[True,False]:
                    tank_bullet.bullets[index][0]-=10
                    if tank_bullet.bullets[index][1] < 0:
                        tank_bullet.bullets.pop(index)
                elif bullet[2]==[False,True]:
                    tank_bullet.bullets[index][0]+=10
                    if tank_bullet.bullets[index][1] > window_x:
                        tank_bullet.bullets.pop(index)
                elif bullet[2]==[False,False]:
                    tank_bullet.bullets[index][1]+=10
                    if tank_bullet.bullets[index][1] > window_y:
                        tank_bullet.bullets.pop(index)
      
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
    
    def draw_player():
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
                    shoot_bullet()

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


while True:
    player.input()
    player.player_movement()
    

    body.pop()
    body.insert(0, list(body_pos))

    game_window.fill(black)

    player.draw_player()
    tank_bullet.move_bullet()

    if shoot_delay != 0:
        shoot_delay-=1

    pygame.display.update()
    fps.tick(fps_speed)
pygame.quit()