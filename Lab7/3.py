import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")

ball_x, ball_y = 400, 300
speed = 20
ball_R = 25


running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_R - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_R + speed <= 600:
        ball_y += speed
    if keys[pygame.K_LEFT] and ball_x - ball_R - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_R + speed <= 800:
        ball_x += speed
    

    screen.fill('White')
    pygame.draw.circle(screen, 'Red', (ball_x, ball_y), ball_R)
    pygame.display.update()

pygame.quit()
