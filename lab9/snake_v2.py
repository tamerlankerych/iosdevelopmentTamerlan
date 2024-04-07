import random
import pygame

pygame.init()
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 0, 127)
FPS = 6
SCORE = 0
LEVEL = 1
BLOCK_SIZE = 20

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LOSS_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background_sound = pygame.mixer.Sound("./materials/Snake Game - Theme Song.mp3")
background_sound = pygame.mixer.music.load("./materials/Snake Game - Theme Song.mp3")
eat_sound = pygame.mixer.Sound("./materials/snake-hissing-6092.mp3")
pygame.display.set_caption('Snake')
score_font = pygame.font.SysFont('Verdana', 20)
level_font = pygame.font.SysFont('Verdana', 20)
pause_font = pygame.font.SysFont('Verdana', 30)
settings_font = pygame.font.SysFont('Verdana', 20)
running = True
paused = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Fruit:
    def __init__(self, x, y, colour, score, timer, max_timer):
        self.location = Point(x, y)
        self.colour = colour
        self.score = score
        self.timer = timer
        self.max_timer = max_timer
    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            self.colour,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    def update(self):
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        self.timer = 0
    def time(self, dt):
        self.timer += dt
        if self.timer >= self.max_timer:
            self.update()
            self.timer = 0
    def level(self):
        global SCORE
        global LEVEL
        global FPS
        if SCORE % 5 == 0:
            LEVEL += 1
            FPS += 2

class Food(Fruit):
    def __init__(self):
        super().__init__(10, 10, YELLOW, 1, 0, 5)

class Poison(Fruit):
    def __init__(self):
        super().__init__(20, 20, GREEN, -1, 0, 5)

class Booster(Fruit):
    def __init__(self):
        super().__init__(20, 10, LIGHTBLUE, 5, 0, 5)

class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        global running
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy
        
        head = self.points[0]
        if head.x >= WIDTH // BLOCK_SIZE or head.x < 0 or head.y >= HEIGHT // BLOCK_SIZE or head.y < 0:
            running = False

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (WIDTH, y), width=1)

def settings_menu():
    global BLOCK_SIZE, FPS
    selected_option = 0
    options = ['Block Size', 'Speed']
    values = [BLOCK_SIZE, FPS]
    running_settings_menu = True

    while running_settings_menu:
        SCREEN.fill(WHITE)
        for i, option in enumerate(options):
            text = settings_font.render(option + ': ' + str(values[i]), True, BLACK)
            SCREEN.blit(text, (150, 150 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running_settings_menu = False
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_LEFT:
                    values[selected_option] -= 1
                    if values[selected_option] < 1:
                        values[selected_option] = 1
                elif event.key == pygame.K_RIGHT:
                    values[selected_option] += 1
            elif event.type == pygame.QUIT:
                running_settings_menu = False

    BLOCK_SIZE = values[0]
    FPS = values[1]

def main_menu():
    global paused, running
    selected_option = 0
    options = ['Start', 'Settings', 'Quit']
    running_main_menu = True

    while running_main_menu:
        SCREEN.fill(WHITE)
        for i, option in enumerate(options):
            color = BLACK if i == selected_option else WHITE
            text = settings_font.render(option, True, color)
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, 150 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        running_main_menu = False
                    elif selected_option == 1:
                        settings_menu()
                    elif selected_option == 2:
                        running = False
                        running_main_menu = False
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
            elif event.type == pygame.QUIT:
                running = False
                running_main_menu = False

def main():
    global SCORE
    global LEVEL
    global FPS
    global running
    global paused
    main_menu()  # Show main menu first
    snake = Snake()
    food = Food()
    poison = Poison()
    booster = Booster()
    dx, dy = 0, 0
    dt = 1
    food.time(dt)   
    poison.time(dt)
    booster.time(dt)

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not paused:
                    if event.key == pygame.K_UP:
                        dx, dy = 0, -1
                    elif event.key == pygame.K_DOWN:
                        dx, dy = 0, +1
                    elif event.key == pygame.K_LEFT:
                        dx, dy = -1, 0
                    elif event.key == pygame.K_RIGHT:
                        dx, dy = +1, 0
                    elif event.key == pygame.K_s:
                        settings_menu()  # Open settings menu on 'S' key press
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if not paused:
            snake.move(dx, dy)
            if snake.check_collision(food):
                eat_sound.play()
                SCORE += food.score
                snake.points.append(Point(food.x, food.y))
                food.update()
                food.level()
            if snake.check_collision(booster):
                eat_sound.play()
                SCORE += booster.score
                snake.points.append(Point(booster.x, booster.y))
                booster.update()
                booster.level()
            if snake.check_collision(poison):
                eat_sound.play()
                SCORE += poison.score
                snake.points.remove(snake.points[len(snake.points)-1])
                poison.update()
                poison.level()

        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        level = level_font.render(f" Level: {LEVEL}", True, (0, 0, 0))

        SCREEN.blit(score, (0, 0))
        SCREEN.blit(level, (20, 20))

        food.draw()
        snake.update()
        poison.draw()
        booster.draw()
        draw_grid()

        if paused:
            pause_text = pause_font.render("PAUSED", True, BLACK)
            SCREEN.blit(pause_text, ((WIDTH - pause_text.get_width()) // 2, (HEIGHT - pause_text.get_height()) // 2))

        pygame.display.flip()
        clock.tick(FPS)

main()
