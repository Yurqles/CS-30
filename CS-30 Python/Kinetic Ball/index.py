# Pygame Kineitc Ball with elastic vs in-elastic
#Right click to make an elastic ball
#Left click to make an in-elastic ball

# Import and initialize the pygame library
import random
import pygame
import time


#Global Varaibles
WIDTH = (500)
HEIGHT = (500)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#start pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((500, 500))

class Ball():
    def __init__(self, color):
        self.color = color
        self.width = 30
        self.gravity = 0.0001
        self.x_position = []
        self.y_position = []
        self.dx_values = [-0.05, 0.015, -0.01, 0.01, 0.005, -0.005]
        self.dx_position = []
        self.dy_position = []

    def getPosition(self):
        pos = pos = pygame.mouse.get_pos()
        self.x_position.append(pos[0])
        self.y_position.append(pos[1])
        self.dx_position.append(random.choice(self.dx_values))
        self.dy_position.append(0)
    
    def draw(self):
        self.start_time = time.time()
        for i in range(len(self.x_position)):
            pygame.draw.circle(screen, self.color, (self.x_position[i], self.y_position[i]), self.width)
    def update(self):
        for i in range(len(self.x_position)):
            self.x_position[i] += self.dx_position[i]
            self.y_position[i] += self.dy_position[i]
            self.dy_position[i] += self.gravity

            #So it can bounce back up once it hits the line
            if self.y_position[i] > 360:
                self.dy_position[i] *= -1
            if self.x_position[i] - self.width< 0:
                self.dx_position[i] *= -1
            elif self.x_position[i] + self.width > WIDTH:
                self.dx_position[i] *= -1
    
class ElasticBall(Ball):
    def __init__(self, color):
        super().__init__(color)
        self.gravity = 0.0001
    
class InelasticBall(Ball):
    def __init__(self, color):
        super().__init__(color)
        self.gravity = 0.0001

    def addWork(self):
        for i in range(len(self.x_position)):
            self.dy_position[i] *= 0.9999


    
    

#Create ball

elasticBall = ElasticBall(WHITE)
inelasticBall = InelasticBall(RED)


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                elasticBall.getPosition()
            elif event.button == 3:
                inelasticBall.getPosition()


    #Logic
    elasticBall.update()
    inelasticBall.update()
    inelasticBall.addWork()


    # Fill the background with white
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, 400), (WIDTH, 400), 20)
    elasticBall.draw()
    inelasticBall.draw()




    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()



