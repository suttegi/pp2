import pygame as pg 

pg.init()

#set up the screen
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

#fill the screen with white color
screen.fill((255,255,255))

#create a panel surface for buttons
panel = pg.Surface((800,100))

#buttons for switching colors
red_button = pg.draw.rect(panel,(255,0,0),(10,10,30,30))
green_button = pg.draw.rect(panel,(0,255,0),(50,10,30,30))
blue_button = pg.draw.rect(panel,(0,0,255),(90,10,30,30))
eraser_button = pg.draw.rect(panel,(255,255,255),(130,10,30,30))
color = (0,0,0)

#buttons for switching drawing shape
rect_button = pg.draw.rect(panel, (128, 128, 128), (170, 10, 30, 30))
circle_button = pg.draw.circle(panel, (128, 128, 128), (220, 25),15)
square_button = pg.draw.rect(panel,(128,128,128),(250,10,30,30))
rtriangle_button = pg.draw.polygon(panel,(128,128,128),((300,10),(300,40),(330,40)))
etriangle_button = pg.draw.polygon(panel,(128,128,128),((365,10),(350,40),(380,40)))
rhombus_button = pg.draw.polygon(panel,(128,128,128),((400,25),(425,10),(450,25),(425,40)))



#options
radius = 0
drawing = False
start_pos = (0,0)
shape = 'line'

#game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos)
            if red_button.collidepoint(event.pos):
                color = (255,0,0)
            elif green_button.collidepoint(event.pos):
                color = (0,255,0)
            elif blue_button.collidepoint(event.pos):
                color = (0,0,255)
            elif eraser_button.collidepoint(event.pos):
                screen.fill((255,255,255))
            elif rect_button.collidepoint(event.pos):
                shape = 'rect'
            elif circle_button.collidepoint(event.pos):
                shape = 'circle'
            elif square_button.collidepoint(event.pos):
                shape = 'square'
            elif rtriangle_button.collidepoint(event.pos):
                shape = 'rtriangle'
            elif etriangle_button.collidepoint(event.pos):
                shape = 'etriangle'
            elif rhombus_button.collidepoint(event.pos):
                shape = 'rhombus'
            else:
                drawing = True
                start_pos = event.pos
        elif event.type == pg.MOUSEBUTTONUP:
            drawing = False

    if drawing:
        
        if pg.mouse.get_pressed()[0]:
            if shape == 'line':
                pg.draw.line(screen, color, start_pos, event.pos, 3)
                start_pos = event.pos
            elif shape == 'rect':
                start_x = min(start_pos[0], event.pos[0])
                start_y = min(start_pos[1], event.pos[1])
                w = abs(start_pos[0] - event.pos[0])
                h = abs(start_pos[1] - event.pos[1])

                pg.draw.rect(screen, color, (start_x, start_y, w, h))
            elif shape == 'circle':
                #radius = hypotenus
                radius = ((start_pos[0]-event.pos[0])**2+(start_pos[1]-event.pos[1])**2)**0.5
                pg.draw.circle(screen,color,(start_pos), radius)
            elif shape == 'square':
                whs = abs(start_pos[0]-event.pos[0])
                start_x = min(start_pos[0], event.pos[0])
                start_y = min(start_pos[1], event.pos[1])
                pg.draw.rect(screen,color,(start_x,start_y,whs,whs))
            elif shape == 'rtriangle':
                pg.draw.polygon(screen,color,((start_pos),(start_pos[0],event.pos[1]),(event.pos)))
            elif shape == 'etriangle':
                mid_point = ((start_pos[0] + event.pos[0]) / 2, start_pos[1])
                height = int((3 ** 0.5 / 2) * abs(event.pos[0] - start_pos[0]))
                vertices = [(mid_point[0], start_pos[1] - height),
                            (start_pos[0], event.pos[1]),
                            (event.pos[0], event.pos[1])]
                pg.draw.polygon(screen, color, vertices)

            elif shape == 'rhombus':
                mid_point = ((start_pos[0] + event.pos[0]) / 2, (start_pos[1] + event.pos[1]) / 2)
                width = abs(start_pos[0] - event.pos[0])
                height = abs(start_pos[1] - event.pos[1])
                vertices = [(mid_point[0], mid_point[1] - height),  
                            (start_pos[0], mid_point[1]),          
                            (mid_point[0], mid_point[1] + height), 
                            (event.pos[0], mid_point[1])]         
                pg.draw.polygon(screen, color, vertices)

            
    screen.blit(panel,(0,0))
    pg.display.update()
    clock.tick(60)
