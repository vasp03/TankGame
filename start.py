import pygame
import sys
import os
import importlib

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

window_x, window_y = (600,600)
fps_speed = 1
running=True
large=True

pygame.init()
pygame.display.set_caption('Tank, the first')
fps = pygame.time.Clock()

if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
    import pyi_splash
    pyi_splash.close()
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

game_window = pygame.display.set_mode((window_x, window_y), pygame.RESIZABLE)

print("Starting start")

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_s:
                import main
                print("Start")
                main.start()
                running = False

while running:
    input()

    font = pygame.font.Font(resource_path("FreeSansBold.ttf"), 32)
    infoSign = font.render("Press S to start!", True, white)
    infoSignRect = infoSign.get_rect()
    infoSignRect.center = (window_x//2,window_y//2)

    game_window.blit(infoSign,infoSignRect)

    pygame.display.update()
    fps.tick(fps_speed)