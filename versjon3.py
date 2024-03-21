import pygame, sys
import random
from pygame import mixer
from button import Button

bredde = 1024
høyde = 1024

pygame.init()
skjerm = pygame.display.set_mode([bredde, høyde])

# Bakgrunn
bakgrunn = pygame.image.load('vei2.jpg')
overlapp = pygame.image.load('vei2.jpg')

b_pos = 0
o_pos = 1024
hastighet = 3

# Bakgrunnsmusikk
mixer.music.load('snowfall.mp3')
mixer.music.play(-1)  # Spiller musikken i en loop

# Bilen
bil = pygame.image.load('bil2premium.png')
bil_x = 200
bil_y = 500

# Snowflakes
snowflakes = []
snowflake_size = 20
snowflake_speed = 6

# Create initial snowflakes
num_snowflakes = 200
for _ in range(num_snowflakes):
    snowflake = pygame.image.load('snowflake.png')  # Load snowflake image
    snowflake = pygame.transform.scale(snowflake, (snowflake_size, snowflake_size))  # Resize snowflake
    snowflake_x = random.randint(0, bredde)
    snowflake_y = random.randint(-høyde, 0)
    snowflakes.append((snowflake, snowflake_x, snowflake_y))

clock = pygame.time.Clock()

def move_snowflakes():
    for i, (snowflake, snowflake_x, snowflake_y) in enumerate(snowflakes):
        snowflake_y += snowflake_speed
        if snowflake_y > høyde:
            snowflake_y = -høyde
            snowflake_x = random.randint(0, bredde)
        # Check for collision with ground
        if snowflake_y + snowflake_size > høyde:
            snowflake_y = random.randint(-høyde, 0)
            snowflake_x = random.randint(0, bredde)
        snowflakes[i] = (snowflake, snowflake_x, snowflake_y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bil_x -= 5  # Juster bilens posisjon til venstre
    if keys[pygame.K_RIGHT]:
        bil_x += 5  # Juster bilens posisjon til høyre

    if b_pos >= høyde:
        b_pos = -høyde
    if o_pos >= høyde:
        o_pos = -høyde

    b_pos += hastighet
    o_pos += hastighet

    move_snowflakes()

    skjerm.blit(bakgrunn, (0, b_pos))
    skjerm.blit(overlapp, (0, o_pos))

    skjerm.blit(bil, (bil_x, bil_y))

    for snowflake, snowflake_x, snowflake_y in snowflakes:
        skjerm.blit(snowflake, (snowflake_x, snowflake_y))

    pygame.display.update()
    clock.tick(60)






