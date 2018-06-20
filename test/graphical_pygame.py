from unittest.mock import _ANY

import pygame
import time
import extext
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

textbox = pygame.font.SysFont(None, 40)
selections = pygame.font.SysFont(None, 20)
ENOURMOUS = pygame.font.SysFont(None, 100)

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

class Setup:
    def __init__(self):
        self.yes = False
        self.moveOn = False

    def custom_message(self, textType, msg, colour, theX, theY):
        screen_text = textType.render(msg, True, colour)
        gameDisplay.blit(screen_text, [theX, theY])

    def buttonify(self, msg, theX, theY, theW, theH, theI, theA, Action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if theX + theW > mouse[0] > theX and theY + theH > mouse[1] > theY:
            pygame.draw.rect(gameDisplay, theA, (theX, theY, theW, theH))
            if click[0] == 1 and Action != None:
                if Action == "trueName":
                    self.moveOn = True
                elif Action == "notTrueName":
                    self.yes = False
                    player.name = ""
                    player.inputs.value = ""

        else:
            pygame.draw.rect(gameDisplay, theI, (theX, theY, theW, theH))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = Setup.textStuff(self, msg, smallText)
        textRect.center = ((theX + (theW / 2)), (theY + (theH / 2)))
        gameDisplay.blit(textSurf, textRect)

    def textStuff(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

class Player:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.highscore = 0
        self.inputs = extext.Input(x = 360, y = 300)

    def get_name(self):
        while True:
            if not instance.yes:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.name += self.inputs.value
                            instance.yes = True

                gameDisplay.fill(white)
                instance.custom_message(textbox, "Please enter your name below", black, 200, 100)
                self.inputs.update(events)
                self.inputs.draw(gameDisplay)
                pygame.display.update()

            if instance.yes:

                while instance.yes:
                    gameDisplay.fill(white)
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    instance.custom_message(textbox, "Is this your Name?", black, 280, 100)
                    instance.custom_message(textbox, self.name, black, 360, 200)
                    instance.buttonify("Yes", 100, 300, 200, 200, green, brightGreen, Action="trueName")
                    instance.buttonify("No", 500, 300, 200, 200, red, brightRed, Action="notTrueName")
                    pygame.display.update()
                    if instance.moveOn:
                        return self.name


instance = Setup()
player = Player()
Name = player.get_name()
print(Name)