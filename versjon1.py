import pygame as pg
from sys import exit

bredde = 1024
høyde = 1024

pg.init() # Starter pygame, viktig at det kommer først
skjerm = pg.display.set_mode([bredde,høyde])  # Tuplen inneholder (Bredde, Høyde)

#Bevgende bakgrunn
bakgrunn = pg.image.load('vei1.jpeg')
overlapp = pg.image.load('vei1.jpeg')

b_pos = 0
o_pos = 1024
hastighet = 0.5

#Bilen
bil = pg.image.load('bil1premium.png')

while True:
    if b_pos >= høyde:
        b_pos = -høyde
    if o_pos >= høyde:
        o_pos = -høyde

    b_pos += hastighet
    o_pos += hastighet

    skjerm.blit(bakgrunn,(0, b_pos))
    skjerm.blit(overlapp,(0, o_pos))
    skjerm.blit(bil,(200,500))
    
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # Tegne alle elementene våres
    # Oppdatere alt
    pg.display.update()
