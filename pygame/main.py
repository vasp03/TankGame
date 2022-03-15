# importing libraries
import pygame
import time
import random
from sys import exit
 
fps_speed = 15
window_x = 0
window_y = 0

key_up = False
key_down = False
key_left = False 
key_right = False
 
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
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

direction = 'RIGHT'
change_to = direction

snake_position = [100, 50]
snake_body = [[100, 50]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up = True
            if event.key == pygame.K_DOWN:
                key_down = True
            if event.key == pygame.K_LEFT:
                key_left = True
            if event.key == pygame.K_RIGHT:
                key_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up = False
            if event.key == pygame.K_DOWN:
                key_down = False
            if event.key == pygame.K_LEFT:
                key_left = False
            if event.key == pygame.K_RIGHT:
                key_right = False


    # if change_to == 'UP' and direction != 'DOWN':
    #     direction = 'UP'
    # if change_to == 'DOWN' and direction != 'UP':
    #     direction = 'DOWN'
    # if change_to == 'LEFT' and direction != 'RIGHT':
    #     direction = 'LEFT'
    # if change_to == 'RIGHT' and direction != 'LEFT':
    #     direction = 'RIGHT'

    if key_up:
        if snake_position[1] > 0:
            snake_position[1] -= 10
    if key_down:
        if snake_position[1] < window_x-10:
            snake_position[1] += 10
    if key_left:
        if snake_position[0] > 0:
            snake_position[0] -= 10
    if key_right:
        if snake_position[0] < window_y-10:
            snake_position[0] += 10

    snake_body.pop()
    snake_body.insert(0, list(snake_position))
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
            pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.display.update()
    fps.tick(fps_speed)
pygame.quit()