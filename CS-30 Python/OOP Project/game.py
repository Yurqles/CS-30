import pygame
import sys
import math
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
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino1.png"), (55.9, 66.3))) #43 x 51
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino2.png"), (55.9, 66.3)))


        #To jump I need gravity and a true or false for jumping
        self.state = False
        self.gravity = 1.5


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
        #I cahneg my state to True so it can't double jump in air
        self.dy = -20
        self.state = True

    def falldown(self): # falling down faster
        self.dy += 20
        
 

class Cactus(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.image = pygame.image.load("assets/cacti/cactus1.png")
        self.x_ = [642, 1242, 1842] # stores the x coordinate of all fo my cactus, if you want to add more cactus just add 1 more value in here


    def draw(self):
        for i in range(len(self.x_)):
            screen.blit(self.image, (self.x_[i], self.y))
    
    def update(self):
        for i in range(len(self.x_)):
            self.x_[i] -= time_passed
            if self.x_[i] < -65:
                self.x_[i] = 1842

class Bird(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

        #I'm having all of my sprites in an image and im gonna rotate between them, this is where I initialize them
        self.sprites = []
        self.index = 0
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/ptero1.png"), (54.6, 40.3))) #42 x 31
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/ptero2.png"), (54.6, 40.3)))

        self.min_amount = 300
    
    def animate(self): # I need help on slowing down my animation, i tried time.sleep but it stopped everything
        self.index += 1
        if self.index > 1:
            self.index = 0
        self.image = self.sprites[self.index]
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= time_passed * 1.8
        if self.x < -42:
            self.x = 2568 + self.min_amount









    
ground = Ground(0, 250, 642, 60, pygame.image.load("assets/ground.png"))
cactus = Cactus(642, 220, 65, 65, pygame.image.load("assets/cacti/cactus1.png"))
bird = Bird(642, 100, 42, 31, pygame.image.load("assets/Ptero1.png"))
dinosaur = Dinosaur(100, 220, 55.9, 66.3, pygame.image.load("assets/Dino1.png"))


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
            elif event.key == pygame.K_DOWN:
                dinosaur.falldown()

    #Logic

    #Collision Detection


    #This is how I change my dinosaur's x and y coordinates and dy and constantly
    dinosaur.update()
    cactus.update()
    bird.update()


    #My True or False decreee for the dinosaur becomes false again when it touched the "ground"
    if dinosaur.y >= 220:
        dinosaur.state = False

    #So my dinosaur doesn't fall out of the stage   
    if dinosaur.y > 220:
        dinosaur.place(100, 220)


    #As you progress forward in the game, it makes you look like you are moving faster but in reality everything else is moving faster
    time_passed += 0.0075
    if time_passed >= 50:
        time_passed = 50


    #White canvas
    screen.fill("white")

    #Drawing all of my objects
    ground.draw()
    cactus.draw()
    bird.animate()
    dinosaur.animate()

    #How I simulate the objecrs moving backwards and going back
    ground.move()


    pygame.display.update()
    clock.tick(30)
