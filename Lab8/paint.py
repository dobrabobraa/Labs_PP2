import pygame 

WIDTH, HEIGHT = 1200, 800  
FPS = 120  
draw = False              
radius = 5    
color = 'blue'           
mode = 'pen'                

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint')  
clock = pygame.time.Clock()  
screen.fill(pygame.Color('white'))  
font = pygame.font.SysFont(None, 60) 

def drawLine(screen, start, end, width, color): 
    x1, y1 = start 
    x2, y2 = end  
    dx, dy = abs(x1 - x2), abs(y1 - y2)  
    A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2  
    
    if dx > dy:  
        if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1  
        for x in range(x1, x2):  
            y = int((-C - A * x) / B)  
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)  
    else:  
        if y1 > y2: x1, x2, y1, y2 = x2, x1, y2, y1  
        for y in range(y1, y2):  
            x = int((-C - B * y) / A)  
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)  

def drawCircle(screen, start, end, width, color):  
    x1, y1 = start  
    x2, y2 = end  
    x, y = (x1 + x2) // 2, (y1 + y2) // 2  
    radius = int(abs(x1 - x2) / 2)  
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  

def drawRectangle(screen, start, end, width, color):  
    x1, y1 = start  
    x2, y2 = end  
    widthr, height = abs(x1 - x2), abs(y1 - y2)  
    x, y = min(x1, x2), min(y1, y2)  
    pygame.draw.rect(screen, pygame.Color(color), (x, y, widthr, height), width)  

lastPos = (0, 0)

while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            exit()  
         
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_r: mode = 'rectangle'  
            if event.key == pygame.K_c: mode = 'circle'  
            if event.key == pygame.K_p: mode = 'pen'  
            if event.key == pygame.K_e: mode = 'erase'  
            if event.key == pygame.K_q:  
                screen.fill(pygame.Color('white'))  
                pygame.display.update()  

            if event.key == pygame.K_1: color = 'black'  
            if event.key == pygame.K_2: color = 'green'  
            if event.key == pygame.K_3: color = 'red'  
            if event.key == pygame.K_4: color = 'blue'  
            if event.key == pygame.K_5: color = 'yellow'  

        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  
            prevPos = event.pos  
            if mode == 'pen':  
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  
            lastPos = event.pos  

        if event.type == pygame.MOUSEBUTTONUP:  
            draw = False  
            if mode == 'rectangle':  
                drawRectangle(screen, prevPos, event.pos, radius, color)  
            elif mode == 'circle':  
                drawCircle(screen, prevPos, event.pos, radius, color)  

        if event.type == pygame.MOUSEMOTION:  
            if draw:  
                if mode == 'pen':  
                    drawLine(screen, lastPos, event.pos, radius, color)  
                elif mode == 'erase':  
                    drawLine(screen, lastPos, event.pos, radius, 'white')  
            lastPos = event.pos  

    pygame.display.flip()  
    clock.tick(FPS)  
