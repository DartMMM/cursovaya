import pygame
import sys
from pygame.locals import *

# Константы
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CAR_SPEED = 2

class Car:
    def init(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 30, 20)
        self.direction = direction  # 1 - вправо, -1 - влево
        self.color = GREEN
        self.speed = CAR_SPEED if direction == 1 else -CAR_SPEED

    def move(self):
        self.rect.x += self.speed

        # Если машина выехала за пределы экрана
        if (self.direction == 1 and self.rect.left > WINDOW_WIDTH) or \
           (self.direction == -1 and self.rect.right < 0):
            return False  # Удалить машину
        return True

def create_button(x, y, w, h):
    return pygame.Rect(x, y, w, h)

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Traffic Light Optimization")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Состояния
    is_welcome = True
    cars_left = []  # Машины, движущиеся вправо
    cars_right = []  # Машины, движущиеся влево

    # Светофоры (True - зеленый)
    light_left = False  # Для машин слева (движение вправо)
    light_right = True  # Для машин справа (движение влево)

    # Таймер для светофоров
    light_timer = 0
    light_change_time = 3000  # 3 секунды

    # Кнопки и ползунки
    start_btn = create_button(325, 400, 150, 50)
    exit_btn = create_button(600, 500, 150, 50)
    slider1 = pygame.Rect(100, 500, 200, 20)
    slider2 = pygame.Rect(100, 550, 200, 20)
    density_left = 50
    density_right = 50
    dragging = None

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        # Автоматическое переключение светофоров
        if current_time - light_timer > light_change_time:
            light_left = not light_left
            light_right = not light_right
            light_timer = current_time

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if is_welcome and start_btn.collidepoint(event.pos):
                    is_welcome = False
                elif not is_welcome and exit_btn.collidepoint(event.pos):
                    running = False

                if slider1.collidepoint(event.pos):
                    dragging = "slider1"
                elif slider2.collidepoint(event.pos):
                    dragging = "slider2"

            if event.type == MOUSEBUTTONUP:
                dragging = None

            if event.type == MOUSEMOTION and dragging:
                if dragging == "slider1":
                    density_left = max(0, min(100, (event.pos[0] - slider1.x) / 2))
                elif dragging == "slider2":
                    density_right = max(0, min(100, (event.pos[0] - slider2.x) / 2))

        # Генерация новых машин
        if not is_welcome:
            if len(cars_left) < density_left and pygame.time.get_ticks() % 30 == 0:
                cars_left.append(Car(-30, 300, 1))

            if len(cars_right) < density_right and pygame.time.get_ticks() % 30 == 0:
                cars_right.append(Car(WINDOW_WIDTH, 350, -1))

        # Движение машин
        cars_left = [car for car in cars_left if car.move() or (not light_left and car.rect.right < 350)]
        cars_right = [car for car in cars_right if car.move() or (not light_right and car.rect.left > 450)]

        # Отрисовка
        window.fill(BLACK)

        if is_welcome:
            title = font.render("Traffic Light Optimization", True, WHITE)
            window.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
pygame.draw.rect(window, BLUE, start_btn)
            start_text = font.render("Start", True, WHITE)
            window.blit(start_text, (start_btn.x + 50, start_btn.y + 15))
        else:
            # Дорога
            pygame.draw.rect(window, (50, 50, 50), (0, 290, WINDOW_WIDTH, 100))
            pygame.draw.line(window, WHITE, (0, 340), (WINDOW_WIDTH, 340), 2)

            # Светофоры
            pygame.draw.rect(window, (70, 70, 70), (340, 200, 60, 100))
            pygame.draw.circle(window, RED if not light_left else BLACK, (370, 230), 15)
            pygame.draw.circle(window, GREEN if light_left else BLACK, (370, 270), 15)

            pygame.draw.rect(window, (70, 70, 70), (440, 200, 60, 100))
            pygame.draw.circle(window, RED if not light_right else BLACK, (470, 230), 15)
            pygame.draw.circle(window, GREEN if light_right else BLACK, (470, 270), 15)

            # Машины
            for car in cars_left:
                pygame.draw.rect(window, car.color, car.rect)
                # Фары
                pygame.draw.rect(window, WHITE, (car.rect.right-5, car.rect.top+5, 5, 10))

            for car in cars_right:
                pygame.draw.rect(window, car.color, car.rect)
                # Фары
                pygame.draw.rect(window, WHITE, (car.rect.left, car.rect.top+5, 5, 10))

            # Ползунки
            pygame.draw.rect(window, WHITE, slider1)
            pygame.draw.rect(window, (int(255 * density_left / 100), 0, 0),
                           (slider1.x, slider1.y, int(density_left * 2), slider1.height))

            pygame.draw.rect(window, WHITE, slider2)
            pygame.draw.rect(window, (int(255 * density_right / 100), 0, 0),
                           (slider2.x, slider2.y, int(density_right * 2), slider2.height))

            # Текст
            left_text = font.render(f"Left: {int(density_left)}", True, WHITE)
            right_text = font.render(f"Right: {int(density_right)}", True, WHITE)
            window.blit(left_text, (slider1.x, slider1.y - 30))
            window.blit(right_text, (slider2.x, slider2.y - 30))

            # Кнопка выхода
            pygame.draw.rect(window, BLUE, exit_btn)
            exit_text = font.render("Exit", True, WHITE)
            window.blit(exit_text, (exit_btn.x + 50, exit_btn.y + 15))

        pygame.display.flip()
        clock.tick(60)

if name == "main":
    main()
    pygame.quit()
    sys.exit()