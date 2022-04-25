import pygame
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
bullet_speed = 5
player_speed = 2
enemy_speed = 2
spawnChance = 1 
powerupChance = 1
advancedMenu = True
boost = 1500
enemyPowerupChance = 4

fullscreen = False
window_x, window_y = (600,600)
#------------------------------------------------------------------------------#

if fullscreen: 
    window_x, window_y = pygame.display.set_mode().get_size()
    game_window = pygame.display.set_mode((window_x, window_y))
else: game_window = pygame.display.set_mode((window_x, window_y), pygame.RESIZABLE)

bullet_shot=0
shoot_timer=0
levelCountdown=0
scoreCount=0
killCount=0
boosted=0
bullet_amount=1
run=True
alive=True
boosting=False
up=False
down=False
right=False
left=False
bullet_list=[]
enemy_list=[]
powerup_list=[]
multishot_list=[]
boss=False
small_window_x, small_window_y = window_x, window_y
hitProcent=100

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

global enemyImg,bulletImg,tankImg,barrelImg,fasterShotingImg,multishotImg

enemyImg = pygame.image.load(resource_path("pictures/enemyImg.png"))
bulletImg = pygame.image.load(resource_path("pictures/bulletImg.png"))
tankImg = pygame.image.load(resource_path("pictures/tankImg.png"))
barrelImg = pygame.image.load(resource_path("pictures/barrelImg.png"))
fasterShotingImg = pygame.image.load(resource_path("pictures/fasterShotingImg.png"))
multishotImg = pygame.image.load(resource_path("pictures/multishotImg.png"))

font = pygame.font.Font(resource_path("FreeSansBold.ttf"), 28)

def log(**txt):
    def __consoleIt(*txt):
        print(*txt)
    __consoleIt(txt["text"][0],txt["text"][1],txt["text"][2],txt["text"][3])
log(text=["Window size:",window_x,"X",window_y])

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
    if not boss:
        bossEnemy.render()
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
        if self.canon_direction == [False,False]: # Down
            game_window.blit(pygame.transform.rotate(tankImg, 180), (self.x,self.y))
            game_window.blit(pygame.transform.rotate(barrelImg, 180), (self.x+10,self.y+30))
        elif self.canon_direction == [True,True]: # Up
            game_window.blit(pygame.transform.rotate(tankImg, 0), (self.x,self.y))
            game_window.blit(pygame.transform.rotate(barrelImg, 0), (self.x+10,self.y-20))
        elif self.canon_direction == [False,True]: # Right
            game_window.blit(pygame.transform.rotate(tankImg, 270), (self.x,self.y))            
            game_window.blit(pygame.transform.rotate(barrelImg, 270), (self.x+30,self.y+10))
        elif self.canon_direction == [True,False]: # Left
            game_window.blit(pygame.transform.rotate(tankImg, 90), (self.x,self.y))
            game_window.blit(pygame.transform.rotate(barrelImg, 90), (self.x-20,self.y+10))
player = playerClass()
class bullet():
    global bullet_amount
    def __init__(self,x,y,canon,offset=0):
        if canon == [False,False]: # Down
            self.x = x+10+offset
            self.y = y+50
            self.direction = [False,False]
        elif canon == [True,True]: # Up
            self.x = x+10+offset
            self.y = y-30
            self.direction = [True,True]
        elif canon == [False,True]: # Right
            self.x = x+50
            self.y = y+10+offset
            self.direction = [False,True]
        elif canon == [True,False]: # Left
            self.x = x-30
            self.y = y+10+offset
            self.direction = [True,False]
    def spawn():
        offset = 0
        i=0
        while i < bullet_amount:
            bullet_list.append(bullet(player.x,player.y,player.canon_direction,offset))
            if offset<=0: offset=abs(offset)+20
            else: offset=offset*-1
            i+=1
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
        game_window.blit(bulletImg, (self.x,self.y))
class powerup():
    def __init__(self,x=0,y=0,type=0):
        self.timer = 360
        rng = random.randrange(0,10)
        if rng <= 3: self.type=0
        else: self.type=1

        if x == 0:
            self.x = random.randrange(0,window_x)
        else:
            self.x=x
        if y == 0:
            self.y = random.randrange(0,window_y)
        else:
            self.y=y
    def spawn(x=0,y=0,enemy=False,noRNG=False):
        if enemy == False:
            if noRNG:
                powerup_list.append(powerup())
            else:
                if random.randrange(0,2000) < powerupChance+1:
                    powerup_list.append(powerup())
        else:
            if noRNG:
                powerup_list.append(powerup(x,y))
            else:
                if random.randrange(0,30) < enemyPowerupChance+1:
                    powerup_list.append(powerup(x,y))
    def render(self):
        if self.type == 0:
            game_window.blit(multishotImg, (self.x,self.y))
        elif self.type == 1:
            game_window.blit(fasterShotingImg, (self.x,self.y))
        else:
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x, self.y, 30, 30))
    def detectCollision(self):
        global alive,scoreCount,killCount,shoot_delay
        xx,yy = range(self.x,self.x+30,1),range(self.y,self.y+30,1)
        px1,px2 = player.x,player.x+30
        py1,py2 = player.y,player.y+30

        if px1 in xx or px2 in xx:
            if py1 in yy or py2 in yy:
                if self.type == 0:
                    multishot_list.append(self)
                elif self.type == 1:
                    shoot_delay-=2     
                powerup_list.remove(self)
class enemy():
    global killCount
    def __init__(self):
        i = random.randrange(0,4)
        jx = random.randrange(0,window_x)
        jy = random.randrange(0,window_y)
        k = random.randrange(0,100)

        self.diagonal=False

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

        if k < 3:
            self.diagonal=True

        self.difficulty = random.randrange(1,3,1)

    def spawn():
        if random.randrange(0,200) < spawnChance+1:
            enemy_list.append(enemy())

    def move(self):
        if self.x < -30 or self.x > window_x or self.y < -30 or self.y > window_y:
            enemy_list.remove(self)

        if self.diagonal:
            if self.direction == [False,False]: # Down
                self.y += enemy_speed*self.difficulty
                self.x += enemy_speed*self.difficulty
            elif self.direction == [True,True]: # Up
                self.y -= enemy_speed*self.difficulty
                self.x -= enemy_speed*self.difficulty
            elif self.direction == [False,True]: # Right
                self.y += enemy_speed*self.difficulty
                self.x += enemy_speed*self.difficulty
            elif self.direction == [True,False]: # Left
                self.y -= enemy_speed*self.difficulty
                self.x -= enemy_speed*self.difficulty
        else:
            if self.direction == [False,False]: # Down
                self.y += enemy_speed*self.difficulty
            elif self.direction == [True,True]: # Up
                self.y -= enemy_speed*self.difficulty
            elif self.direction == [False,True]: # Right
                self.x += enemy_speed*self.difficulty
            elif self.direction == [True,False]: # Left
                self.x -= enemy_speed*self.difficulty

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

                try:
                    file1 = open(resource_path("highscore.txt"), "r") 
                except:
                    file1 = open(resource_path("highscore.txt"), "x")

                oldScore = int(file1.read())
                if oldScore<scoreCount:
                    file1.close()
                    file1 = open(resource_path("highscore.txt"), "w") 
                    file1.write(str(scoreCount))
                    file1.close()
                    score = font.render(str(scoreCount), True, white)
                else:
                    file1.close()
                    score = font.render(str(scoreCount), True, white)

        for bullet in bullet_list:
            bx1,bx2 = bullet.x,bullet.x+10
            by1,by2 = bullet.y,bullet.y+10
         
            if bx1 in xx or bx2 in xx:
                if by1 in yy or by2 in yy:
                    try:
                        powerup.spawn(self.x,self.y,True)
                        enemy_list.remove(self)
                        scoreCount+=1
                        killCount+=1
                    except:
                        pass
class bossEnemy(): #ToDo
    def __init__(self,health=4):
        self.x=random.randrange(30,window_x-30)
        self.y=random.randrange(30,window_y-30)
        self.canon_direction=[True,True]
    
    def spawn():
        boss = bossEnemy()

    def render():
        if boss != False:
            # game_window.blit(bossImg, (boss.x,boss.y))
            pygame.draw.rect(game_window, blue, pygame.Rect(self.x, self.y, 30, 30))

    def shoot(self):
        bullet_list.append(bullet(self.x,self.y,self.canon_direction))

    def ai():
        if boss.x in range(player.x-10,player.y+10) or boss.y in range(player.y-10,player.y+10):
            pass
def start():
    alive=True
    scoreCount=0
    shoot_timer=0
    shoot_delay=60
    bullet_shot=0
    spawnChance=1
    enemy_list=[]
    powerup_list=[]
    bullet_list=[]
    player.x,player.y = round(window_x/2), round(window_y/2)
    up,down,right,left=False,False,False,False
def input():
    global up,down,right,left,window_x,window_y,fullscreen,last_window_x,last_window_y,small_window_x, small_window_y,alive,enemy_list,bullet_list,scoreCount,spawnChance,shoot_delay,shoot_timer,bullet_shot,advancedMenu,boosting

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

            if event.key == pygame.K_LSHIFT:boosting=True
            if event.key == pygame.K_k:
                spawnChance+=1
                if spawnChance % 5 == 0:
                    print("Boss spawn")
                    bossEnemy.spawn()
            if event.key == pygame.K_i:
                advancedMenu = not advancedMenu
            if event.key == pygame.K_j:
                powerup.spawn(0,0,False,True)
            if event.key == pygame.K_r:
                alive=True
                scoreCount=0
                shoot_timer=0
                shoot_delay=60
                bullet_shot=0
                spawnChance=1
                enemy_list=[]
                powerup_list=[]
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

            if event.key == pygame.K_LSHIFT:boosting=False
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
def gui():
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

    shotSign = font.render("shot delay: "+str(shoot_delay), True, white)
    shotSignRect = shotSign.get_rect()
    shotSignRect.center = (110,170)

    shotSign = font.render("Boost: "+str(round(boosted/10)), True, white)
    shotSignRect = shotSign.get_rect()
    shotSignRect.center = (100,175)

    game_window.blit(scoreSign, scoreSignRect)
    game_window.blit(levelSign, levelSignRect)
    if advancedMenu:
        game_window.blit(bulletShot, bulletShotRect)
        game_window.blit(procentSign, procentSignRect)
        game_window.blit(shotSign, shotSignRect)
def dataCheck():
    global killCount,shoot_timer,boosted,spawnChance,player_speed,bullet_amount
    if killCount > 11:
        spawnChance+=1
        killCount=0
        if spawnChance % 5 == 0:
            print("Boss spawn")
            bossEnemy.spawn()
    if shoot_timer != 0: shoot_timer-=1

    if boosted<boost and not boosting:
        boosted+=2
        player_speed=2

    if 0<boosted and boosting and boosted != 0:
        player_speed=4
        boosted-=10
    else:
        player_speed=2

    if boosted<0:
        boosted=0
    
    for bulletPower in multishot_list:
        if bulletPower.timer > 0:
            bulletPower.timer-=1
        else:
            multishot_list.remove(bulletPower)
    bullet_amount = len(multishot_list)+1
while run:
    while alive:
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

        dataCheck()
        
        gui()
        pygame.display.update()
        fps.tick(fps_speed)

    text = font.render('Your highscore:', True, white)
    textRect = text.get_rect()
    textRect.center = (window_x // 2, window_y // 2)

    score = font.render(str(scoreCount), True, white)
    scoreRect = score.get_rect()
    scoreRect.center = (window_x // 2, (window_y // 2)+40)

    file1 = open(resource_path("highscore.txt"), "r") 
    oldScore = font.render("Old Highscore: "+file1.read(), True, white)
    oldScoreRect = oldScore.get_rect()
    oldScoreRect.center = (window_x // 2, window_y // 2+80)

    textSign = font.render("Press R to restart!", True, white)
    textSignRect = textSign.get_rect()
    textSignRect.center = (window_x // 2, window_y // 2+120)

    while not alive:
        input()
        powerup_list=[]
        multishot_list=[]
        boosted=0

        game_window.fill(black)
        game_window.blit(text, textRect)
        game_window.blit(score, scoreRect)
        game_window.blit(oldScore, oldScoreRect)
        game_window.blit(textSign, textSignRect)

        pygame.display.update()