import pygame
import sys
import random

pygame.init()

#Screen proportions
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Endless runner")

#Surfaces
ground = pygame.image.load("assets/ground.png")
ground = pygame.transform.scale(ground, (WIDTH, 20))
ground_x = 0
ground_rect = ground.get_rect(center=(640, 400))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill("white")


    ground_x -= 10

    screen.blit(ground, (ground_x, 360))
    screen.blit(ground, (ground_x + 1280, 360))

    if ground_x <= -1280:
        ground_x = 0

    pygame.display.update()
    clock.tick(30)


