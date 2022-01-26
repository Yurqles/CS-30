#Chrome Dino in OOP Made by Abdirahman Hussein
import pygame
from pygame import mixer
import sys
import math
import random

pygame.init()

#Global Variables
WIDTH = 642
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Chrome Dino!")
time_passed = 8
font = pygame.font.Font('freesansbold.ttf', 16)
score_value = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
play1 = True
play2 = True





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

    


class Cactus(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.image = pygame.image.load("assets/cacti/cactus1.png")
        self.x_ = [642, 1142, 1442, 1942] # stores the x coordinate of all fo my cactus, if you want to add more cactus just add 1 more value in here


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
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/ptero1.png"), (int(54.6), int(40.3)))) #42 x 31
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/ptero2.png"), (int(54.6), int(40.3))))

        self.min_amount = 300
    
    def animate(self): # I need help on slowing down my animation, i tried time.sleep but it stopped everything
        self.index += 1

        if self.index >= 16:
            self.index = 0

        if self.index < 8:
            self.image = pygame.transform.scale(pygame.image.load("assets/ptero1.png"), (int(54.6), int(40.3)))
        elif self.index >= 8:
            self.image = pygame.transform.scale(pygame.image.load("assets/ptero2.png"), (int(54.6), int(40.3)))
        
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= time_passed
        if self.x < -42:
            self.x = cactus.x_[3] +300


class Dinosaur(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)

        #I'm having all of my sprites in an image and im gonna rotate between them, this is where I initialize them
        self.sprites = []
        self.index = 0
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino1.png"), (int(55.9), int(66.3)))) #43 x 51
        self.sprites.append(pygame.transform.scale(pygame.image.load("assets/Dino2.png"), (int(55.9), int(66.3))))


        #To jump I need gravity and a true or false for jumping
        self.state = False
        self.gravity = 1.5

        self.alive = True
        self.container = []

        self.jump_noise = mixer.Sound('assets/sfx/jump.mp3')
        self.deadnoise = mixer.Sound("assets/sfx/lose.mp3")
        self.every100 = mixer.Sound("assets/sfx/100points.mp3")
        self.playsound = True

    def animate(self): # I need help on slowing down my animation, i tried time.sleep but it stopped everything
        self.index += 1

        if self.index >= 16:
            self.index = 0

        if self.index < 8:
            self.image = pygame.transform.scale(pygame.image.load("assets/Dino1.png"), (int(55.9), int(66.3)))
        elif self.index >= 8:
            self.image = pygame.transform.scale(pygame.image.load("assets/Dino2.png"), (int(55.9), int(66.3)))
        
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += self.gravity
    
    def place(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        #I chnage my state to True so it can't double jump in air
        self.dy = -20
        self.jump_noise.play()
        self.state = True

    def falldown(self): # falling down faster
        self.dy += 20

    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False

    def is_aabb_collision(self, other, anArray, i):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - anArray[i]) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

#To find multiples of 100
def multiples(num):
    if num % 100==0:
        return True

    
ground = Ground(0, 250, 642, 60, pygame.image.load("assets/ground.png"))
cactus = Cactus(642, 220, 65, 65, pygame.image.load("assets/cacti/cactus1.png"))
bird = Bird(-52, 100, 42, 31, pygame.image.load("assets/Ptero1.png"))
dinosaur = Dinosaur(100, 220, int(55.9), int(66.3), pygame.image.load("assets/Dino1.png"))


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
    if dinosaur.alive == True:
        score_value +=1

    #Collision Detection
    if dinosaur.is_distance_collision(bird):
        dinosaur.alive = False
    for i in range(len(cactus.x_)):
        if dinosaur.is_aabb_collision(cactus, cactus.x_, i):
            dinosaur.alive = False

    #Make a noise each time you hit a multiple of 100
    if multiples(score_value):
        play2 = True
        if play2 == True:
            dinosaur.every100.play()
            play2 = False
            

    if dinosaur.alive == False:
        time_passed = 0
        dinosaur.gravity = 0
        dinosaur.dy = 0
        if play1 == True:
            dinosaur.deadnoise.play()
            play1 = False


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
    if score_value < 1000:
        screen.fill(WHITE)
    elif score_value >= 1000:
        screen.fill(BLACK)

    #Drawing all of my objects
    ground.draw()
    cactus.draw()
    bird.animate()
    dinosaur.animate()

    #Where I show the score
    score = font.render("Score : " + str(score_value), True, (RED))
    screen.blit(score, (540, 10))

    #How I simulate the objecrs moving backwards and going back
    ground.move()


    pygame.display.update()
    clock.tick(30)

