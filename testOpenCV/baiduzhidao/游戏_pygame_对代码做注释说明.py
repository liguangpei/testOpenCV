# -*- coding: UTF-8 -*-
import pygame
import sys
#进入游戏循环
while True:
    #遍历事件
    for event in pygame.event.get():
        #如果事件类型为QUIT，则退出游戏
        if event.type == pygame.QUIT: #sys.exit()
            pygame.quit()
            exit()
        # 如果事件类型为鼠标点击，记录当前点击位置和xy移动距离
        elif event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        #如果事件类型为鼠标按键抬起
        elif event.type == pygame.MOUSEBUTTONUP:
            #如果游戏结束，重置相关数据，生命值，分数，关卡等
            if game_over:
                game_over = False
                lives = 10
                score = 0
                Round =1
                vel_y=0.4
                mine=0
                flag=0
                pic=cat
                bomb_y = -50
        #获得按键
        keys = pygame.key.get_pressed()
        #如果按键是ESC键，则应用程序关闭
        if keys[pygame.K_ESCAPE]:
            sys.exit()