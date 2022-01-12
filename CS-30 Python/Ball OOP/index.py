import pygame
import random
from ball import Ball


WIDTH = 800
HEIGHT = 600
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

starting_balls = 10



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Constellation Maker")
clock = pygame.time.Clock()


def draw_environment(ball_list):
    screen.fill(WHITE)
    for ball_dict in ball_list:
        for ball_id in ball_dict:
            ball = ball_dict[ball_id]
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.size)
            ball.move()

    pygame.display.update()
    
    
    
def main():
    blue_balls = dict(enumerate([Ball(BLUE,WIDTH,HEIGHT) for i in range(starting_balls)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_balls])
        clock.tick(60)

if __name__ == '__main__':
    main()














