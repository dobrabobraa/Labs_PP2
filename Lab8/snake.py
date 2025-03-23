import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Константы игры
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 10  # Размер одной клетки

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

# Шрифты
font = pygame.font.Font(None, 30)

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10  # Начальная скорость

# Начальная генерация еды

def generate_food():
    while True:
        food = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE, 
                random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
        if food not in snake_body:  # Проверяем, чтобы еда не появилась на змее
            return food

food_pos = generate_food()
game_score = 0
level = 1

isRunning = True

while isRunning:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Движение змеи
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= CELL_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= CELL_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    # Вставляем новую позицию головы змеи
    snake_body.insert(0, list(snake_pos))

    # Проверка, съела ли змея еду
    if snake_pos == food_pos:
        game_score += 1
        food_pos = generate_food()
    else:
        snake_body.pop()

    # Проверка столкновения со стенами
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    # Проверка столкновения с собой
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Проверка уровня (каждые 3 очка)
    new_level = game_score // 3 + 1
    if new_level > level:
        level = new_level
        speed += 2  # Увеличиваем скорость при повышении уровня

    # Отрисовка экрана
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)  # Регулировка скорости игры

# Экран окончания игры
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
