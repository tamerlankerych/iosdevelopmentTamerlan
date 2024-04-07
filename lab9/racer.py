import random
import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 400, 600

# Создание основного экрана и экрана проигрыша
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LOSS_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Установка цветов
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Переменные для очков и жизней игрока
SCORE = 0
LIFE = 3

# Создание часов для управления фреймрейтом
clock = pygame.time.Clock()

# Загрузка изображения фона
background = pygame.image.load('./materials/AnimatedStreet.png')

# Загрузка звуков
background_sound = pygame.mixer.Sound("./materials/background.wav")
crush_sound = pygame.mixer.Sound("./materials/crash.wav")

# Переменная для управления движением фона
background_y = 0

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.randint(6,8)
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 7
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)

# Группа для монет
coins = pygame.sprite.Group()

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.randint(5, 8)
        self.random_number = random.randint(0, 6)
        if self.random_number in [0,1,2]:
            self.image = pygame.image.load("./materials/coin.png")
        else:
            self.image = pygame.image.load("./materials/cent.png")
        self.resized_image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.resized_image.get_rect()
        if WIDTH - self.rect.width > self.rect.width:
            x = random.randint(self.rect.width, WIDTH - self.rect.width)
        else:
            x = random.randint(WIDTH - self.rect.width, self.rect.width)
        self.rect.center = (x, 0)

    def draw(self, surface):
        surface.blit(self.resized_image, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            global LIFE
            LIFE -= 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )

    def collide(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.kill()  # Удаляем спрайт из всех групп, к которым он принадлежит
            return True
        
        return False
    
    def is_mega_coin(self):
        return self.random_number in [0,1,2]

def main():
    global background_y
    global coins

    # Флаг для управления основным циклом
    running = True

    # Создание игрока, врага и монеты
    player = Player()
    enemy = Enemy()
    coin = Coin()

    # Создание группы врагов и добавление в неё врага
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    # Добавление монеты в группу
    coins.add(coin)

    # Воспроизведение фоновой музыки
    background_sound.play(-1)

    while running:
        global SCORE
        global LIFE

        # Заливка экрана белым цветом
        SCREEN.fill(WHITE)

        # Отображение фона
        background_rect = background.get_rect()
        SCREEN.blit(background, (0, background_y))
        SCREEN.blit(background, (0, background_y - background_rect.height)) 
        background_y += 4  

        # Обновление координаты фона для создания эффекта движения
        if background_y > background_rect.height:
            background_y = 0
        
        # Отображение текущего счета и количества жизней игрока
        # Создание шрифта для отображения текущего счета игрока
        score_font = pygame.font.SysFont("Verdana", 30)
        score = score_font.render(f"Your score: {SCORE}", True, BLACK)
        SCREEN.blit(score, (0, 0))
        # Создание шрифта для отображения количества жизней игрока
        life_font = pygame.font.SysFont("Verdana", 30)       
        life = life_font.render(f"Your life: {LIFE}", True, BLACK)
        SCREEN.blit(life, (0, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or LIFE == 0:
                running = False

        # Обновление игрока и врага
        player.update()
        enemy.update()

        # Создание новой монеты после сбора текущей
        for coin in coins:
            if coin.collide(player):
                coins.remove(coin)
                SCORE += 1
                coins.add(Coin())
                if coin.is_mega_coin():
                    SCORE += 4
        
        # Увеличение скорости врага при достижении определенного счета
        if SCORE > 30:
            enemy.speed = random.randint(8, 11)

        # Завершение игры при окончании жизней игрока
        if LIFE == 0:
            running = False

        # Отображение и обновление монеты, игрока и врага
        coin.draw(SCREEN)
        coin.update()
        player.draw(SCREEN)
        enemy.draw(SCREEN)

        # Завершение игры при столкновении игрока с врагом
        if pygame.sprite.spritecollide(player, enemies, False):
            background_sound.stop() 
            crush_sound.play() 
            pygame.time.wait(2000)
            running = False
        
        # Отображение экрана
        pygame.display.flip()
        clock.tick(60)

# Запуск основной функции игры
main()