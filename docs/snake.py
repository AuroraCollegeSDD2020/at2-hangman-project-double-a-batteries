import pygame
import time
import random
from pygame import font

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
brightRed = (255, 0, 0)
green = (0, 200, 0)
brightGreen = (0, 255, 0)
blue = (0, 0, 200)
brightBlue = (0, 0, 255)
orange = (255,69,0)
brightOrange = (255,127,80)

blocky = 10
FPS = 30

WIDTH = 800
HEIGHT = 600

font = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [(WIDTH/2 - (len(msg)*3.5)), (HEIGHT/2)])

def custom_message(msg, colour, theX, theY):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [theX, theY])

def mainMenu():
        pygame.display.set_caption("Slither")
        while True:
                gameDisplay.fill(white)
                message_to_screen("welcome to Slither!", blue)
                custom_message("Press E for endless mode or C for campaign!", blue, 235, 400)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_e:
                                        gameLoop()
                                        False
                                elif event.key == pygame.K_c:
                                        campaign()
                                        False
                pygame.display.update()
        

def snake(blocky, snakeList):
        for XnY in snakeList:
            pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], blocky, blocky])

def gameLoop():
    lead_x = (WIDTH/2)
    lead_y = (HEIGHT/2)
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, (WIDTH-blocky))/10.0)*10.0
    randAppleY = round(random.randrange(0, (HEIGHT-blocky))/10.0)*10.0

    gameExit = False
    gameOver = False

    snakeList = []
    snakeLength = 1
    appleThickness = 10
    count = 0

    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over, Press R to restart or Q to quit", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_r:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    lead_x_change = -blocky
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    lead_x_change = blocky
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    lead_y_change = -blocky
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    lead_y_change = blocky
                    lead_x_change = 0

        if lead_x >= WIDTH:
            lead_x = 10
        if lead_x <= 0:
            lead_x = WIDTH-10
        if lead_y >= HEIGHT:
            lead_y = 10
        if lead_y <= 0:
            lead_y = HEIGHT-10

        if lead_x in range(100, 125) and lead_y in range(100, 200):
            gameOver = True
        if lead_x in range(125, 675) and lead_y in range(100, 125):
            gameOver = True
        if lead_x in range(675, 700) and lead_y in range(100, 200):
            gameOver = True
        if lead_x in range(100, 125) and lead_y in range(400, 500):
            gameOver = True
        if lead_x in range(125, 675) and lead_y in range(470, 500):
            gameOver = True
        if lead_x in range(670, 700) and lead_y in range(400, 500):
            gameOver = True
        #print(lead_x, lead_y)
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.polygon(gameDisplay, black, ([100, 100], [100, 200], [125, 200], [125, 125], [675, 125], [675, 200], [700, 200], [700, 100]), 0)
        pygame.draw.polygon(gameDisplay, black, ([100, 500], [100, 400], [125, 400], [125, 475], [675, 475], [675, 400], [700, 400], [700, 500]), 0)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])
        custom_message("Score: " + str(count), red, 700, 10)
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
           del snakeList[0]

        for segMent in snakeList[:-1]:
            if segMent == snakeHead:
                gameOver = True
        
        snake(blocky, snakeList)
        
        pygame.display.update()

        if randAppleX in range(100, 125) and randAppleY in range(100, 200):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0
        if randAppleX in range(125, 675) and randAppleY in range(100, 125):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0
        if randAppleX in range(675, 700) and randAppleY in range(100, 200):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0
        if randAppleX in range(100, 125) and randAppleY in range(400, 500):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0
        if randAppleX in range(125, 675) and randAppleY in range(470, 500):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0
        if randAppleX in range(670, 700) and randAppleY in range(400, 500):
            randAppleX = round(random.randrange(0, (WIDTH - blocky)) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, (HEIGHT - blocky)) / 10.0) * 10.0

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, (WIDTH-blocky))/10.0)*10.0
            randAppleY = round(random.randrange(0, (HEIGHT-blocky))/10.0)*10.0
            snakeLength += 1
            count += 1
            
        clock.tick(FPS)
def campaign():
    lead_x = (WIDTH/2)
    lead_y = (HEIGHT/2)
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, (WIDTH-blocky))/10.0)*10.0
    randAppleY = round(random.randrange(0, (HEIGHT-blocky))/10.0)*10.0

    gameExit = False
    gameOver = False

    snakeList = []
    snakeLength = 1
    appleThickness = 10
    FPS = 30
    count = 0
    level = 1

    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over, Press R to restart or Q to quit", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    elif event.key == pygame.K_r:
                        campaign()
                        count = 0
                        level = 1
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    lead_x_change = -blocky
                    lead_y_change = 0
                elif event.key == pygame.K_d:
                    lead_x_change = blocky
                    lead_y_change = 0
                elif event.key == pygame.K_w:
                    lead_y_change = -blocky
                    lead_x_change = 0
                elif event.key == pygame.K_s:
                    lead_y_change = blocky
                    lead_x_change = 0

        if lead_x >= WIDTH or lead_x <= 0 or lead_y >= HEIGHT or lead_y <= 0:
            gameOver = True
        
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
           del snakeList[0]

        for segMent in snakeList[:-1]:
            if segMent == snakeHead:
                gameOver = True

        custom_message("count: " + str(count), red, 700, 10)
        
        snake(blocky, snakeList)
        
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, (WIDTH-blocky))/10.0)*10.0
            randAppleY = round(random.randrange(0, (HEIGHT-blocky))/10.0)*10.0
            snakeLength += 1
            count += 1

        if count == 20:
                level += 1
                while True:
                        gameDisplay.fill(white)
                        message_to_screen("Level " + str(level), red)
                        custom_message("Press Enter to continue or q to quit", red, 320, 400)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_q:
                                                pygame.quit()
                                        elif event.key == pygame.K_e:
                                                count = 0
                                                FPS += 5
                                                campaign()
                                                break
                        pygame.display.update()
                
        clock.tick(FPS)


mainMenu()