# Simple pygame program

# Import and initialize the pygame library
import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop

running = True 
while running:
    screen.fill(0, 0, 0)
    playerX += 0.1

     # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key is pressed cheks if it is left or right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
             print("left arrow is pressed")
        if event.type == pygame.K_RIGHT:
             print("right key is pressed")


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        player(playerX, playerY)
        pygame.display.update()




