import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Константи
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = -20
PLAYER_SIZE = 50
GROUND_HEIGHT = 50

# Налаштуваня екрану
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Міні-Даш")
clock = pygame.time.Clock()

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Oб'єкт гравця
player_x = 50
player_y = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_SIZE
player_y_velocity = 0
is_jumping = False

# Основний цикл гри
running = True
while running:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Стрибок по пробілу
            if event.key == pygame.K_SPACE and not is_jumping:
                player_y_velocity = JUMP_STRENGTH
                is_jumping = True

    # 1. Рух гравця (Автоматичний рух вправо)
    player_x += 5 # Постійна швидкість

    # 2. Гравітація та стрибок
    player_y_velocity += GRAVITY
    player_y += player_y_velocity

    # 3. Перевірка зіткнення з землею
    if player_y >= SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_SIZE:
        player_y = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_SIZE
        player_y_velocity = 0
        is_jumping = False
    
    # 4. Прокрутка рівня (якщо гравець виходить за межі екрану, починаємо знову)
    if player_x > SCREEN_WIDTH:
        player_x = 50 # Рестарт позиції для мінімалістичної "нескінченної" гри

    # Відображення
    screen.fill(WHITE)

    # Малювання землі
    ground_rect = pygame.Rect(0, SCREEN_HEIGHT - GROUND_HIGHT, SCREEN_WIDTH, GROUND_HEIGHT)
    pygame.draw.rect(screen, BLACK, ground_rect)

    # Малювання гравця
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Оновлення екрану
    pygame.dysplay.flip()

    # Обмеження FPS
    clock.tick(FPS)

# Вихід з Pygame
pygame.quit()
sys.exit()
