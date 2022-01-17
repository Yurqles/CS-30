import pygame
import sys
import time
import random

pygame.init()

#Screen proportions
WIDTH = 642
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Endless runner")
time_passed = 5



class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.dy = 0
        self.dx = 0
        self.width = width
        self.height = height
        self.image = image

class Ground(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

    def draw(self): #I need help on why it's moving both of them backwards
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, ((self.x + 624), self.y))

    def move(self):
        self.x -= time_passed

        #Make an illusion looking like it's a never ending ground by having two grounds that teleport when they go past the screen's width by 2 times (-642)
        if self.x <= -642:
            self.x = 0

    

class Dinosaur(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

        #I'm having all of my sprites in an image and im gonna rotate between them, this is where I initialize them
        self.sprites = []
        self.index = 0
        self.sprites.append(pygame.image.load("assets/Dino1.png"))
        self.sprites.append(pygame.image.load("assets/Dino2.png"))
        self.image = self.sprites[self.index]

        #To jump I need gravity and a true or false for jumping
        self.state = False
        self.gravity = 1


    def animate(self): # I need help on slowing down my animation, i tried time.sleep but it stopped everything
        self.index += 1
        if self.index > 1:
            self.index = 0
        self.image = self.sprites[self.index]
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += self.gravity
    
    def place(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        self.dy = -15
        self.state = True
        
        

    
ground = Ground(0, 250, 642, 60, pygame.image.load("assets/ground.png"))
dinosaur = Dinosaur(50, 225, 43, 51, pygame.image.load("assets/Dino1.png"))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Keyboard events - I only jump though...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if dinosaur.state == False:
                    dinosaur.jump()


    #Logic

    #This is how I change my dinosaur's x and y coordinates and dy and dx
    dinosaur.update()


    #My True or False decreee for the dinosaur becomes false again when it touched the "ground"
    if dinosaur.y == 225:
        dinosaur.state = False

    #So my dinosaur doesn't fall out of the stage   
    if dinosaur.y > 225:
        dinosaur.place(50, 225)


    #As you progress forward in the game, it makes you look like you are moving faster but in reality everything else is moving faster
    time_passed += 0.0075
    if time_passed >= 50:
        time_passed = 50


    #White canvas
    screen.fill("white")

    #Drawing all of my objects
    ground.draw()
    dinosaur.animate()

    #How I simulate the ground moving backwards and going back
    ground.move()


    pygame.display.update()
    clock.tick(30)


