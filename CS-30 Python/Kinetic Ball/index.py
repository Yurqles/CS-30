# Pygame Kineitc Ball with elastic vs in-elastic
#Right click to make an elastic ball
#Left click to make an in-elastic ball

# Import and initialize the pygame library
import pygame


#Global Varaibles\
WIDTH = (500)
HEIGHT = (500)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((500, 500))

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = WHITE
        self.width = 30
        self.dx = 0
        self.dy = 0
        self.gravity = 0.0001
        self.circle_pos = []
        self.circle_pos_ = []

    def getPosition(self):
        pos = pos = pygame.mouse.get_pos()
        self.circle_pos.append(pos)
        self.circle_pos_ = list(self.circle_pos)

    def draw(self):
        for i in range(len(self.circle_pos_)):
            pygame.draw.circle(screen, self.color, (self.circle_pos_[i]), self.width)
        pass
    
    def update(self):
        for i in range(len(self.circle_pos)):
            self.circle_pos_[i][0] += self.dx
            self.circle_pos_[i][1] += self.dy
            self.dy += self.gravity
            if self.circle_pos_[1] + self.width > 400:
                self.dy *= -1
        pass



#Create ball

ball = Ball(300, 30)



# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ball.getPosition()

    #Logic
    ball.update()

    # Fill the background with white
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, 400), (WIDTH, 400), 20)
    ball.draw()




    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
