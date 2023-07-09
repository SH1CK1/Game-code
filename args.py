import pygame
import random
import pickle

file_in = open("data.pickle", "rb")
data = pickle.load(file_in)
file_in.close()

# базовые параметры
width = 750
height = 750
FPS = 120
currentTime = 0
# параметры игры
game_stage = "explanation"
in_menu_stage = None
in_game_stage = "play"
scroll_level = "stop"
close_level_list = data
# ледибаг
x = width // 2 + 100
y = 400
L_R_movment_coef = 5
sila_tyg = 0
gravity = 0.4
jump_stage = 0
lb_long = 64
lb_hieght = 100
lb_mid_main_side = lb_long // 2
#  земля
ground_y = height - 90
# платфоры 
platform_coordinate_1_level = [(175, 500), (515, 250), (262, 0), (10, -250), (515, -250), (275, -480), (400, -720), (235, -950), (10, -1160)]
platform_coordinate_2_level = [(175, 500, False), (515, 250, True), (262, 0, False), (515, -250, True), (275, -480, False), (400, -720, True), (235, -950, True), (10, -1160, False)]
platform_coordinate_3_level = [(25, 500, False), (500, 250, True), (515, 0, False), (500, -250, False), (10, -480, True), (500, -720, False), (500, -950, False), (10, -1160, True)]
platform_coordinate_boss_fight = [(10, 450), (425, 300), (425 + 225, 300)]
platform = []
# скролл
scroll_sum = 0
scroll_step = 4
scroll_limit = 0
# wind
pipe = []
pipe_parameters = [(0, 430, "left", random.randint(1500, 3000)), (710, -100, "right", random.randint(6000, 8000)), (0, -350, "left", 4000), (710, -820, "right", 0), (710, -1050, "right", 4000)]
wind = []
wind_parameters = [(-102, 440, "left"), (750 + 102, -90, "right"), (-102, -340, "left"), (750 + 102, -810, "right"), (750 + 102, -1040, "right")]
#hail 
hail = None
hail_waitings_time = 0
# lightning
lightning = None
lightning_waitings_time = 0
under_boss_time = 0 
after_under_boss_time = 0 
under_lb_time = 0
after_under_lb_time = 0
lightning_strike_time = 0
# лестница
ledder_rect = pygame.Rect(50, -1450, 78, 200)
# boss fight 
dome_life = 3
lb_lifes_score = 3
lb_lifes_counter = lb_lifes_score 
life_x = 10
boss_life = True
dome_life_x = 600

# добавление изображений
#  задний фон
bg_menu_img = pygame.image.load('game image/bg menu.png')
bg_1_level_img = pygame.image.load('game image/bg 1 level.png')
bg_mid_level_img = pygame.image.load('game image/bg mid level.jpg')
bg_boss_fight_img = pygame.image.load('game image/bg boss fight.jpg')
bg_finish_slide_img = pygame.image.load('game image/finish slide.jpg')
# игровые изображения
ledder_img = pygame.image.load('game image/ledder.png')

lb_r_img = pygame.image.load('game image/lb r.png')
lb_l_img = pygame.image.load('game image/lb l.png')
lb_img = lb_r_img

platform_img = pygame.image.load('game image/platform.png')
ground_img = pygame.image.load('game image/ground.png')

level_list_img = pygame.image.load('game image/level list.png')
close_level_img = pygame.image.load('game image/close level.png')
button_pause_img = pygame.image.load('game image/button pause.png')
pause_list_img = pygame.image.load('game image/pause list.png')

next_to_2_level_img = pygame.image.load('game image/next to 2 level.png')
next_to_3_level_img = pygame.image.load('game image/next to 3 level.png')
next_to_boss_fight_img = pygame.image.load('game image/next to boss fight.png')
next_to_finish_slide_img = pygame.image.load('game image/next to finish slide.png')

level_again_img = pygame.image.load('game image/level again.png')
explanation_img = pygame.image.load('game image/explanation.png')

preface_1_level_img = pygame.image.load('game image/preface 1 level.png')
preface_2_level_img = pygame.image.load('game image/preface 2 level.png')
preface_3_level_img = pygame.image.load('game image/preface 3 level.png')
preface_boss_fight_img = pygame.image.load('game image/preface boss fight.png')

pipe_l_img = pygame.image.load('game image/pipe l.png')
pipe_r_img = pygame.image.load('game image/pipe r.png')
wind_l_img = pygame.image.load('game image/wind l.png')
wind_r_img = pygame.image.load('game image/wind r.png')

hail_img = pygame.image.load('game image/hail.png')
gray_cloud_img = pygame.image.load('game image/gray cloud.png')

dome_img = pygame.image.load('game image/dome.png')
bad_weather_img = pygame.image.load('game image/bad weather.png')

full_life_img = pygame.image.load('game image/full life.png')
empty_life_img = pygame.image.load('game image/empty life.png')

dome_life_img = pygame.image.load('game image/dome life.png')
lightning_img = pygame.image.load('game image/lightning.png')