import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((1300, 900))
pg.display.set_caption("Bill Evans")
clock = pg.time.Clock()

bg = pg.image.load('graphics/bill-evans.jpg')
bg = pg.transform.scale(bg,(1000,692))

musics = ['some-other-time', 'blue-in-green', 'lucky-to-be-me', 'when-i-fall-in-love', 'young-and-foolish']
current_song = 0
pg.mixer.music.load(f'music/{musics[current_song]}.mp3')
pg.mixer.music.play()

flPause = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPause = not flPause
                if flPause:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT: 
                current_song = (current_song + 1) % 5
                pg.mixer.music.load(f'music/{musics[current_song]}.mp3')
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                current_song = (current_song - 1) % 5
                pg.mixer.music.load(f'music/{musics[current_song]}.mp3')
                pg.mixer.music.play()
    screen.fill((255,255,255))
    screen.blit(bg, (400, 208))
    pg.display.update()
    clock.tick(60)