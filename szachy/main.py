import pygame as pg
import numpy as np

pg.init()

width = 1024
height = 1024

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Szachy")
white = (255, 220, 178)
brown = (205, 133, 63)


def main():
    pass


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    screen.fill((0, 0, 0))

    main()

    pg.display.flip()
