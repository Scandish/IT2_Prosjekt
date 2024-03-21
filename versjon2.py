import pygame as pg
from sys import exit
from pygame import mixer
import random

bredde = 1024
høyde = 1024

pg.init()
skjerm = pg.display.set_mode([bredde, høyde])

# Bakgrunn
bakgrunn = pg.image.load('vei1.jpeg')
overlapp = pg.image.load('vei1.jpeg')

b_pos = 0
o_pos = 1024
hastighet = 3

# Bakgrunnsmusikk
mixer.music.load('snowfall.mp3')
mixer.music.play(-1)  # Spiller musikken i en loop

# Bilen
bil = pg.image.load('bil1premium.png')
bil_x = 200
bil_y = 500

# Snowflakes
snowflakes = []
snowflake_size = 2
snowflake_speed = 3

# Create initial snowflakes
num_snowflakes = 50
for _ in range(num_snowflakes):
    snowflake = pg.image.load('snowflake.png')  # Load snowflake image
    snowflake = pg.transform.scale(snowflake, (snowflake_size, snowflake_size))  # Resize snowflake
    snowflake_x = random.randint(0, bredde)
    snowflake_y = random.randint(-høyde, 0)
    snowflakes.append((snowflake, snowflake_x, snowflake_y))

clock = pg.time.Clock()

def move_snowflakes():
    for i, (snowflake, snowflake_x, snowflake_y) in enumerate(snowflakes):
        snowflake_y += snowflake_speed
        if snowflake_y > høyde:
            snowflake_y = -høyde
            snowflake_x = random.randint(0, bredde)
        snowflakes[i] = (snowflake, snowflake_x, snowflake_y)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        bil_x -= 5  # Adjust the car's position to the left
    if keys[pg.K_RIGHT]:
        bil_x += 5  # Adjust the car's position to the right

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

    pg.display.update()
    clock.tick(60)

