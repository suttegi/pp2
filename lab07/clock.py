import pygame as pg
from sys import exit
import datetime as dt

pg.init()
screen=pg.display.set_mode((600,450))
pg.display.set_caption("mickii))))")
clock = pg.time.Clock()

bg = pg.image.load('graphics/mainclock.png').convert_alpha()
bg = pg.transform.scale(bg,(600,450))

minutes = pg.image.load('graphics/rightarm.png').convert_alpha()
minutes = pg.transform.scale(minutes,(600,450))

seconds = pg.image.load('graphics/leftarm.png').convert_alpha()
seconds = pg.transform.scale(seconds,(27,450))

bg_rect = bg.get_rect().center

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    second = dt.datetime.now().second
    minute = dt.datetime.now().minute
    second*=-6
    minute*=-6

    sec_rotate = pg.transform.rotate(seconds,second)
    sec_rect = sec_rotate.get_rect(center=bg_rect)

    min_rotate = pg.transform.rotate(minutes,minute)
    min_rect = min_rotate.get_rect(center=bg_rect)

    screen.blit(bg,(0,0))
    screen.blit(min_rotate,min_rect)
    screen.blit(sec_rotate,sec_rect)

    pg.display.update()
    clock.tick(60)