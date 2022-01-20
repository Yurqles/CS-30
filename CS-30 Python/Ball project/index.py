# Constellation Maker by Abdirahman Hussein

# In this program you can make it so you can add more circles and they will connect
# If you click "r", everything will be wiped
#If you left click on a star, it will be gone
#If you press backspace you can undo your last circle you added

# Import and initialize the pygame library
import pygame
import math


#Global Varibales

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 500
HEIGHT = 500

pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Have an array with all of my values
circle_pos = []

def getPosition():
    pos = pygame.mouse.get_pos()
    circle_pos.append(pos)

def popValue(): # I need help with this, it only erases the last one
    for i in range(len(circle_pos)):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        sqx = (x - circle_pos[i][0])**2
        sqy = (y - circle_pos[i][1])**2

        if math.sqrt(sqx + sqy) < 10:
            circle_pos.pop(i)
            break

def removeAll():
    for i in range(len(circle_pos)):
        circle_pos.pop(len(circle_pos)-1)

def removeLast():
    if len(circle_pos)-1 > 0:
        circle_pos.pop()
    else:
        print("Stop please. This is the last one, you killed it's whole family :(")


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                getPosition()
            elif event.button == 3:
                popValue()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                removeAll()
            elif event.key == pygame.K_BACKSPACE:
                removeLast()
                


    # Fill the background with white
    screen.fill(BLACK)
    for n in range(len(circle_pos)):
        pygame.draw.circle(screen, WHITE, circle_pos[n], 10)
        if len(circle_pos) > 1:
            pygame.draw.line(screen, WHITE, circle_pos[n-1], circle_pos[n], 10)
    


    # Flip the display
    pygame.display.flip()


pygame.quit()
