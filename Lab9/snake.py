import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10

game_score = 0
level = 1

# Генерация еды с разным весом, некоторые из которых исчезают через время

def generate_food():
    value = random.randint(1, 3)
    food = [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]
    timed = random.choice([True, False])  # Определяем, будет ли еда с таймером
    if timed:
        lifetime = 5000  # Таймер 5 секунд для исчезающей еды
    else:
        lifetime = None
    if food not in snake_body:
        return food, value, pygame.time.get_ticks() if timed else None, lifetime
    return generate_food()

food_pos, food_value, food_timer, food_lifetime = generate_food()
isRunning = True

while isRunning:
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

    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= CELL_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= CELL_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    snake_body.insert(0, list(snake_pos))

    # Проверка съеденной еды
    if snake_pos == food_pos:
        game_score += food_value
        food_pos, food_value, food_timer, food_lifetime = generate_food()
    else:
        snake_body.pop()

    # Проверка истечения времени еды, если она с таймером
    if food_timer is not None and pygame.time.get_ticks() - food_timer > food_lifetime:
        food_pos, food_value, food_timer, food_lifetime = generate_food()

    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    new_level = game_score // 3 + 1
    if new_level > level:
        level = new_level
        speed += 2

    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], CELL_SIZE, CELL_SIZE))
    color = RED if food_timer is not None else WHITE
    pygame.draw.rect(screen, color, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)

screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
