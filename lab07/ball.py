import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,800))
pg.display.set_caption("ball")
clock = pg.time.Clock()

screen.fill((255,255,255))

x = 400
y = 400

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    keys= pg.key.get_pressed()
    if keys[pg.K_UP]:
        if y>0:
            y-=20
    if keys[pg.K_DOWN]:
        if y<800:
            y+=20
    if keys[pg.K_RIGHT]:
        if x<800:
            x+=20
    if keys[pg.K_LEFT]:
        if x>0:
            x-=20

    screen.fill((255,255,255))

    pg.draw.circle(screen, (255,0,0), (x,y), 25)
    pg.display.update()
    clock.tick(60)