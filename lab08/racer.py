import pygame as pg
from random import randrange

pg.init()  # Initializing Pygame
screen = pg.display.set_mode((400, 600))
clock = pg.time.Clock()

#upload resources
background = pg.image.load('resource/AnimatedStreet.png').convert_alpha()
player = pg.image.load('resource/Player.png').convert_alpha()
enemy = pg.image.load('resource/Enemy.png').convert_alpha()
coin = pg.image.load('resource/coin.png').convert_alpha()
pg.mixer.music.load('resource/background.wav')

#get rectangles of resources
player_rect = player.get_rect(center=(200, 500))
enemy_rect = enemy.get_rect()
coin_rect = coin.get_rect()
pg.mixer.music.play(-1)
enemy_rect.x = randrange(0, 356, 48)
coin_rect.x = randrange(0, 356, 48)


#initial options
speed = 5
point = 0
coin_collected = False 

#func of game over 
def game_over():
    font = pg.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    gmt = game_over_text.get_rect(center=screen.get_rect().center)
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, gmt)
    pg.display.update()
    pg.time.delay(2000)
    pg.quit()
    exit()




#game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit() 
    #check for keyboard input to change the direction of the snake
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player_rect.x > 0:
        player_rect.x -= speed
    if keys[pg.K_RIGHT] and player_rect.x < 356:
        player_rect.x += speed


    enemy_rect.y += speed
    if enemy_rect.y > 600:
        enemy_rect.y = 0
        enemy_rect.x = randrange(0, 356, 48)
    coin_rect.y += speed
    if coin_rect.y > 600:
        coin_rect.y = 0
        coin_rect.x = randrange(0, 356, 48)
        coin_collected = False  

    if enemy_rect.colliderect(player_rect):
        game_over()
        break
    if coin_rect.colliderect(player_rect) and not coin_collected:
        point += 1

        coin_collected = True  
        coin_rect.x = -coin_rect.width

    #render the text of score
    score = pg.font.Font(None, 36)
    score_text = score.render(f"Score: {point}", True, (0,0,0))


    #draw all the elements
    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(coin, coin_rect)
    screen.blit(score_text, score_text.get_rect(topright=screen.get_rect().topright))
    pg.display.update()
    clock.tick(60)
