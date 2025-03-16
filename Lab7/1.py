import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1300,1000))
clock = pygame.time.Clock()


font = pygame.font.SysFont('Verdana', 50)
mainclock=pygame.image.load('C:/Users/Диас/Desktop/pygame/images/clock.png')
clock_arrow_second=pygame.image.load('C:/Users/Диас/Desktop/pygame/images/leftarm.png')
clock_arrow_minutes=pygame.image.load('C:/Users/Диас/Desktop/pygame/images/rightarm.png')




center=(700, 500)

def rotate_image(image, angle, pos):
    rotated_image=pygame.transform.rotate(image, angle)
    new_rec=rotated_image.get_rect(center=pos)
    return rotated_image, new_rec

running = True
while running:

    screen.fill('White')

    time = datetime.now()
    timerender = font.render(f'{time:%H:%M:%S}', True, 'Green')
    minutes=time.minute
    seconds=time.second

    minute_angle = -minutes * 6- 60
    second_angle = -seconds*6 

    second_rotated, second_rect=rotate_image(clock_arrow_second, second_angle, center)
    minute_rotated, minute_rect=rotate_image(clock_arrow_minutes, minute_angle, center)

    screen.blit(mainclock,(0,0))
    screen.blit(second_rotated, second_rect)
    screen.blit(minute_rotated, minute_rect)



    screen.blit(timerender, (0, 0))

    

    pygame.display.flip()
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
