import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Retro Racing Game')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
screen.fill('Cyan')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0)) #block-image-transfer
    pygame.display.update()
    clock.tick(60) # fps ceiling, capper på 60 fps

