import pygame as pg
from math import cos, sin , pi 

# Инициализация Pygame
pg.init()

# Создание окна размером 800x600 пикселей
screen = pg.display.set_mode((800, 600))

# Установка шрифта для текста
font = pg.font.SysFont("Verdana", 15)

# Цвет для рисования по умолчанию
cur_color = 'white'

# Функция для вычисления расстояния между двумя точками
def get_distance(a,b): 
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

# Функция для рисования прямоугольного треугольника
def right_triangle(screen, cur, end, d, color): 
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    dify = abs(y1-y2) 
    if y1 < y2: 
        pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
    else: 
        pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    

# Функция для рисования треугольника
def triangle(color, pos):
    pg.draw.polygon(screen, color, pos, 3)

# Функция для рисования квадрата
def square(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, a, a), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, a, a), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, a, a), d)

# Функция для рисования ромба
def rhombus(color, pos):
    pg.draw.polygon(screen, color, pos, 3)

last_pos = (0, 0)
w = 2

# Словарь для отслеживания текущей выбранной фигуры
di = {
    'sqr': False,
    'triangle': False,
    'rhombus': False,
    'right_triangle': False
}

# Заливка экрана черным цветом
screen.fill((0,0,0))

running = True
while running:
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
                  
        if event.type == pg.KEYDOWN:
            # Установка выбранной фигуры при нажатии соответствующих клавиш
            if event.key == pg.K_1:
                di['sqr'] = True
                for i, j in di.items(): 
                    if i != 'sqr':
                        di[i] = False
            if event.key == pg.K_2:
                di['triangle'] = True
                for i, j in di.items():
                    if i != 'triangle':
                        di[i] = False
            if event.key == pg.K_3:
                di['rhombus'] = True
                for i, j in di.items():
                    if i != 'rhombus':
                        di[i] = False
            if event.key == pg.K_4:
                di['right_triangle'] = True
                for i, j in di.items():
                    if i != 'right_triangle':
                        di[i] = False
            
                
        elif di['sqr'] == True:
            # Рисование квадрата при нажатии и отпускании кнопки мыши
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                square(screen, last_pos, pos, w, cur_color)
                
        elif di['triangle'] == True:
            # Рисование треугольника при нажатии и отпускании кнопки мыши
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                # Рассчет координат для треугольника
                triangle(cur_color,[last_pos, pos,((pos[0] - last_pos[0])*cos(pi/3) - (pos[1] - last_pos[1])*sin(pi/3) + last_pos[0], (pos[0] - last_pos[0])*sin(pi/3) + (pos[1] - last_pos[1])*cos(pi/3) + last_pos[1])])
                
        if di['right_triangle'] == 1:
            # Рисование прямоугольного треугольника при нажатии и отпускании кнопки мыши
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                right_triangle(screen, last_pos, pos, w, cur_color)
                
        elif di['rhombus'] == 1:
            # Рисование ромба при нажатии и отпускании кнопки мыши
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                # Рассчет координат для ромба
                rhombus(cur_color, [last_pos, (last_pos[0] + d, last_pos[1]), (pos[0] + d, pos[1]), pos])
                
        # Вывод текста с инструкциями для пользователя
        txt = font.render("square - 1 right triangle - 2 rhombus - 3 equivalent triangle - 4", True, (255,0,0))
        screen.blit(txt, (0,0))

    pg.display.update()

# Выход из Pygame
pg.quit()
