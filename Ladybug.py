# добавление библиотек и доп. файлов
import pygame
import args
import function
import random
import pickle


# инициализация игры 
pygame.init()
screen = pygame.display.set_mode((args.width, args.height))
clock = pygame.time.Clock()

pygame.display.set_caption("Ladybug and super cat")

#зауск цикла игры
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    args.currentTime = pygame.time.get_ticks()

    # проверка на выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # проверка на нажатие клавиш 
    keys = pygame.key.get_pressed()


    # стадия меню
    if args.game_stage == "explanation":
        screen.fill((255, 255, 255))
        screen.blit(args.explanation_img, (125, 189))
        if mouse_x > 400 + 125 and mouse_x < 400 + 125 + 51  \
        and mouse_y > 304 + 189 and mouse_y < 304 + 189 + 42 and args.game_stage == "explanation" and click:
            args.game_stage = "menu"
            args.in_menu_stage = None


    if args.game_stage == "menu":
        
        screen.blit(args.bg_menu_img, (0, 0))

        if mouse_x > 98 and mouse_x < 98 + 165  \
        and mouse_y > 315 and mouse_y < 315 + 55 and click:
            args.in_menu_stage = "list level"
        if mouse_x > 98 and mouse_x < 98 + 165  \
        and mouse_y > 379 and mouse_y < 379 + 55 and click:
            args.in_menu_stage = "restart"
        if mouse_x > 98 and mouse_x < 98 + 165  \
        and mouse_y > 443 and mouse_y < 443 + 55 and click:
            args.in_menu_stage = "save"
        if mouse_x > 98 and mouse_x < 98 + 165  \
        and mouse_y > 507 and mouse_y < 507 + 55 and click:
            args.game_stage = "exit"


        if mouse_x > 472 and mouse_x < 472 + 164  \
        and mouse_y > 315 and mouse_y < 315 + 54 and args.in_menu_stage == "list level" and click:
            args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_1_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
            # добавление платформ
            args.platform.clear()
            for i in range(0, 9):
                args.platform.append(function.Platform(args.platform_coordinate_1_level[i][0], args.platform_coordinate_1_level[i][1]))

        if mouse_x > 472 and mouse_x < 472 + 164  \
        and mouse_y > 379 and mouse_y < 379 + 54 and args.in_menu_stage == "list level" and len(args.close_level_list) < 3 and click:
            args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_2_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
            args.platform.clear()
            for i in range(0, 8):
                args.platform.append(function.Platform(args.platform_coordinate_2_level[i][0], args.platform_coordinate_2_level[i][1], args.platform_coordinate_2_level[i][2]))

        if mouse_x > 472 and mouse_x < 472 + 164  \
        and mouse_y > 443 and mouse_y < 443 + 54 and args.in_menu_stage == "list level" and len(args.close_level_list) < 2 and click:
            args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time = function.start_satings_3_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time)
            args.platform.clear()
            args.pipe.clear()
            args.wind.clear()
            for i in range(0, 8):
                args.platform.append(function.Platform(args.platform_coordinate_3_level[i][0], args.platform_coordinate_3_level[i][1], args.platform_coordinate_3_level[i][2]))
            for i in range(0, 5):
                args.pipe.append(function.Pipe(args.pipe_parameters[i][0], args.pipe_parameters[i][1], args.pipe_parameters[i][2], args.pipe_parameters[i][3]))
                args.wind.append(function.Wind(args.wind_parameters[i][0], args.wind_parameters[i][1], args.wind_parameters[i][2]))
            args.hail = function.Hail(random.randint(20, 520), -150)
            

        if mouse_x > 472 and mouse_x < 472 + 164  \
        and mouse_y > 507 and mouse_y < 507 + 54 and args.in_menu_stage == "list level" and len(args.close_level_list) == 0 and click:
            args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum = function.start_satings_boss_fight(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum)
            args.platform.clear()
            for i in range(0, 3):
                args.platform.append(function.Platform(args.platform_coordinate_boss_fight[i][0], args.platform_coordinate_boss_fight[i][1]))
            args.hail = function.Hail(random.randint(20, 520), -150) 
            args.lightning = function.Lightning() 
            

        if args.in_menu_stage == "list level":
            screen.blit(args.level_list_img, (436, 280))
            for i in args.close_level_list:
                screen.blit(args.close_level_img, (470, i))

        if args.in_menu_stage == "restart":
            args.close_level_list = [382, 446, 511]
            file = open('data.pickle', 'wb')
            pickle.dump(args.close_level_list, file)
            file.close() 
            

        if args.in_menu_stage == "save":
            file = open('data.pickle', 'wb')
            pickle.dump(args.close_level_list, file)
            file.close() 



    # 1 уровень         
    if args.game_stage == "level 1":
        if args.in_game_stage == "preface":
            screen.fill((255, 255, 255))
            screen.blit(args.preface_1_level_img, (125, 189))  
            if mouse_x > 125 + 227 and mouse_x < 125 + 227 + 51  \
            and mouse_y > 302 + 189 and mouse_y < 302 + 189 + 42 and args.in_game_stage == "preface" and click:
                args.in_game_stage = "play"


        if args.in_game_stage == "play":
            screen.blit(args.bg_1_level_img, (0 , 0))
            if mouse_x > 700 and mouse_x < 700 + 50  \
            and mouse_y > 0 and mouse_y < 0 + 50 and args.game_stage == "level 1" and click:
                args.in_game_stage = "pause"


            # Движение по диагонали
            if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x += args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4 
                args.jump_stage = 0
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x -= args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0
                args.lb_img = args.lb_l_img

            # движение по оси х
            elif keys[pygame.K_RIGHT]:
                args.x += args.L_R_movment_coef
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT]:
                args.x -= args.L_R_movment_coef
                args.lb_img = args.lb_l_img

            # движение по оси у
            elif keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0
            

            # столкновение игрока с землей
            args.gravity, args.sila_tyg, args.jump_stage, args.y = function.ground_conflict(args.y, args.lb_hieght, args.height, args.gravity, args.sila_tyg, args.jump_stage, args.scroll_sum)
            # столкновение игрока с краями экрана
            args.x = function.x_wall(args.x, args.width)
            args.y, args.sila_tyg, args.in_game_stage = function.y_wall(args.y, args.height, args.lb_hieght, args.sila_tyg, args.in_game_stage)


            # взаимодействие игрока с платформами
            for obj in args.platform:
                screen.blit(args.platform_img, (obj.coordinate_x, obj.coordinate_y)) # отрисовка платформ
                #  столкновение игрока с платформой 
                args.gravity, args.sila_tyg, args.jump_stage, args.x, args.y = obj.conflict(args.x, args.y, args.lb_mid_main_side, args.lb_long, args.lb_hieght, args.gravity, args.sila_tyg, args.jump_stage)
                if args.scroll_level:
                    obj.scroll(args.scroll_step)
                obj.swim()


            # падение и прыжок игрока
            args.y += args.sila_tyg
            args.sila_tyg += args.gravity

            
            # скролл экрана 
            if args.jump_stage == 1 and args.y + args.lb_hieght <= args.height // 2 - 100 and args.scroll_level != True and args.scroll_sum < 1800:
                args.scroll_level = True
                args.scroll_limit = args.height - (args.y + args.lb_hieght + 50)
                args.scroll_sum += args.scroll_limit
                if 1800 - args.scroll_sum  <= args.height // 2 - 15:
                    args.scroll_limit = 1800 - args.scroll_sum
                    args.scroll_sum = 1800
                
            if args.scroll_level:
                args.y += args.scroll_step
                args.scroll_limit -= args.scroll_step
                args.ground_y += args.scroll_step
                args.ledder_rect.y += args.scroll_step
                if args.scroll_limit <= 0:
                    args.scroll_level = False
            
            if args.ledder_rect.x <= args.x + (args.lb_long // 2) <= args.ledder_rect.x + args.ledder_rect.width:
                if args.ledder_rect.y <= args.y + (args.lb_hieght // 2) <= args.ledder_rect.y + args.ledder_rect.height:
                    args.in_game_stage = "next level"
                    if len(args.close_level_list) == 3:
                        args.close_level_list.pop(0)

            screen.blit(args.ground_img, (0, args.ground_y))                                            
            screen.blit(args.ledder_img, (args.ledder_rect.x, args.ledder_rect.y))
            screen.blit(args.lb_img, (args.x, args.y))
            screen.blit(args.button_pause_img, (args.width - 50, 0))                     


        if args.in_game_stage == "level faild":
            args.gravity = 0
            screen.blit(args.level_again_img, (125, 189))

            if mouse_x > 98 + 125 and mouse_x < 98 + 125 + 63 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"

            if mouse_x > 180 + 125 and mouse_x < 180 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 269 + 125 and mouse_x < 269 + 125 + 43 \
            and mouse_y > 182 + 189 and mouse_y < 182 + 189 + 62 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_1_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 9):
                    args.platform.append(function.Platform(args.platform_coordinate_1_level[i][0], args.platform_coordinate_1_level[i][1]))

            if mouse_x > 350 + 125 and mouse_x < 350 + 125 + 45 \
            and mouse_y > 179 + 189 and mouse_y < 179 + 189 + 65 and click:
                args.game_stage = "menu"
                args.in_menu_stage = None


        if args.in_game_stage == "pause":
            args.gravity = 0
            screen.blit(args.pause_list_img, (250, 312))

            if mouse_x > 250 + 33 and mouse_x < 250 + 33 + 39 \
            and mouse_y > 312 + 38 and mouse_y < 312 + 38 + 55 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 250 + 116 and mouse_x < 250 + 116 + 22 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 53 and click:
                args.in_game_stage = "play"
                args.gravity = 0.4

            if mouse_x > 250 + 180 and mouse_x < 250 + 180 + 37 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 56 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_1_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 9):
                    args.platform.append(function.Platform(args.platform_coordinate_1_level[i][0], args.platform_coordinate_1_level[i][1]))


        if args.in_game_stage == "next level":
            args.gravity = 0
            screen.blit(args.next_to_2_level_img, (125, 189))

            if mouse_x > 61 + 125 and mouse_x < 61 + 125 + 43 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_1_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 9):
                    args.platform.append(function.Platform(args.platform_coordinate_1_level[i][0], args.platform_coordinate_1_level[i][1]))

            if mouse_x > 138 + 125 and mouse_x < 138 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 225 + 125 and mouse_x < 225 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_1_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_1_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 306 + 125 and mouse_x < 306 + 125 + 59 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_2_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_2_level[i][0], args.platform_coordinate_2_level[i][1], args.platform_coordinate_2_level[i][2]))

            if mouse_x > 381 + 125 and mouse_x < 381 + 125 + 62 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"


    # 2 уровень        
    if args.game_stage == "level 2":
        if args.in_game_stage == "preface":
            screen.fill((255, 255, 255))
            screen.blit(args.preface_2_level_img, (125, 189))
            if mouse_x > 125 + 227 and mouse_x < 125 + 227 + 51  \
            and mouse_y > 302 + 189 and mouse_y < 302 + 189 + 42 and args.in_game_stage == "preface" and click:
                args.in_game_stage = "play"


        if args.in_game_stage == "play":
            screen.blit(args.bg_mid_level_img, (0 , 0))


            if mouse_x > 700 and mouse_x < 700 + 50  \
            and mouse_y > 0 and mouse_y < 0 + 50 and args.game_stage == "level 2" and click:
                args.in_game_stage = "pause"

            # Движение по диагонали
            if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x += args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4 
                args.jump_stage = 0
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x -= args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0
                args.lb_img = args.lb_l_img

            # движение по оси х
            elif keys[pygame.K_RIGHT]:
                args.x += args.L_R_movment_coef
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT]:
                args.x -= args.L_R_movment_coef
                args.lb_img = args.lb_l_img

            # движение по оси у
            elif keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0

            
            # столкновение игрока с землей
            args.gravity, args.sila_tyg, args.jump_stage, args.y = function.ground_conflict(args.y, args.lb_hieght, args.height, args.gravity, args.sila_tyg, args.jump_stage, args.scroll_sum)
            # столкновение игрока с краями экрана
            args.x = function.x_wall(args.x, args.width)
            args.y, args.sila_tyg, args.in_game_stage = function.y_wall(args.y, args.height, args.lb_hieght, args.sila_tyg, args.in_game_stage)


            # взаимодействие игрока с платформами
            for obj in args.platform:
                screen.blit(args.platform_img, (obj.coordinate_x, obj.coordinate_y)) # отрисовка платформ
                #  столкновение игрока с платформой 
                args.gravity, args.sila_tyg, args.jump_stage, args.x, args.y = obj.conflict(args.x, args.y, args.lb_mid_main_side, args.lb_long, args.lb_hieght, args.gravity, args.sila_tyg, args.jump_stage)
                if args.scroll_level:
                    obj.scroll(args.scroll_step)
                obj.swim()


            # падение и прыжок игрока
            args.y += args.sila_tyg
            args.sila_tyg += args.gravity

            
            # скролл экрана 
            if args.jump_stage == 1 and args.y + args.lb_hieght <= args.height // 2 - 100 and args.scroll_level != True and args.scroll_sum < 1800:
                args.scroll_level = True
                args.scroll_limit = args.height - (args.y + args.lb_hieght + 50)
                args.scroll_sum += args.scroll_limit
                if 1800 - args.scroll_sum  <= args.height // 2 - 15:
                    args.scroll_limit = 1800 - args.scroll_sum
                    args.scroll_sum = 1800
                
            if args.scroll_level:
                args.y += args.scroll_step
                args.scroll_limit -= args.scroll_step
                args.ground_y += args.scroll_step
                args.ledder_rect.y += args.scroll_step

                if args.scroll_limit <= 0:
                    args.scroll_level = False
            
            if args.ledder_rect.x <= args.x + (args.lb_long // 2) <= args.ledder_rect.x + args.ledder_rect.width:
                if args.ledder_rect.y <= args.y + (args.lb_hieght // 2) <= args.ledder_rect.y + args.ledder_rect.height:
                    args.in_game_stage = "next level"
                    if len(args.close_level_list) == 2:
                        args.close_level_list.pop(0)


            screen.blit(args.ground_img, (0, args.ground_y))                                         
            screen.blit(args.ledder_img, (args.ledder_rect.x, args.ledder_rect.y))
            screen.blit(args.lb_img, (args.x, args.y))
            screen.blit(args.button_pause_img, (args.width - 50, 0))                     


        if args.in_game_stage == "level faild":
            args.gravity = 0
            screen.blit(args.level_again_img, (125, 189))


            if mouse_x > 98 + 125 and mouse_x < 98 + 125 + 63 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"

            if mouse_x > 180 + 125 and mouse_x < 180 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 269 + 125 and mouse_x < 269 + 125 + 43 \
            and mouse_y > 182 + 189 and mouse_y < 182 + 189 + 62 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_2_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_2_level[i][0], args.platform_coordinate_2_level[i][1], args.platform_coordinate_2_level[i][2]))

            if mouse_x > 350 + 125 and mouse_x < 350 + 125 + 45 \
            and mouse_y > 179 + 189 and mouse_y < 179 + 189 + 65 and click:
                args.game_stage = "menu"
                args.in_menu_stage = None


        if args.in_game_stage == "pause":
            args.gravity = 0
            screen.blit(args.pause_list_img, (250, 312))

            if mouse_x > 250 + 33 and mouse_x < 250 + 33 + 39 \
            and mouse_y > 312 + 38 and mouse_y < 312 + 38 + 55 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 250 + 116 and mouse_x < 250 + 116 + 22 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 53 and click:
                args.in_game_stage = "play"
                args.gravity = 0.4

            if mouse_x > 250 + 180 and mouse_x < 250 + 180 + 37 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 56 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_2_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_2_level[i][0], args.platform_coordinate_2_level[i][1], args.platform_coordinate_2_level[i][2]))


        if args.in_game_stage == "next level":
            args.gravity = 0
            screen.blit(args.next_to_3_level_img, (125, 189))


            if mouse_x > 61 + 125 and mouse_x < 61 + 125 + 43 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity = function.start_satings_2_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_2_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity)
                args.platform.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_2_level[i][0], args.platform_coordinate_2_level[i][1], args.platform_coordinate_2_level[i][2]))

            if mouse_x > 138 + 125 and mouse_x < 138 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 225 + 125 and mouse_x < 225 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"
            if mouse_x > 306 + 125 and mouse_x < 306 + 125 + 59 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time = function.start_satings_3_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time)
                args.platform.clear()
                args.pipe.clear()
                args.wind.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_3_level[i][0], args.platform_coordinate_3_level[i][1], args.platform_coordinate_3_level[i][2]))
                for i in range(0, 5):
                    args.pipe.append(function.Pipe(args.pipe_parameters[i][0], args.pipe_parameters[i][1], args.pipe_parameters[i][2], args.pipe_parameters[i][3]))
                    args.wind.append(function.Wind(args.wind_parameters[i][0], args.wind_parameters[i][1], args.wind_parameters[i][2]))
                args.hail = function.Hail(random.randint(20, 520), -150)


            if mouse_x > 381 + 125 and mouse_x < 381 + 125 + 62 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"

    # 3 уровень        
    if args.game_stage == "level 3":
        if args.in_game_stage == "preface":
            screen.fill((255, 255, 255))
            screen.blit(args.preface_3_level_img, (125, 189))
            if mouse_x > 125 + 227 and mouse_x < 125 + 227 + 51  \
            and mouse_y > 302 + 189 and mouse_y < 302 + 189 + 42 and args.in_game_stage == "preface" and click:
                args.in_game_stage = "play"
                args.hail_waitings_time = args.currentTime
                for i in args.pipe:
                    i.waiting_time = args.currentTime
                

        
        if args.in_game_stage == "play":
            screen.blit(args.bg_mid_level_img, (0 , 0))


            if mouse_x > 700 and mouse_x < 700 + 50  \
            and mouse_y > 0 and mouse_y < 0 + 50 and args.game_stage == "level 3" and click:
                args.in_game_stage = "pause"

            # Движение по диагонали
            if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x += args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4 
                args.jump_stage = 0
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x -= args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0
                args.lb_img = args.lb_l_img

            # движение по оси х
            elif keys[pygame.K_RIGHT]:
                args.x += args.L_R_movment_coef
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT]:
                args.x -= args.L_R_movment_coef
                args.lb_img = args.lb_l_img

            # движение по оси у
            elif keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0

           # столкновение игрока с землей
            args.gravity, args.sila_tyg, args.jump_stage, args.y = function.ground_conflict(args.y, args.lb_hieght, args.height, args.gravity, args.sila_tyg, args.jump_stage, args.scroll_sum)
            # столкновение игрока с краями экрана
            args.x = function.x_wall(args.x, args.width)
            args.y, args.sila_tyg, args.in_game_stage = function.y_wall(args.y, args.height, args.lb_hieght, args.sila_tyg, args.in_game_stage)


            # взаимодействие игрока с платформами
            for obj in args.platform:
                screen.blit(args.platform_img, (obj.coordinate_x, obj.coordinate_y)) # отрисовка платформ
                #  столкновение игрока с платформой 
                args.gravity, args.sila_tyg, args.jump_stage, args.x, args.y = obj.conflict(args.x, args.y, args.lb_mid_main_side, args.lb_long, args.lb_hieght, args.gravity, args.sila_tyg, args.jump_stage)
                if args.scroll_level:
                    obj.scroll(args.scroll_step)
                obj.swim()

            # падение и прыжок игрока
            args.y += args.sila_tyg
            args.sila_tyg += args.gravity

            # скролл экрана 
            if args.jump_stage == 1 and args.y + args.lb_hieght <= args.height // 2 - 100 and args.scroll_level != True and args.scroll_sum < 1800:
                args.scroll_level = True
                args.scroll_limit = args.height - (args.y + args.lb_hieght + 50)
                args.scroll_sum += args.scroll_limit
                if 1800 - args.scroll_sum  <= args.height // 2 - 15:
                    args.scroll_limit = 1800 - args.scroll_sum
                    args.scroll_sum = 1800
                
            if args.scroll_level:
                args.y += args.scroll_step
                args.scroll_limit -= args.scroll_step
                args.ground_y += args.scroll_step
                args.ledder_rect.y += args.scroll_step

                if args.scroll_limit <= 0:
                    args.scroll_level = False
            
            for w in args.wind:
                if w.blowing_wind:
                    w.flight_wind()
                if args.scroll_level:
                    w.scroll(args.scroll_step)

                args.x = w.conflict(args.x, args.y, args.lb_long, args.lb_hieght)
                if w.side == "left":
                     screen.blit(args.wind_l_img, (w.coordinate_x, w.coordinate_y))
                elif w.side == "right":
                     screen.blit(args.wind_r_img, (w.coordinate_x, w.coordinate_y))

            for p in args.pipe:
                if p.side == "left":
                     screen.blit(args.pipe_l_img, (p.coordinate_x, p.coordinate_y))
                elif p.side == "right":
                     screen.blit(args.pipe_r_img, (p.coordinate_x, p.coordinate_y))
                #  столкновение игрока с платформой 
                if args.scroll_level:
                    p.scroll(args.scroll_step)

                if p.first_launch == True and p.start_wind_work == False:
                    if args.currentTime - p.waiting_time >= p.start_time:
                        p.start_wind_work = True
                        p.first_launch = False
                        p.start_time = args.currentTime
                        p.waitings_time = args.currentTime

                elif p.first_launch == False and p.start_wind_work == False:
                    if args.currentTime - p.waitings_time >= 6500:
                        p.start_wind_work = True
                        p.start_time = args.currentTime
                        p.waitings_time = args.currentTime
                        
                if p.start_wind_work:
                    p.pipe_work()

                if args.currentTime - 1000 >= p.start_time and p.start_wind_work:
                    p.start_wind_work = False
                    p.waitings_time = args.currentTime
                    args.wind[args.pipe.index(p)].blowing_wind = True


            if args.currentTime - args.hail_waitings_time >= 5000 and args.hail.start_hail_fall == False:
                args.hail.coordinate_x = random.randint(20, 520)
                args.hail.start_hail_fall = True
                args.hail_waitings_time = args.currentTime
            if args.hail.start_hail_fall:
                args.hail.fall_hail()
                args.in_game_stage, args.lb_lifes_score = args.hail.conflict(args.x, args.y, args.lb_long, args.lb_hieght, args.game_stage, args.in_game_stage, args.lb_lifes_score)
                screen.blit(args.hail_img, (args.hail.coordinate_x, args.hail.coordinate_y))

            
            if args.ledder_rect.x <= args.x + (args.lb_long // 2) <= args.ledder_rect.x + args.ledder_rect.width:
                if args.ledder_rect.y <= args.y + (args.lb_hieght // 2) <= args.ledder_rect.y + args.ledder_rect.height:
                    args.in_game_stage = "next level"
                    if len(args.close_level_list) == 1:
                        args.close_level_list.clear()
            

            screen.blit(args.gray_cloud_img, (0, -10))
            screen.blit(args.ground_img, (0, args.ground_y))                                         
            screen.blit(args.ledder_img, (args.ledder_rect.x, args.ledder_rect.y))
            screen.blit(args.lb_img, (args.x, args.y))
            screen.blit(args.button_pause_img, (args.width - 50, 0))  

                               

        if args.in_game_stage == "level faild":
            args.gravity = 0
            screen.blit(args.level_again_img, (125, 189))

            if mouse_x > 98 + 125 and mouse_x < 98 + 125 + 63 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"

            if mouse_x > 180 + 125 and mouse_x < 180 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 269 + 125 and mouse_x < 269 + 125 + 43 \
            and mouse_y > 182 + 189 and mouse_y < 182 + 189 + 62 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time = function.start_satings_3_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time)
                args.platform.clear()
                args.pipe.clear()
                args.wind.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_3_level[i][0], args.platform_coordinate_3_level[i][1], args.platform_coordinate_3_level[i][2]))
                for i in range(0, 5):
                    args.pipe.append(function.Pipe(args.pipe_parameters[i][0], args.pipe_parameters[i][1], args.pipe_parameters[i][2], args.pipe_parameters[i][3]))
                    args.wind.append(function.Wind(args.wind_parameters[i][0], args.wind_parameters[i][1], args.wind_parameters[i][2]))
                args.hail = function.Hail(random.randint(20, 520), -150)


            if mouse_x > 350 + 125 and mouse_x < 350 + 125 + 45 \
            and mouse_y > 179 + 189 and mouse_y < 179 + 189 + 65 and click:
                args.game_stage = "menu"
                args.in_menu_stage = None


        if args.in_game_stage == "pause":
            args.gravity = 0
            screen.blit(args.pause_list_img, (250, 312))

            args.hail_waitings_time = args.currentTime
            for i in args.pipe:
                i.waiting_time = args.currentTime

            if mouse_x > 250 + 33 and mouse_x < 250 + 33 + 39 \
            and mouse_y > 312 + 38 and mouse_y < 312 + 38 + 55 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 250 + 116 and mouse_x < 250 + 116 + 22 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 53 and click:
                args.in_game_stage = "play"
                args.gravity = 0.4

            if mouse_x > 250 + 180 and mouse_x < 250 + 180 + 37 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 56 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time = function.start_satings_3_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time)
                args.platform.clear()
                args.pipe.clear()
                args.wind.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_3_level[i][0], args.platform_coordinate_3_level[i][1], args.platform_coordinate_3_level[i][2]))
                for i in range(0, 5):
                    args.pipe.append(function.Pipe(args.pipe_parameters[i][0], args.pipe_parameters[i][1], args.pipe_parameters[i][2], args.pipe_parameters[i][3]))
                    args.wind.append(function.Wind(args.wind_parameters[i][0], args.wind_parameters[i][1], args.wind_parameters[i][2]))
                args.hail = function.Hail(random.randint(20, 520), -150)

        if args.in_game_stage == "next level":
            args.gravity = 0
            screen.blit(args.next_to_boss_fight_img, (125, 189))
            
            
            if mouse_x > 61 + 125 and mouse_x < 61 + 125 + 43 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time = function.start_satings_3_level(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_3_level, args.in_game_stage, args.game_stage, args.scroll_sum, args.scroll_limit, args.ledder_rect.y, args.gravity, args.pipe_parameters, args.wind_parameters, args.hail_waitings_time)
                args.platform.clear()
                args.pipe.clear()
                args.wind.clear()
                for i in range(0, 8):
                    args.platform.append(function.Platform(args.platform_coordinate_3_level[i][0], args.platform_coordinate_3_level[i][1], args.platform_coordinate_3_level[i][2]))
                for i in range(0, 5):
                    args.pipe.append(function.Pipe(args.pipe_parameters[i][0], args.pipe_parameters[i][1], args.pipe_parameters[i][2], args.pipe_parameters[i][3]))
                    args.wind.append(function.Wind(args.wind_parameters[i][0], args.wind_parameters[i][1], args.wind_parameters[i][2]))
                args.hail = function.Hail(random.randint(20, 520), -150)

            if mouse_x > 138 + 125 and mouse_x < 138 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 225 + 125 and mouse_x < 225 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 306 + 125 and mouse_x < 306 + 125 + 59 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum = function.start_satings_boss_fight(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum)
                args.platform.clear()
                for i in range(0, 3):
                    args.platform.append(function.Platform(args.platform_coordinate_boss_fight[i][0], args.platform_coordinate_boss_fight[i][1]))
                args.hail = function.Hail(random.randint(20, 520), -150) 
                args.lightning = function.Lightning() 

            if mouse_x > 381 + 125 and mouse_x < 381 + 125 + 62 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"




    # boss fight         
    if args.game_stage == "boss fight":
        if args.in_game_stage == "preface":
            screen.fill((255, 255, 255))
            screen.blit(args.preface_boss_fight_img, (125, 189))                           
    
            if mouse_x > 125 + 227 and mouse_x < 125 + 227 + 51  \
            and mouse_y > 302 + 189 and mouse_y < 302 + 189 + 42 and args.in_game_stage == "preface" and click:
                args.in_game_stage = "play"
                args.hail_waitings_time = args.currentTime
                args.lightning_waitings_time = args.currentTime
                args.y = 500
                

        
        if args.in_game_stage == "play":
            screen.blit(args.bg_boss_fight_img, (0 , 0))


            if mouse_x > 700 and mouse_x < 700 + 50  \
            and mouse_y > 0 and mouse_y < 0 + 50 and args.game_stage == "boss fight" and click:
                args.in_game_stage = "pause"

            # Движение по диагонали
            if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x += args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4 
                args.jump_stage = 0
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.x -= args.L_R_movment_coef
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0
                args.lb_img = args.lb_l_img

            # движение по оси х
            elif keys[pygame.K_RIGHT]:
                args.x += args.L_R_movment_coef
                args.lb_img = args.lb_r_img
                
            elif keys[pygame.K_LEFT]:
                args.x -= args.L_R_movment_coef
                args.lb_img = args.lb_l_img

            # движение по оси у
            elif keys[pygame.K_SPACE] and args.jump_stage == 1:
                args.sila_tyg = -15
                args.gravity = 0.4
                args.jump_stage = 0

           # столкновение игрока с землей
            args.gravity, args.sila_tyg, args.jump_stage, args.y = function.ground_conflict(args.y, args.lb_hieght, args.height, args.gravity, args.sila_tyg, args.jump_stage, args.scroll_sum)
            # столкновение игрока с краями экрана
            args.x = function.x_wall(args.x, args.width)
            args.y, args.sila_tyg, args.in_game_stage = function.y_wall(args.y, args.height, args.lb_hieght, args.sila_tyg, args.in_game_stage)
            args.x = function.x_wall_dome(args.x, args.y)


            # взаимодействие игрока с платформами
            for obj in args.platform:
                screen.blit(args.platform_img, (obj.coordinate_x, obj.coordinate_y)) # отрисовка платформ
                #  столкновение игрока с платформой 
                args.gravity, args.sila_tyg, args.jump_stage, args.x, args.y = obj.conflict(args.x, args.y, args.lb_mid_main_side, args.lb_long, args.lb_hieght, args.gravity, args.sila_tyg, args.jump_stage)


            # падение и прыжок игрока
            args.y += args.sila_tyg
            args.sila_tyg += args.gravity

            if args.currentTime - args.hail_waitings_time >= 5000 and args.hail.start_hail_fall == False:
                args.hail.coordinate_x = random.randint(20, 520)
                args.hail.start_hail_fall = True
                args.hail_waitings_time = args.currentTime

            if args.hail.start_hail_fall:
                args.hail.fall_hail()
                args.in_game_stage, args.lb_lifes_score = args.hail.conflict(args.x, args.y, args.lb_long, args.lb_hieght, args.game_stage, args.in_game_stage, args.lb_lifes_score)
                screen.blit(args.hail_img, (args.hail.coordinate_x, args.hail.coordinate_y))
                
            screen.blit(args.gray_cloud_img, (0, -10))
            screen.blit(args.ground_img, (0, args.ground_y))
            screen.blit(args.lb_img, (args.x, args.y))
            screen.blit(args.button_pause_img, (args.width - 50, 0))  




            if args.dome_life != 0:
                screen.blit(args.dome_img, (425, 420))
                for i in range(args.dome_life):
                    screen.blit(args.dome_life_img, (args.dome_life_x, 5))
                    args.dome_life_x += 35
                

            
            if args.boss_life:
                screen.blit(args.full_life_img, (args.dome_life_x, 5))
            else:
                screen.blit(args.empty_life_img, (args.dome_life_x, 5))
                args.in_game_stage = "next level"

            args.dome_life_x = 550

            screen.blit(args.bad_weather_img, (425 + 50 + 84, 750 - 180 - 60))

            for i in range(args.lb_lifes_score):
                screen.blit(args.full_life_img, (args.life_x, 5))
                args.life_x += 35
            for k in range(args.lb_lifes_counter - args.lb_lifes_score):
                screen.blit(args.empty_life_img, (args.life_x, 5))
                args.life_x += 35
            args.life_x = 10

            if args.lb_lifes_score == 0:
                args.in_game_stage = "level faild"


            # запуск молнии в игре 
            if args.lightning.stage_lightning == 0:
                if args.currentTime - args.lightning_waitings_time >= 3000: 
                    args.lightning.coordinate_x = 68 + 425 + 50 + 84
                    args.lightning.stage_lightning = 1
                    args.under_boss_time = args.currentTime
                    args.lightning.bad_weather_conflict = False
            
            # появление молнии над боссом
            if args.lightning.stage_lightning == 1:
                if args.currentTime - args.under_boss_time >= 2000:
                    args.lightning.stage_lightning = 2
                    args.after_under_boss_time = args.currentTime

                screen.blit(args.lightning_img, (args.lightning.coordinate_x, 0))
                args.lightning.vibration()
                args.lightning.lb_conflict = False
                args.lightning.bad_weather_conflict = False
                args.lightning.dome_conflict = False
                args.lb_lifes_score = args.lightning.conflict(args.x, args.y, args.lb_long, args.lb_hieght, args.lb_lifes_score, args.dome_life)

                if args.lightning.lb_conflict:
                    args.lightning.stage_lightning = 0
                    args.lightning_waitings_time = args.currentTime
                    args.lightning.lb_conflict = False

            # ожидание времени между молнией над боссом и фантомом молнии над игроком
            if args.lightning.stage_lightning == 2:
                if args.currentTime - args.after_under_boss_time >= 2000:
                    args.lightning.stage_lightning = 3
                    args.under_lb_time = args.currentTime
            
            # появление фантома молнии над игроком
            if args.lightning.stage_lightning == 3:
                if args.currentTime - args.under_lb_time >= 1500:
                    args.lightning.stage_lightning = 4
                    args.after_under_lb_time = args.currentTime
                args.lightning.coordinate_x = args.x - 8
                pygame.draw.rect(screen, (255, 0, 0), (args.lightning.coordinate_x, 0, 3, 750))
                pygame.draw.rect(screen, (255, 0, 0), (args.lightning.coordinate_x + 20 + 20 + 20 + 7, 0, 3, 750))

            #  ожидание времени между появлением фантома и ударом молнии в место фантома
            if args.lightning.stage_lightning == 4:
                if args.currentTime - args.after_under_lb_time >= 1500:
                    args.lightning.stage_lightning = 5
                    args.lightning_strike_time = args.currentTime

            # удар молнии в место фантома
            if args.lightning.stage_lightning == 5:
                if args.currentTime - args.lightning_strike_time >= 500:
                    args.lightning.stage_lightning = 0
                    args.lightning_waitings_time = args.currentTime
                screen.blit(args.lightning_img, (args.lightning.coordinate_x, 0))
                args.lightning.vibration()
                args.lightning.lb_conflict = False
                args.lightning.bad_weather_conflict = False
                args.lightning.dome_conflict = False
                args.lb_lifes_score = args.lightning.conflict(args.x, args.y, args.lb_long, args.lb_hieght, args.lb_lifes_score, args.dome_life)

                if args.lightning.lb_conflict:
                    args.lightning.stage_lightning = 0
                    args.lightning_waitings_time = args.currentTime
                    args.lightning.lb_conflict = False

                if args.lightning.dome_conflict and args.dome_life != 0:
                    args.lightning.stage_lightning = 0
                    args.lightning_waitings_time = args.currentTime
                    args.dome_life -= 1
                    args.lightning.dome_conflict = False

                if args.lightning.bad_weather_conflict and args.dome_life == 0:
                    args.lightning.stage_lightning = 0
                    args.lightning_waitings_time = args.currentTime
                    args.boss_life = False
                    args.lightning.bad_weather_conflict = False
                    



        if args.in_game_stage == "level faild":
            args.gravity = 0
            screen.blit(args.level_again_img, (125, 189))

            if mouse_x > 98 + 125 and mouse_x < 98 + 125 + 63 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"

            if mouse_x > 180 + 125 and mouse_x < 180 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 269 + 125 and mouse_x < 269 + 125 + 43 \
            and mouse_y > 182 + 189 and mouse_y < 182 + 189 + 62 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum = function.start_satings_boss_fight(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum)
                args.platform.clear()
                for i in range(0, 3):
                    args.platform.append(function.Platform(args.platform_coordinate_boss_fight[i][0], args.platform_coordinate_boss_fight[i][1]))
                args.hail = function.Hail(random.randint(20, 520), -150) 
                args.lightning = function.Lightning() 


            if mouse_x > 350 + 125 and mouse_x < 350 + 125 + 45 \
            and mouse_y > 179 + 189 and mouse_y < 179 + 189 + 65 and click:
                args.game_stage = "menu"
                args.in_menu_stage = None


        if args.in_game_stage == "pause":
            args.gravity = 0
            screen.blit(args.pause_list_img, (250, 312))

            args.hail_waitings_time = args.currentTime
            for i in args.pipe:
                i.waiting_time = args.currentTime

            if mouse_x > 250 + 33 and mouse_x < 250 + 33 + 39 \
            and mouse_y > 312 + 38 and mouse_y < 312 + 38 + 55 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 250 + 116 and mouse_x < 250 + 116 + 22 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 53 and click:
                args.in_game_stage = "play"
                args.gravity = 0.4

            if mouse_x > 250 + 180 and mouse_x < 250 + 180 + 37 \
            and mouse_y > 312 + 41 and mouse_y < 312 + 41 + 56 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum = function.start_satings_boss_fight(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum)
                args.platform.clear()
                for i in range(0, 3):
                    args.platform.append(function.Platform(args.platform_coordinate_boss_fight[i][0], args.platform_coordinate_boss_fight[i][1]))
                args.hail = function.Hail(random.randint(20, 520), -150) 
                args.lightning = function.Lightning() 

        if args.in_game_stage == "next level":
            args.gravity = 0
            screen.blit(args.next_to_finish_slide_img, (125, 189))
            
            if mouse_x > 61 + 125 and mouse_x < 61 + 125 + 43 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum = function.start_satings_boss_fight(args.x, args.y, args.sila_tyg, args.jump_stage, args.ground_y, args.platform_coordinate_boss_fight, args.in_game_stage, args.game_stage, args.gravity, args.hail_waitings_time, args.lb_lifes_counter, args.lb_lifes_score, args.life_x, args.dome_life, args.boss_life, args.dome_life_x, args.lightning_waitings_time, args.under_boss_time, args.after_under_boss_time, args.under_lb_time, args.after_under_lb_time, args.lightning_strike_time, args.scroll_sum)
                args.platform.clear()
                for i in range(0, 3):
                    args.platform.append(function.Platform(args.platform_coordinate_boss_fight[i][0], args.platform_coordinate_boss_fight[i][1]))
                args.hail = function.Hail(random.randint(20, 520), -150) 
                args.lightning = function.Lightning() 

            if mouse_x > 138 + 125 and mouse_x < 138 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                file = open('data.pickle', 'wb')
                pickle.dump(args.close_level_list, file)
                file.close() 


            if mouse_x > 225 + 125 and mouse_x < 225 + 125 + 45 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 65 and click:
                args.in_menu_stage = None
                args.game_stage = "menu"

            if mouse_x > 306 + 125 and mouse_x < 306 + 125 + 59 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 63 and click:
                args.game_stage = "conclusion"

            if mouse_x > 381 + 125 and mouse_x < 381 + 125 + 62 \
            and mouse_y > 181 + 189 and mouse_y < 181 + 189 + 62 and click:
                args.game_stage = "exit"
    
    if args.game_stage == "conclusion":
        if mouse_x > 700 and mouse_x < 700 + 50  \
        and mouse_y > 0 and mouse_y < 0 + 50 and click:
            args.in_menu_stage = None
            args.game_stage = "menu"

                

        screen.blit(args.bg_finish_slide_img, (0, 0))
        screen.blit(args.button_pause_img, (args.width - 50, 0))  

    if args.game_stage == "exit":
        pygame.quit()
        exit()
    # найстройки фпс и обновление экрана пользователя
    pygame.display.update()
    clock.tick(args.FPS)