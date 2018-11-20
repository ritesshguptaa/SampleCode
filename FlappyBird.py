import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

color = (randint(0,255), randint(0,255),randint(0,255))

surfaceWidth = 1350
surfaceHeight = 700

imgHeight = 43
imgWidth = 100

pygame.init()
Surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')

def block(x_block, y_block, block_width,block_height, gap,color):
    
    pygame.draw.rect(Surface,color, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(Surface,color, [x_block,y_block+gap+block_height,block_width,surfaceHeight])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN :
           continue
        return event.key
               
    return None
    
    
    

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def makeTextObjsScore(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    Surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    Surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()
    

def helicopter(x,y,image):
    Surface.blit(img, (x,y))

 
def gameOver():
    msgSurface('Crash!')
    main()

def score(current_score,level):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    scoreTextSurf, scoreTextRect = makeTextObjs( "Level: " + str(level) + " Score: " + str(current_score), smallText)
    scoreTextRect.center = 60 , 20
    Surface.blit(scoreTextSurf,[0,0])
    






    

def main():

    x = 150
    y = 200    
    y_move = 0

    x_block = surfaceWidth
    y_block = 0
    block_width = randint(75,85)
    block_height = randint(0,surfaceHeight/2)
    gap = imgHeight * 5

    block_move = 8

    current_score = 0

    level = 1

    

    color = (randint(230,255),randint(20, 255), randint(20,255))
                                                        
    
    
    game_over = False

    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                game_over = True

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_UP:
                    y_move = 5 
        y += y_move
        

        Surface.fill(black)
        helicopter(x,y,img)
                    
        block(x_block, y_block, block_width,block_height, gap,color)
        score(current_score,level)
        
        x_block -= block_move

        if y > surfaceHeight - imgHeight  or y < 0 :
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0,surfaceHeight/2)
            current_score += 1
            color = (randint(230,255),randint(20, 255), randint(20,255))
            #print('score added')

            
        if x + imgWidth > x_block :
            if x < x_block + block_width :
                #print('possibly within the boundry of upper block')
                if y < block_height :
                    #print('Y crossover Upper')
                    if x - imgWidth < block_width + x_block :
                        #print('gameOver upper hit')
                        gameOver()

         
            if x < x_block + block_width :
                #print('possibly hit the boundry of lower block')
                if y + imgHeight > block_height + gap   :
                    #print('Y crossover lower')
                    if x - imgWidth < block_width + x_block  :
                        #print('gameOver lower hit')
                        gameOver()



            #difficutly level
        if current_score >= 10 :
            gap = imgHeight * 4
            level = 2
            block_move = 20

        elif current_score >= 25 :
            gap = imgHeight * 3.5
            level = 3
            block_move = 25
            
        elif current_score >= 100 :
            gap = imgHeight * 3
            level = 4
            block_move = 30
        
                           
                
        pygame.display.update()

        clock.tick(60)

    

main()
pygame.quit()
quit()
