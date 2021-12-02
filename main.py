# CPSC 3720
# Julio Reyes
# 12/02/2021

import pygame
import sys
import pip._vendor.requests
import json
from pygame import mixer
import random
import time

pygame.init()
init_check = pygame.init()

# INITIALIZATION CHECK
if init_check[1] > 0:
    print("Errors During Initialization, quitting....".format(init_check[1]))
    sys.exit(-1)
else:
    print("PyGame Initialized Successfully")


# Background Music
mixer.music.load("familyfeud.mp3")
mixer.music.play(-1)


width = 800
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('CPSC 3720 - Charades Game')
pygame.display.flip()

screenWidth = screen.get_width()
screenHeight = screen.get_height()

clock = 60

# Game Fonts
smallerFont = pygame.font.SysFont('Gabriola', 40)
medFont = pygame.font.SysFont('Gabriola', 45)
largeFont = pygame.font.SysFont('Gabriola', 50)

# Game Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (166,16,30)

# Background
background = pygame.image.load('background.jpg')

# Random Word API
# Get Random Word
randomWord = pip._vendor.requests.get ("https://random-word-form.herokuapp.com/random/noun");


def mainScreen():
    gameScreen = largeFont.render('CPSC 3720 - CHARADES', True, white)
    mainRect = gameScreen.get_rect()
    mainRect.midtop = (400, 10)
    screen.blit(gameScreen, mainRect)
    gameText = smallerFont.render('Your Word is Displayed Below...', True, white)
    textRect = gameText.get_rect()
    textRect.midtop = (400, 55)
    screen.blit(gameText, textRect)

# Displays the current word to the player
# Grabs new word from random word API
def currentWord():
    data = json.loads(randomWord.text)
    data = json.dumps(data)
    gameCard = largeFont.render(data, True, white)
    gameCardRect = gameCard.get_rect()
    gameCardRect.midtop = (width / 2, height / 2 - 40)
    screen.blit(gameCard, gameCardRect)


# Button for selecting new word
def newCard():
    nextButtonText = largeFont.render('New Card', True, black)
    # creating next button
    nextButton = nextButtonText.get_rect()
    # set center of next button
    nextButton.midbottom = screenWidth / 2, screenHeight / 2 + 95
    # create button
    pygame.draw.rect(screen, white, [screenWidth / 2 - 90, screenHeight / 2 + 40, 185, 50])
    # put text onto the button
    screen.blit(nextButtonText, nextButton)


# Controller
fpsController = pygame.time.Clock()

# Timer decreases each second
pygame.time.set_timer(pygame.USEREVENT, 1000)

# GAME
while True:

    screen.fill(black)
    # Inserting Background Image
    screen.blit(background, (0,0))
    # Timer
    timer = medFont.render('Next Word In: ' + str(clock), True, white)
    screen.blit(timer, (300, 95))

    for event in pygame.event.get():
        # Quitting
        if event.type == pygame.QUIT:
            pygame.quit()

        # Timer Conditions
        elif event.type == pygame.USEREVENT:
            clock -= 1
            # Timer Resets When Complete + New Word Added
            if clock <= 0:
                clock = 60
                pygame.time.set_timer(pygame.USEREVENT, 1000)
                randomWord = pip._vendor.requests.get("https://random-word-form.herokuapp.com/random/noun");
                currentWord()
                pygame.display.update()

        # Mouse Condition for New Word
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 310 <= mouse[0] <= 495 and 290 <= mouse[1] <= 370:
                randomWord = pip._vendor.requests.get("https://random-word-form.herokuapp.com/random/noun");
                currentWord()
                pygame.display.update()



        # get the pos of the mouse so we can know which button
        mouse = pygame.mouse.get_pos()
        mainScreen()
        newCard()
        currentWord()
        pygame.display.update()


