import random
# столкновение игрока с краями экрана
def x_wall(x, width):
    if x < 0:
        x = 0
    if x + 64 > width:
        x = 750 - 64
    return x

def x_wall_dome(x, y):
    if x + 64 > 425 and y + 100 > 400:
        x = 425 - 64
    return x


def y_wall(y, hieght, lb_hieght, sila_tyg, in_game_stage):
    if y <= 0:
        y = 1 
        sila_tyg = 0
    if y > hieght:
        in_game_stage = "level faild"
    return y, sila_tyg, in_game_stage
    

# столкновение игрока с землей 
def ground_conflict(y, lb_hieght, height, gravity, sila_tyg, jump_stage, scroll_summ):
    if y + lb_hieght > height - 30 and scroll_summ == 0:
        gravity = 0
        sila_tyg = 0
        jump_stage = 1
        y = height - 100 - 60
    return gravity, sila_tyg, jump_stage, y

def start_satings_1_level(x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_1_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity):
    x = 100
    y = 750 - 100
    sila_tyg = 0
    jump_stage = 0
    ground_y =  750 - 90
    platform_coordinate_1_level = [(175, 500), (515, 250), (262, 0), (10, -250), (515, -250), (275, -480), (400, -720), (235, -950), (10, -1160)]
    in_game_stage = "preface"
    game_stage = "level 1"
    scroll_sum = 0
    scroll_limit = 0
    ledder_rect_y = -1450
    gravity = 0.4
    return x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_1_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity
    

def start_satings_2_level(x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_2_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity):
    x = 100
    y = 750 - 100
    sila_tyg = 0
    jump_stage = 0
    ground_y =  750 - 90
    platform_coordinate_2_level = [(175, 500, False), (515, 250, True), (262, 0, False), (515, -250, True), (275, -480, False), (400, -720, True), (235, -950, True), (10, -1160, False)]
    in_game_stage = "preface"
    game_stage = "level 2"
    scroll_sum = 0
    scroll_limit = 0
    ledder_rect_y = -1450
    gravity = 0.4
    return x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_2_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity

def start_satings_3_level(x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_3_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity, pipe_parameters, wind_parameters, hail_waitings_time):
    x = 100
    y = 750 - 100
    sila_tyg = 0
    jump_stage = 0
    ground_y =  750 - 90
    platform_coordinate_3_level = [(55, 500, False), (500, 250, True), (485, 0, False), (55, -250, False), (10, -480, True), (485, -720, False), (485, -950, False), (10, -1160, True)]
    in_game_stage = "preface"
    game_stage = "level 3"
    scroll_sum = 0
    scroll_limit = 0
    ledder_rect_y = -1450
    gravity = 0.4
    pipe_parameters = [(0, 430, "left", random.randint(1500, 3000)), (710, -100, "right", random.randint(6000, 8000)), (0, -350, "left", 4000), (710, -820, "right", 0), (710, -1050, "right", 4000)]
    wind_parameters = [(-102, 440, "left"), (750 + 102, -90, "right"), (-102, -340, "left"), (750 + 102, -810, "right"), (750 + 102, -1040, "right")]
    hail_waitings_time = 0
    return x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_3_level, in_game_stage, game_stage, scroll_sum, scroll_limit, ledder_rect_y, gravity, pipe_parameters, wind_parameters, hail_waitings_time


def start_satings_boss_fight(x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_boss_fight, in_game_stage, game_stage, gravity, hail_waitings_time, lb_lifes_counter, lb_lifes_score, life_x, dome_life, boss_life, dome_life_x, lightning_waitings_time, under_boss_time, after_under_boss_time, under_lb_time, after_under_lb_time, lightning_strike_time, scroll_sum):
    x = 100
    y = 750 - 150
    sila_tyg = 0
    jump_stage = 0
    ground_y =  750 - 90
    platform_coordinate_boss_fight = [(10, 450), (425, 300), (425 + 225, 300)]
    in_game_stage = "preface"
    game_stage = "boss fight"
    gravity = 0.4
    hail_waitings_time = 0
    lb_lifes_score = 3
    lb_lifes_counter = lb_lifes_score
    life_x = 10
    dome_life = 3
    boss_life = True 
    dome_life_x = 550
    lightning_waitings_time = 0
    under_boss_time = 0 
    after_under_boss_time = 0 
    under_lb_time = 0
    after_under_lb_time = 0
    lightning_strike_time = 0
    scroll_sum = 0
    return x, y, sila_tyg, jump_stage, ground_y, platform_coordinate_boss_fight, in_game_stage, game_stage, gravity, hail_waitings_time, lb_lifes_counter, lb_lifes_score, life_x, dome_life, boss_life, dome_life_x, lightning_waitings_time, under_boss_time, after_under_boss_time, under_lb_time, after_under_lb_time, lightning_strike_time, scroll_sum

#  класс платформ 
class Platform:
    coordinate_x = 0
    coordinate_y = 0
    long = 0
    hieght = 0
    middle_sup_side = 0
    lb_on_platform = False
    swim_stage = False
    swim_step = 10
    #  создание платформы
    def __init__(self, coordinate_x, coordinate_y, swim_stage = False, swim_step = 2, long = 225, hieght = 40, lb_on_platform = False):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.long = long
        self.hieght = hieght
        self.middle_sup_side = hieght // 2
        self.lb_on_platform = lb_on_platform
        self.swim_stage = swim_stage
        self.swim_step = swim_step
    # столкновение платформы и игрока
    def conflict(self, x, y, lb_mid_main_side, lb_long, lb_hieght, gravity, sila_tyg, jump_stage):
        # падение игрока на платформу
        if (self.coordinate_x <= (x + lb_mid_main_side) <= self.coordinate_x + self.long) and \
            (self.coordinate_y <= y + lb_long + 10 <= self.coordinate_y + self.hieght):
            sila_tyg = 0
            jump_stage = 1
            gravity = 0
            self.lb_on_platform = True
            y = self.coordinate_y - lb_hieght
        if self.lb_on_platform:
            if x + lb_mid_main_side <= self.coordinate_x or x + lb_mid_main_side >= self.coordinate_x + self.long and self.lb_on_platform:
                gravity = 0.4
                self.lb_on_platform = False
        # столкновение в дно платформы 

        if (self.coordinate_x <= (x + lb_mid_main_side) <= self.coordinate_x + self.long) and \
            (self.coordinate_y <= y <= self.coordinate_y + self.hieght):
            y = self.coordinate_y + self.hieght + 1
            sila_tyg = 0
            
        # столкновение в левый бок платформы 
        if (y <= self.coordinate_y + self.hieght // 2 <= y + lb_long) and \
            (x <= self.coordinate_x <= x + lb_long):
            x = self.coordinate_x - lb_long

        # столкновение в правый бок платформы 
        if (y <= self.coordinate_y + self.hieght // 2 <= y + lb_long) and \
            (x <= self.coordinate_x + self.long <= x + lb_long):
            x = self.coordinate_x + self.long

        return gravity, sila_tyg, jump_stage, x, y
    def swim(self):
        if self.swim_stage:
            self.coordinate_x += self.swim_step
            if self.coordinate_x + self.long > 750:
                self.coordinate_x  = 750 - self.long
                self.swim_step -= 2 * self.swim_step
            if self.coordinate_x < 0:
                self.coordinate_x = 0
                self.swim_step -= 2 * self.swim_step
                
    
    # скролл платформы 
    def scroll(self, scroll_step):
        if self.coordinate_y - 100 <= 750:
            self.coordinate_y += scroll_step



class Pipe:
    coordinate_x = 0
    coordinate_y = 0
    long = 0
    hieght = 0
    side = ''
    vibro_coef = 4
    start_time = 0
    time_work_step = 0
    start_wind_work = False
    fisrt_launch = True
    waitings_time = 0

    def __init__(self, coordinate_x, coordinate_y, side, start_time, long = 40, hieght = 80, vibro_coef = 4, start_wind_work = False, first_launch = True, waitings_time = 0):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.long = long
        self.hieght = hieght
        self.side = side
        self.vibro_coef = vibro_coef

        self.waitings_time = waitings_time
        self.start_time = start_time
        self.start_wind_work = start_wind_work
        self.first_launch = first_launch
    
    def pipe_work(self):
        self.coordinate_y += self.vibro_coef 
        self.vibro_coef *= -1

    def scroll(self, scroll_step):
        if self.coordinate_y - 100 <= 750:
            self.coordinate_y += scroll_step


class Wind:
    coordinate_x = 0
    coordinate_y = 0
    long = 0
    hieght = 0
    side = ''
    blowing_wind = False 

    def __init__(self, coordinate_x, coordinate_y, side, long = 102, hieght = 60, blowing_wind = False):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.long = long
        self.hieght = hieght
        self.side = side
        self.blowing_wind = blowing_wind

    def conflict(self, x, y, lb_long, lb_hieght):
        if (self.coordinate_x <= x + lb_long // 2 <= self.coordinate_x + self.long) and \
            (self.coordinate_y <= y + lb_hieght // 2 <= self.coordinate_y + self.hieght):
            if self.side == "right":
                x -= 9
            if self.side == "left":
                x += 9
        return x
    
    def flight_wind(self):
        if self.side == "right":
            self.coordinate_x -= 9
            if self.coordinate_x + self.long < 0:
                self.blowing_wind = False
                self.coordinate_x = 750
                
        if self.side == "left":
            self.coordinate_x += 9
            if self.coordinate_x > 750:
                self.blowing_wind = False 
                self.coordinate_x = 0 - self.long
    
    def scroll(self, scroll_step):
        if self.coordinate_y - 100 <= 750:
            self.coordinate_y += scroll_step



class Hail:
    coordinate_x = 0
    coordinate_y = 0
    long = 0
    hieght = 0

    start_hail_fall = False
    waitings_time = 0


    def __init__(self, coordinate_x, coordinate_y, long = 210, hieght = 150, start_hail_fall = False):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.long = long
        self.hieght = hieght

        self.start_hail_fall = start_hail_fall
    

    def fall_hail(self):
        self.coordinate_y += 8
        if self.coordinate_y > 750:
            self.coordinate_y = 0 - self.hieght
            self.start_hail_fall = False
    

    def conflict(self, x, y, lb_long, lb_hieght, game_stage, in_game_stage, lb_life_score):
        if (self.coordinate_x <= x + lb_long // 2<= self.coordinate_x + self.long) and \
            (self.coordinate_y <= y + lb_hieght // 2 <= self.coordinate_y + self.hieght):

            if game_stage == "level 3":
                in_game_stage = "level faild"

            if game_stage == "boss fight":
                self.coordinate_y = 0 - self.hieght
                self.start_hail_fall = False
                lb_life_score -= 1
        return in_game_stage, lb_life_score


class Lightning:
    coordinate_x = 0
    coordinate_y = 0
    long = 0
    hieght = 0
    vibration_coef = 0

    start_lightning_fall = False
    waitings_time = 0

    lb_conflict = False
    dome_conflict = False
    bad_weather_conflict = False


    def __init__(self, coordinate_x = 0, coordinate_y = 0, long = 80, hieght = 690, stage_lightning = 0, vibration_coef = 2, lb_conflict = False, dome_conflict = False, bad_weather_conflict = False):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.long = long
        self.hieght = hieght
        self.vibration_coef = vibration_coef
        self.lb_conflict = lb_conflict
        self.dome_conflict = dome_conflict
        self.bad_weather_conflict = bad_weather_conflict
        self.stage_lightning = stage_lightning

    def fall_lightning(self):
        self.coordinate_y += 8
        if self.coordinate_y > 750:
            self.coordinate_y = 0 - self.hieght
            self.start_lightning_fall = False

    def vibration(self):
        self.coordinate_x += self.vibration_coef
        self.vibration_coef *= -1
    

    def conflict(self, x, y, lb_long, lb_hieght, lb_life_score, dome_life):
        if ((self.coordinate_x <= x <= self.coordinate_x + self.long) and (self.coordinate_y <= y <= self.coordinate_y + self.hieght)) \
        or ((self.coordinate_x <= x + lb_long <= self.coordinate_x + self.long) and (self.coordinate_y <= y <= self.coordinate_y + self.hieght)) \
        or ((self.coordinate_x <= x <= self.coordinate_x + self.long) and (self.coordinate_y <= y + lb_hieght <= self.coordinate_y + self.hieght)) \
        or((self.coordinate_x <= x + lb_long<= self.coordinate_x + self.long) and (self.coordinate_y <= y + lb_hieght <= self.coordinate_y + self.hieght)):
            self.stage_lightning = False
            lb_life_score -= 1
            self.lb_conflict = True

        if (((self.coordinate_x <= 425 + 50 + 84 <= self.coordinate_x + self.long) and (self.coordinate_y <= 750 - 180 - 60 <= self.coordinate_y + self.hieght)) and dome_life == 0) \
        or (((self.coordinate_x <= 425 + 50 + 84 + 54 <= self.coordinate_x + self.long) and (self.coordinate_y <= 750 - 180 - 60 <= self.coordinate_y + self.hieght)) and dome_life == 0) \
        or (((self.coordinate_x <= 425 + 50 + 84 + 108 <= self.coordinate_x + self.long) and (self.coordinate_y <= 750 - 180 - 60 <= self.coordinate_y + self.hieght)) and dome_life == 0):
            self.bad_weather_conflict = True
        
        if ((425 <= self.coordinate_x <= 750) and (425 <= self.coordinate_x + self.long <= 750)) and dome_life != 0:
            self.dome_conflict = True
        return lb_life_score