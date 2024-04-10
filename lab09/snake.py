import pygame as pg 
from random import randrange
from random import randint

pg.init()  # Initializing Pygame

# Setting window parameters and creating the screen
wh = 800
screen = pg.display.set_mode((wh, wh))

# Initial state of the snake and food
dx, dy = 0, 0
size = 20
speed = 10  
segments = [(randrange(0, wh, size), randrange(0, wh, size))]  # Initial snake position
point_x, point_y = randrange(0, wh, size), randrange(0, wh, size)  # Initial food position

clock = pg.time.Clock()  # Creating clock for time control in the game

score = 0  
level = 1  
foods_to_next_level = 3  
timer = pg.time.get_ticks() #get current time
font = pg.font.Font(None, 36) 

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()  

    screen.fill((0, 0, 0)) 

    pg.draw.rect(screen, (255, 0, 0), (point_x, point_y, size, size))  #draw the food
    for segment in segments:
        pg.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], size, size))  #draw the snake

    head = segments[0]
    new_head = (head[0] + dx * size, head[1] + dy * size)  #calculate the new position of the snake's head
    segments.insert(0, new_head)
    
    #check if the snake has eaten the food
    if new_head[0] == point_x and new_head[1] == point_y:
        point_x, point_y = randrange(0, wh, size), randrange(0, wh, size)  
        score += 1  
        if score % foods_to_next_level == 0:  
            level += 1  
            speed += 2  
            foods_to_next_level += 2  
        for _ in range(randrange(0,2)):  
            segments.append(segments[-1]) 
        
    else:
        segments.pop() 

    #check if 8 seconds passed
    if pg.time.get_ticks() - timer > 8000:
        point_x, point_y = randrange(0, wh, size), randrange(0, wh, size)
        timer = pg.time.get_ticks()

    if (new_head[0] < 0 or new_head[0] >= wh or
        new_head[1] < 0 or new_head[1] >= wh):
        exit() 
    if new_head in segments[1:]:
        exit()  


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    len_text = font.render(f"Size: {len(segments)}", True, (255,255,255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))
    screen.blit(len_text, (10, 90))

    pg.display.update()  
    clock.tick(speed)  

    #check for keyboard input to change the direction of the snake
    key = pg.key.get_pressed()
    if key[pg.K_w]:
        dx, dy = 0, -1
    if key[pg.K_s]:
        dx, dy = 0, 1
    if key[pg.K_a]:
        dx, dy = -1, 0
    if key[pg.K_d]:
        dx, dy = 1, 0