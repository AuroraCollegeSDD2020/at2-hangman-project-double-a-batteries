__author__ = "Bailey Foster"
__license__ = "GPL"
__version__ = "1.5.4"
__email__ = "bailey.foster5@education.nsw.com.au"
__status__ = "Production"

#dependencies
import pygame
import time
import extext
import random
import drawthingz

#initializes pygame
pygame.init()

#define other setup variables

#defining colours to use later on
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

#sets width and height
WIDTH = 800
HEIGHT = 600

#sets different text text sizes
textbox = pygame.font.SysFont(None, 40)
selections = pygame.font.SysFont(None, 20)
ENOURMOUS = pygame.font.SysFont(None, 100)

#define neccesary classes


class Setup: #class used to set up pygame window and define crucial functions
    def __init__(self):
        self.yes = False #creates boolean
        self.moveOn = False #creates boolean
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT)) #creates window to be called in an instance of this class
        self.icon = pygame.image.load('icon.png') #loads image
        pygame.display.set_caption('Get Hanged Man!!') #sets window name
        pygame.display.set_icon(self.icon) #sets window icon
        self.backGround = pygame.image.load("background.png") #loads another image to be used later

    def custom_message(self, textType, msg, colour, theX, theY): #this function is used to put messages on the screen
        screen_text = textType.render(msg, True, colour) # sets what the display will look like
        self.gameDisplay.blit(screen_text, [theX, theY]) # puts the text on the screen with the given coordinates

    def buttonify(self, msg, theX, theY, theW, theH, theI, theA, Action=None): #this function setus up buttons on the screen
        mouse = pygame.mouse.get_pos() #gets the mouse position
        click = pygame.mouse.get_pressed() #gets whether the mouse is clicked

        if theX + theW > mouse[0] > theX and theY + theH > mouse[1] > theY: #
            pygame.draw.rect(self.gameDisplay, theA, (theX, theY, theW, theH))
            if click[0] == 1 and Action != None:
                if Action == "trueName":
                    self.moveOn = True
                elif Action == "notTrueName":
                    self.yes = False
                    player.name = ""
                    player.inputs.value = ""
                elif Action == "easy":
                    player.level = 0
                    instance.moveOn = True
                elif Action == "medium":
                    player.level = 1
                    instance.moveOn = True
                elif Action == "hard":
                    player.level = 2
                    instance.moveOn = True
                elif Action == "impossible":
                    player.level = 3
                    instance.moveOn = True
                elif Action == "Quit":
                    pygame.quit()
                    quit()
                elif Action == "PlayAgain":
                    gameLoop.change = True
                elif Action == "start":
                    return True

        else:
            pygame.draw.rect(self.gameDisplay, theI, (theX, theY, theW, theH))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = Setup.textStuff(self, msg, smallText)
        textRect.center = ((theX + (theW / 2)), (theY + (theH / 2)))
        self.gameDisplay.blit(textSurf, textRect)

    def textStuff(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()


class Player:
    def __init__(self):
        self.name = ""
        self.word = ""
        self.level = 0
        self.highscore = 0
        self.inputs = extext.Input(x = 360, y = 300)
        self.level1wordList = ["cat", "dog", "fox", "wolf", "ship", "maths", "mix", "jar", "pig", "beg", "posh", "what",
                               "home", "rock", "stone", "note", "issue", "code"]
        self.level2wordList = ["cheese", "super", "fibre", "collar", "sheep", "supply", "reason", "catfish", "laptop",
                               "google", "chrome", "python", "adobe", "connect"]
        self.level3wordList = ["Geoff", "awkward", "contract", "hangman", "youtube", "firefox", "bitcoin", "dwarves",
                               "jukebox", "kiosk", "rhythmic", "sphinx", "Zigzag"]
        self.level4wordList = ["antidisestablishmentarianism", "pneumonoultramicroscopicsilicovolcanoconiosis",
                               "floccinaucinihilipilification", "supercalifragilisticexpialidocious",
                               "methionylthreonylthreonyglutaminylarginylisoleucine"]

    def intro(self):
        while True:
            events = pygame.event.get()
            instance.gameDisplay.blit(instance.backGround, (0, 0))
            continues = instance.buttonify("Start", 400, 25, 300, 100, green, brightGreen, Action="start")
            instance.buttonify("Quit", 400, 135, 300, 100, red, brightRed, Action="Quit")
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 50 + 130 > mouse[0] > 50 and 400 + 120 > mouse[1] > 400:
                if click[0] == 1:
                    print("you suck")
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
            if continues:
                break

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

                instance.gameDisplay.fill(white)
                instance.custom_message(textbox, "Please enter your name below", black, 200, 100)
                self.inputs.update(events)
                self.inputs.draw(instance.gameDisplay)
                pygame.display.update()

            if instance.yes:
                while instance.yes:
                    instance.gameDisplay.fill(white)
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
                        instance.yes = False
                        return self.name

    def get_level(self):
        time.sleep(0.3)
        instance.moveOn = False
        while not instance.yes:
            instance.gameDisplay.fill(white)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
            instance.custom_message(textbox, "What level would you like to play at?", black, 150, 50)
            instance.buttonify("Level 1 - Easy", 50, 100, 700, 100, green, brightGreen, Action="easy")
            instance.buttonify("Level 2 - Medium", 50, 220, 700, 100, orange, brightOrange, Action="medium")
            instance.buttonify("Level 3 - Hard", 50, 340, 700, 100, red, brightRed, Action="hard")
            instance.buttonify("Level 4 - Impossible", 50, 460, 700, 100, blue, brightBlue, Action="impossible")
            pygame.display.update()
            if instance.moveOn:
                return self.level

    def get_word(self):
        if self.level == 0:
            self.word = random.choice(self.level1wordList)
        if self.level == 1:
            self.word = random.choice(self.level2wordList)
        if self.level == 2:
            self.word = random.choice(self.level3wordList)
        if self.level == 3:
            self.word = random.choice(self.level4wordList)
        return self.word


class game:
    def __init__(self, Word):
        self.playerName = player
        self.wrongGuesses = 0
        self.wrongGuess = []
        self.rightLetters = []
        self.change = False
        self.won = False
        self.word = Word
        self.x = 100
        self.y = 530
        self.length = list(self.word)
        self.guess = extext.Input(maxlength=1)

    def drawLetters(self):
        if len(self.length) == 3:
            self.x = 348
        elif len(self.length) == 4:
            self.x = 320
        elif len(self.length) == 5:
            self.x = 300
        elif len(self.length) == 6:
            self.x = 280
        elif len(self.length) == 7:
            self.x = 260
        elif len(self.length) == 8:
            self.x = 240
        for letter in self.length:
            if letter in self.rightLetters:
                instance.custom_message(textbox, letter, black, self.x, self.y)
            else:
                instance.custom_message(textbox, "_", black, self.x, self.y)
            self.x += 50
        self.x -= (len(self.length)*50)

    def draw(self):
        while not self.change:
            instance.gameDisplay.fill(white)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.wrongGuesses != 9:
                            self.wrongGuesses += 1
                    elif event.key == pygame.K_DOWN:
                        if self.wrongGuesses != 0:
                            self.wrongGuesses -= 1

            self.guess.update(events)

            if self.wrongGuesses == 1:
                draw.level1(instance.gameDisplay)
            elif self.wrongGuesses == 2:
                draw.level2(instance.gameDisplay)
            elif self.wrongGuesses == 3:
                draw.level3(instance.gameDisplay)
            elif self.wrongGuesses == 4:
                draw.level4(instance.gameDisplay)
            elif self.wrongGuesses == 5:
                draw.level5(instance.gameDisplay)
            elif self.wrongGuesses == 6:
                draw.level6(instance.gameDisplay)
            elif self.wrongGuesses == 7:
                draw.level7(instance.gameDisplay)
            elif self.wrongGuesses == 8:
                draw.level8(instance.gameDisplay)
            elif self.wrongGuesses == 9:
                draw.level9(instance.gameDisplay)

            self.drawLetters()
            instance.custom_message(textbox, "Letters Guessed:", black, 10, 10)
            x = 10
            if len(self.wrongGuess)-1 >= 1:
                for entry in self.wrongGuess:
                        instance.custom_message(textbox, entry, black, x, 50)
                        x += 30
            x = 10
            pygame.display.update()
            if self.guess.value in self.length:
                if self.guess.value not in self.rightLetters:
                    for letter in self.length:
                        if letter == self.guess.value:
                            self.rightLetters.append(self.guess.value)
            else:
                if self.guess.value not in self.wrongGuess:
                    self.wrongGuess.append(self.guess.value)
                    if self.wrongGuesses != 9:
                        self.wrongGuesses += 1

            self.guess.value = ""
            if self.wrongGuesses == 9:
                self.change = True
            if len(self.length) == len(self.rightLetters):
                self.won = True
                self.change = True

        return self.won

    def playerWon(self):
        self.change = False
        while not self.change:
            instance.gameDisplay.fill(white)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
            instance.custom_message(textbox, "Congratulations you guessed the word " + Name + "!!", black, 100, 50)
            instance.custom_message(textbox, "The word was \"" + self.word + "\"", black, 250, 200)
            instance.buttonify("Click here to play again!!", 100, 300, 600, 100, green, brightGreen, Action="PlayAgain")
            instance.buttonify("Click here to Quit!!", 100, 450, 600, 100, red, brightRed, Action="Quit")
            pygame.display.update()

        return "Please stop Erroring"

    def playerLost(self):
        self.change = False
        while not self.change:
            instance.gameDisplay.fill(white)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
            instance.custom_message(textbox, "You unfortunately did not guess the word " + Name + "!!", black, 100, 50)
            instance.custom_message(textbox, "The word was \"" + self.word + "\"", black, 250, 200)
            instance.buttonify("Click here to play again!!", 100, 300, 600, 100, green, brightGreen, Action="PlayAgain")
            instance.buttonify("Click here to Quit!!", 100, 450, 600, 100, red, brightRed, Action="Quit")
            pygame.display.update()

        return "Please stop Erroring"

#setup game
draw = drawthingz.drawLevel()
instance = Setup()
player = Player()
player.intro()
Name = player.get_name()
#game loop
while True:
    Level = player.get_level()
    Word = player.get_word()
    gameLoop = game(Word)
    runGame = gameLoop.draw()
    if runGame:
        runWinScene = gameLoop.playerWon()
    else:
        runLoseScene = gameLoop.playerLost()
