import pygame.mixer
from pygame import mixer, mixer_music

mixer.init()
sound1 = pygame.mixer.Sound("sounds/2.mp3")
sound2 = pygame.mixer.Sound("sounds/3.mp3")
soundbg = pygame.mixer.Sound("sounds/bc.mp3")
soundgo = pygame.mixer.Sound("sounds/piy.mp3")


from win32api import GetSystemMetrics
WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)


# ширина ракетки
# 1980\30  W\x
PAD_W = (20*WIDTH)/1980
# высота ракетки
PAD_H = (200*HEIGHT)/1050

# радиус мяча
BALL_RADIUS = 25*WIDTH/1980
center_x = WIDTH/2
center_y = HEIGHT/2
# скорось с которой будут ездить ракетки
PAD_SPEED = 100
# скорость левой платформы
LEFT_PAD_SPEED = 0
# скорость правой ракетки
RIGHT_PAD_SPEED = 0

# по горизонтали
BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0

# Насколько будет увеличиваться скорость мяча с каждым ударом
BALL_SPEED_UP = 1.15
# Максимальная скорость мяча
BALL_MAX_SPEED = 60
# Начальная скорость по горизонтали
BALL_X_SPEED = 10
# Начальная скорость по вертикали
BALL_Y_SPEED = 10

INITIAL_SPEED = 10
# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля
right_line_distance = WIDTH - PAD_W



PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
BGcol = '#8A2BE2'


