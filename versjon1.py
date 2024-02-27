import pygame as pg
from sys import exit

pg.init() # Starter pygame, viktig at det kommer først
skjerm = pg.display.set_mode((800,400))  # Tuplen inneholder (Bredde, Høyde)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # Tegne alle elementene våres
    # Oppdatere alt
    pg.display.update()
