import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("space inveders")
icon = pygame.image.load("arcade-game.png")
pygame.display.set_icon(icon)

#font
font =pygame.font.Font('Gameplay.ttf',32)
textX = 10
textY =10

#game over
over_font =pygame.font.Font('Gameplay.ttf',64)
highScore_font =pygame.font.Font('Gameplay.ttf',32)



#score
score_value = 0
global high_score
high_score = 0


#player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy

EnemyImage = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemy = 6


for i in range(num_of_enemy):
    EnemyImage.append(pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0, 736))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(4)
    EnemyY_change.append(40)

    
#bullet
"""
state ready means bullet is hidden
state fire means bullet is visible
"""
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#background
backgroundImage = pygame.image.load("background.png")

#music
mixer.music.load("background.wav")
mixer.music.play(-1)

def show_score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    screen.blit(backgroundImage,(0,0))
    game_over_text = over_font.render("GAME OVER ",True,(255,255,255))
    screen.blit(game_over_text,(200,250))
    highScore_text = highScore_font.render("Your Score : "+str(score_value),True,(255,255,255))
    screen.blit(highScore_text,(280,330))
    

def Player(x,y):
    screen.blit(playerImage,(x,y))

def Enemy(x,y,i):
    screen.blit(EnemyImage[i],(x,y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage,(x+16,y+10))

def isCollision(EnemyX,EnemyY,bulletX,bulletY):
    distance = math.sqrt(  (math.pow(EnemyX-bulletX,2)) + (math.pow(EnemyY-bulletY,2)) )
    if distance <  27:
        return True
    else:
        return False
    
    
running =True
while running:
    screen.fill((0,0,0))
    screen.blit(backgroundImage,(0,0))
    
    
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #key stroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(bulletX,bulletY)
                    
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    #boundry
    if playerX <= 0 :
        playerX = 0
    if playerX >=736 :
        playerX = 736


    for i in range(num_of_enemy):
        #game over
        if EnemyY[i] >= 440:
            for j in range(num_of_enemy):
                EnemyY[j] = 2000
            game_over()
            break


        
        EnemyX[i] += EnemyX_change[i]
        #boundry
        if EnemyX[i] <= 0 :
            EnemyX_change[i] = 3
            EnemyY[i] += EnemyY_change[i]
            
        elif EnemyX[i] >=736 :
            EnemyX_change[i] = -3
            EnemyY[i] += EnemyY_change[i]

        #collision
        collision = isCollision(EnemyX[i],EnemyY[i],bulletX,bulletY)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
           # print(score)
            EnemyX[i] = random.randint(0,735)
            EnemyY[i] = random.randint(50,150)
        
        Enemy(EnemyX[i],EnemyY[i] , i)


    
            

    #bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        bullet_fire(bulletX,bulletY)
        bulletY -= bulletY_change

    


        
    Player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
    
