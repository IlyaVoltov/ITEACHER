import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Стратегия на Python")

# Цвета
white = (255, 255, 255)
bg_color = (200, 200, 255)  # Нежный голубой фон
green = (0, 150, 0)
red = (200, 0, 0)
highlight_color = (255, 255, 0)  # Жёлтая подсветка

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Регионы
regions = [
    {"name": "Germany", "x": 100, "y": 100, "color": green},
    {"name": "France", "x": 300, "y": 100, "color": red},
    {"name": "Spain", "x": 100, "y": 300, "color": green},
    {"name": "Russia", "x": 300, "y": 300, "color": red}
]

# Основной цикл
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем координаты курсора
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем фон
    screen.fill(bg_color)

    # Рисуем регионы
    for region in regions:
        rect = pygame.Rect(region["x"], region["y"], 100, 100)

        # Проверяем, находится ли мышь над регионом
        if rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, highlight_color, rect, border_radius=15)
        else:
            pygame.draw.rect(screen, region["color"], rect, border_radius=15)

        # Отображаем название региона
        text = font.render(region["name"], True, white)
        screen.blit(text, (region["x"] + 10, region["y"] + 35))

    # Обновляем экран
    pygame.display.flip()

pygame.quit()
