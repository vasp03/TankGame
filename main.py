import pygame
import random
import random
import sys
import os
import importlib

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

shoot_delay = 60
bullet_speed = 3
player_speed = 2
enemy_speed = 2
maximum_enemys = 100
spawnChance = 1 
powerupChance = 1

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

bullet_shot=0
shoot_timer=0
levelCountdown=0
run=True
alive = True
bullet_list=[]
enemy_list=[]
powerup_list=[]
small_window_x, small_window_y = window_x, window_y
pygame.init()
pygame.display.set_caption('Ett spel, I guess')
fps = pygame.time.Clock()
scoreCount=0
killCount=0
hitProcent=100

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

enemyImg = pygame.image.load(resource_path("enemyImg.png"))
# bulletImg = pygame.image.load(resource_path("bulletImg.png"))
# tankImg = pygame.image.load(resource_path("tankImg.png"))
powerupImg = pygame.image.load(resource_path("powerupImg.png"))

font = pygame.font.Font(resource_path("FreeSansBold.ttf"), 32)

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
    if len(powerup_list) != 0:
        for jjj in powerup_list:
            jjj.render()

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
        # pygame.draw.rect(game_window, blue, pygame.Rect(self.x, self.y, 10, 10))
        game_window.blit(powerupImg, (self.x,self.y))


class powerup():
    def __init__(self):
        self.x = random.randrange(0,window_x)
        self.y = random.randrange(0,window_y)
        self.powerup = random.randrange(0,1)

    def spawn():
        if random.randrange(0,1000) < powerupChance+1:
            powerup_list.append(powerup())

    def render(self):
        pygame.draw.rect(game_window, green, pygame.Rect(self.x, self.y, 30, 30))
        # game_window.blit(powerupImg, (self.x,self.y))

    def detectCollision(self):
        global alive,scoreCount,killCount,shoot_delay
        xx,yy = range(self.x,self.x+30,1),range(self.y,self.y+30,1)
        px1,px2 = player.x,player.x+30
        py1,py2 = player.y,player.y+30

        if px1 in xx or px2 in xx:
            if py1 in yy or py2 in yy:
                shoot_delay-=2
                powerup_list.remove(self)

class enemy():
    global killCount
    def __init__(self):
        i = random.randrange(0,4)
        jx = random.randrange(0,window_x)
        jy = random.randrange(0,window_y)

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
        if random.randrange(0,200) < spawnChance+1:
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
        if self.direction == [True,True]: #Up
            game_window.blit(pygame.transform.rotate(enemyImg, 270), (self.x,self.y))
        elif self.direction == [False,False]: #Down
            game_window.blit(pygame.transform.rotate(enemyImg, 90), (self.x,self.y))
        elif self.direction == [True,False]: #Left
            game_window.blit(pygame.transform.flip(enemyImg, False, False), (self.x,self.y))
        elif self.direction == [False,True]: #Right
            game_window.blit(pygame.transform.flip(enemyImg, True, False), (self.x,self.y))

    def detectCollision(self):
        global alive,scoreCount,killCount
        xx,yy = range(self.x,self.x+30,1),range(self.y,self.y+30,1)
        px1,px2 = player.x,player.x+30
        py1,py2 = player.y,player.y+30

        if px1 in xx or px2 in xx:
            if py1 in yy or py2 in yy:
                alive=False
                score = font.render(str(scoreCount), True, white)

        for bullet in bullet_list:
            bx1,bx2 = bullet.x,bullet.x+10
            by1,by2 = bullet.y,bullet.y+10
         
            if bx1 in xx or bx2 in xx:
                if by1 in yy or by2 in yy:
                    print("Hit")
                    try:
                        enemy_list.remove(self)
                        scoreCount+=1
                        killCount+=1
                    except:
                        print("Can't kill")
def input():
    global up,down,right,left,window_x,window_y,fullscreen,last_window_x,last_window_y,small_window_x, small_window_y,alive,enemy_list,bullet_list,scoreCount,spawnChance,shoot_delay,shoot_timer,bullet_shot

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and alive: up   =  True
            if event.key == pygame.K_s and alive: down =  True
            if event.key == pygame.K_a and alive: right=  True
            if event.key == pygame.K_d and alive: left =  True

            if event.key == pygame.K_UP and alive: player.canon_direction   = [True,True]
            if event.key == pygame.K_DOWN and alive: player.canon_direction = [False,False]
            if event.key == pygame.K_LEFT and alive: player.canon_direction = [True,False]
            if event.key == pygame.K_RIGHT and alive: player.canon_direction= [False,True]

            if event.key == pygame.K_k:
                spawnChance+=1
            if event.key == pygame.K_r:
                alive=True
                scoreCount=0
                shoot_timer=0
                bullet_shot=0
                spawnChance=1
                enemy_list=[]
                bullet_list=[]
                player.x,player.y = round(window_x/2), round(window_y/2)
                up,down,right,left=False,False,False,False
            if event.key == pygame.K_ESCAPE:
                run=False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE and alive and shoot_timer <= 0:
                bullet.spawn()
                bullet_shot+=1 
                shoot_timer=shoot_delay


        if event.type == pygame.KEYUP and alive:
            if event.key == pygame.K_w: up   =  False
            if event.key == pygame.K_s: down =  False
            if event.key == pygame.K_a: right=  False
            if event.key == pygame.K_d: left =  False

            if event.key == pygame.K_l and alive:
                enemy_list.append(enemy())
            if event.key == pygame.K_F11: 
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

    if up == True and alive:
        if player.y > 0:
            player.move([True,True])
    if down == True and alive:
        if player.y < window_y - 30:
            player.move([False,False])
    if left == True and alive:
        if player.x < window_x - 30:
            player.move([True,False])
    if right == True and alive:
        if player.x > 0:
            player.move([False,True])


while run:
    while alive:
        scoreSign = font.render("Score: "+str(scoreCount), True, white)
        scoreSignRect = scoreSign.get_rect()
        scoreSignRect.center = (70,20)

        levelSign = font.render("Level: "+str(spawnChance), True, white)
        levelSignRect = levelSign.get_rect()
        levelSignRect.center = (65,60)

        bulletShot = font.render("Shot bullets: "+str(bullet_shot), True, white)
        bulletShotRect = bulletShot.get_rect()
        bulletShotRect.center = (116,100)

        if bullet_shot==0:hitProcent=0
        else: hitProcent=round((scoreCount+0.001)/(bullet_shot+0.001)*100)

        procentSign = font.render("Hit %: "+str(hitProcent), True, white)
        procentSignRect = procentSign.get_rect()
        procentSignRect.center = (82,140)

        input()
        enemy.spawn() 
        powerup.spawn()

        moveEntity()

        for i in enemy_list:
            i.detectCollision()
        for j in powerup_list:
            j.detectCollision()

        game_window.fill(black)
        player.render()
        renderEntity()

        game_window.blit(scoreSign, scoreSignRect)
        game_window.blit(levelSign, levelSignRect)
        game_window.blit(bulletShot, bulletShotRect)
        game_window.blit(procentSign, procentSignRect)

        if killCount > 9:
            print("Higher")
            spawnChance+=1
            killCount=0
        if shoot_timer != 0: shoot_timer-=1

        pygame.display.update()
        fps.tick(fps_speed)

    text = font.render('Your highscore:', True, white)
    textRect = text.get_rect()
    textRect.center = (window_x // 2, window_y // 2)

    score = font.render(str(scoreCount), True, white)
    scoreRect = score.get_rect()
    scoreRect.center = (window_x // 2, (window_y // 2)+40)

    while not alive:
        input()

        game_window.fill(black)
        game_window.blit(text, textRect)
        game_window.blit(score, scoreRect)

        pygame.display.update()