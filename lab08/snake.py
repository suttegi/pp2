import pygame as pg 
from random import randrange

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

score = 0  # Initializing score
level = 1  # Initializing level
foods_to_next_level = 3  # Amount of food eaten to reach next level  

font = pg.font.Font(None, 36)  # Setting font for text rendering

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()  # Exit the game if the user closes the window

    screen.fill((0, 0, 0))  # Fill the screen with black color

    pg.draw.rect(screen, (255, 0, 0), (point_x, point_y, size, size))  # Draw the food
    for segment in segments:
        pg.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], size, size))  # Draw the snake

    head = segments[0]
    new_head = (head[0] + dx * size, head[1] + dy * size)  # Calculate the new position of the snake's head
    segments.insert(0, new_head)  # Insert the new head position into the segments list
    
    # Check if the snake has eaten the food
    if new_head[0] == point_x and new_head[1] == point_y:
        point_x, point_y = randrange(0, wh, size), randrange(0, wh, size)  # Generate new food position
        score += 1  # Increment the score
        if score % foods_to_next_level == 0:  # Check if the score reaches the threshold for the next level
            level += 1  # Increment the level
            speed += 2  # Increase the speed
            foods_to_next_level += 2  # Increase the threshold for the next level
        
    else:
        segments.pop()  # Remove the tail segment of the snake if it hasn't eaten food

    # Check for collisions with screen boundaries or itself
    if (new_head[0] < 0 or new_head[0] >= wh or
        new_head[1] < 0 or new_head[1] >= wh):
        exit()  # Exit the game if the snake collides with the screen boundaries
    if new_head in segments[1:]:
        exit()  # Exit the game if the snake collides with itself

    # Render score and level text on the screen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pg.display.update()  # Update the display
    clock.tick(speed)  # Control the game speed

    # Check for keyboard input to change the direction of the snake
    key = pg.key.get_pressed()
    if key[pg.K_w]:
        dx, dy = 0, -1
    if key[pg.K_s]:
        dx, dy = 0, 1
    if key[pg.K_a]:
        dx, dy = -1, 0
    if key[pg.K_d]:
        dx, dy = 1, 0
