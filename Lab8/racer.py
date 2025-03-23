import pygame
import random

pygame.init()

# Окно игры
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Загрузка изображений
bg_image = pygame.image.load('C:/Users/Диас/Documents/Labs/labs_PP2/Lab8/images/bg_image.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

player = pygame.image.load('C:/Users/Диас/Documents/Labs/labs_PP2/Lab8/images/playes_car.png')
player = pygame.transform.scale(player, (150, 150))

enemy_img = pygame.image.load('C:/Users/Диас/Documents/Labs/labs_PP2/Lab8/images/enemy_car.png')
enemy_img = pygame.transform.scale(enemy_img, (130, 130))
enemy_img = pygame.transform.rotate(enemy_img, 180)

coin_img = pygame.image.load('C:/Users/Диас/Documents/Labs/labs_PP2/Lab8/images/coins.png')
coin_img = pygame.transform.scale(coin_img, (50, 50))

# Полосы дороги
lanes = [200, 350, 500, 650]

# Игровые переменные
player_x, player_y = 500, 850
speed = 10
num_enemies = 3
enemy_speed = 15
game_over = False
score = 0  # Счетчик монет
enemies = []  # Список врагов

# Функция создания врагов (всегда 3)
def spawn_enemies():
    global enemies  
    enemies = [(random.choice(lanes), random.randint(-500, -100)) for _ in range(num_enemies)]

# Создаем врагов перед началом игры
spawn_enemies()

# Создание монеты сразу при запуске
coin = (random.choice(lanes)+10, random.randint(200, 800))

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(bg_image, (0, 0))

    if game_over:
        # Отображение текста "Game Over"
        font = pygame.font.Font(None, 80)
        text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(text, (100, HEIGHT // 2))
    else:
        # Отображение машины игрока
        screen.blit(player, (player_x, player_y))

        # Отображение монеты
        screen.blit(coin_img, coin)

        # Рисуем врагов
        for enemy in enemies:
            screen.blit(enemy_img, enemy)

        # Движение врагов
        new_enemies = []
        for x, y in enemies:
            y += enemy_speed  
            if y > HEIGHT:
                new_enemies.append((random.choice(lanes), random.randint(-500, -100)))
            else:
                new_enemies.append((x, y))
        enemies = new_enemies  

        # Проверка столкновений
        player_rect = pygame.Rect(player_x, player_y, 100, 150)
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], 100, 150)
            if player_rect.colliderect(enemy_rect):
                game_over = True  

        # Проверка сбора монеты
        coin_rect = pygame.Rect(coin[0], coin[1], 50, 50)
        if player_rect.colliderect(coin_rect):
            score += 1  # Увеличиваем счет
            coin = (random.choice(lanes), random.randint(200, 800))  # Новая монета

        # Отображение счета
        font = pygame.font.Font(None, 50)
        score_text = font.render(f"Score: {score}", True, (255, 255, 0))
        screen.blit(score_text, (20, 20))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_w] and player_y > 0:
            player_y -= speed
        if keys[pygame.K_s] and player_y < HEIGHT - 150:
            player_y += speed
        if keys[pygame.K_a] and player_x > 200:
            player_x -= speed
        if keys[pygame.K_d] and player_x < 650:
            player_x += speed
    else:
        if keys[pygame.K_r]:  # Перезапуск игры при нажатии R
            player_x, player_y = 500, 850
            spawn_enemies()
            coin = (random.choice(lanes), random.randint(200, 800))  # Новая монета после рестарта
            score = 0  # Обнуление счета
            game_over = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
