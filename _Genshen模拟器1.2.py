from easygui import *
import zipping
import random
import sys
import time
import pygame
from moviepy.editor import VideoFileClip

# name = '旅行者'
# name_second = '动身吧，旅行者，异世的诗篇还在等着我们呢'
open_image1 = pygame.image.load('image/open1.jpg')
open_image2 = pygame.image.load('image/open2.jpg')
open_image3 = pygame.image.load('image/open3.jpg')
open_image4 = pygame.image.load('image/open4.jpg')
open_image5 = pygame.image.load('image/open5.jpg')
open_image6 = pygame.image.load('image/open6.jpg')
open_image7 = pygame.image.load('image/open7.jpg')
open_image8 = pygame.image.load('image/open8.jpg')
open_image9 = pygame.image.load('image/open9.jpg')
size = weight, height = 1200, 600
screen = pygame.display.set_mode(size)
screen.blit(open_image1, (0, 0))
pygame.display.flip()

try:
    ff = open(r'C:\name.txt', 'a')
    ff.close()
    ff = open(r'C:\name.txt')
    name = ff.read()
    ff.close()
    if name == '':
        ff = open(r'C:\name.txt', 'w')
        ff.write('旅行者')
        name = '旅行者'
    ff.close()

    ff = open(r'C:\name2.txt', 'a')
    ff.close()
    ff = open(r'C:\name2.txt')
    name_second = ff.read()
    ff.close()
    if name_second == '':
        ff = open(r'C:\name2.txt', 'w')
        ff.write('动身吧，旅行者，异世的诗篇还在等着我们呢')
        name_second = '动身吧，旅行者，异世的诗篇还在等着我们呢'
    ff.close()
except Exception:
    pass
if True:
    great_img = pygame.image.load('image/great.png')
    musicplay = False
    musiclist = []
    musiclist.append(r'music/镇守之森.mp3')
    musiclist.append(r'music/何妄何执.mp3')
    musiclist.append(r'music/甘雨.mp3')
    musiclist.append(r'music/璃月.mp3')
    musiclist.append(r'music/温迪.mp3')
    yinyueshuliang = 4
    dinggui = 0
    dingguiobject = 'wuqi'
    a = 0  # 总抽数
    c = 0  # 五星保底
    d = 0  # 五星总抽中数
    sixingfangwai = 0
    musicplayer = 0
    musicloud = 0.5
    music_main_loud = 1
    moved = False
    moved2 = False
    b1 = 0  # 五星抽中数（歪）
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0
    b6 = 0
    p = 0  # 五星歪数
    oo = 0  # 五星防第二次歪
    c1 = 0  # 四星
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    u = 0  # 四星保底
    po = 0  # 四星总抽中数
    four_start_low = 0  # 四星保底数
    d1 = 0  # 三星
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    d7 = 0
    d8 = 0
    d9 = 0
    d10 = 0
    m0 = 0
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    m8 = 0
    m9 = 0
    m10 = 0
    m11 = 0
    m12 = 0
    m13 = 0
    m14 = 0
    m15 = 0
    m16 = 0
    m17 = 0
    m18 = 0
    m19 = 0
    m20 = 0
    m21 = 0
    m22 = 0
    m23 = 0
    m24 = 0
    m25 = 0
    m26 = 0
    m27 = 0
    m28 = 0
    m29 = 0
    m30 = 0
    m31 = 0
    m32 = 0
    m33 = 0
    m34 = 0
    m35 = 0
    m36 = 0
    m37 = 0
    m38 = 0
    m39 = 0
    kq1 = 0
    kq2 = 0
    chouzhongprize1 = 0
    chouzhongprize2 = 0
    wushichou = 0
    liushichou = 0
    qishichou = 0
    bashichou = 0
    wuxingbaodi = 0
    xingchen = 0
    xinghui = 0
    linshixingchen = 0
    linshixinghui = 0
    aa = True
    cc = True
    movie_play = False
    fff = False
    gg = False
    oiu = False
    firsting = True
    wuqi1 = True
    green = (0, 255, 0)  # 颜色设置
    number = 4
    image1 = pygame.image.load('{}/1.png'.format(number))
    image2 = pygame.image.load('{}/2.png'.format(number))
    image3 = pygame.image.load('{}/3.png'.format(number))
    image4 = pygame.image.load('{}/4.png'.format(number))
    image5 = pygame.image.load('{}/5.png'.format(number))
    image6 = pygame.image.load('{}/6.png'.format(number))
    image7 = pygame.image.load('{}/7.png'.format(number))
    image8 = pygame.image.load('{}/8.png'.format(number))
    image9 = pygame.image.load('{}/9.png'.format(number))
    image10 = pygame.image.load('{}/10.png'.format(number))
    image11 = pygame.image.load('{}/11.png'.format(number))
    image12 = pygame.image.load('{}/12.png'.format(number))
    image_strong = pygame.image.load('image/strong1.jpg')
    prize_list = ['甘雨', '温迪', '钟离', '武器池', '刻晴']
    listing = []
    super_super = True
    musicing1 = pygame.image.load("musicplayer.png")
    musicing2 = pygame.image.load("musicplayer2.png")
    local_image_one = pygame.image.load("image/local0.png")
    local_image_main = pygame.image.load('image/local2.png')
    pygame.mixer.quit()
    pygame.init()
    bg = (0, 0, 0)
    prize1 = '温迪'
    prize2 = '温迪'
    clip1 = VideoFileClip(r'video/10j.mp4')
    clip2 = VideoFileClip(r'video/1j.mp4')
    screen.blit(open_image1, (0, 0))
    pygame.display.flip()
    tupian = pygame.image.load("image/venty.jpg")
    listw = ['芭芭拉', '菲谢尔', '香菱', '芭芭拉', '菲谢尔']
    location1 = -2000
    location2 = -750
    button_up = pygame.image.load('image/0.png')
    button_down = pygame.image.load('image/1.png')
    button_back = pygame.image.load('image/2.png')
    vel_x, vel_y = 0, 0
    vel_a, vel_b = 0, 0
    moving = False
    bigger = False
    count_hi = 0
    main_music = pygame.mixer.Sound("music/sound1.mp3")
    main_music2 = pygame.mixer.Sound("music/sound2.mp3")
    font_music_loud = pygame.font.Font('hk4e_zh-cn.ttf', 25)
    image_go1 = pygame.image.load('image/go.png')
    screen.blit(open_image2, (0, 0))
    pygame.display.flip()


def aff(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        zipping.breakplay()
        screen.blit(tupian, (0, 0))
        pygame.display.flip()


screen.blit(open_image2, (0, 0))
pygame.display.flip()


def move():
    global hop
    while hop:
        for event in pygame.event.get():
            global moving, location1, location2, bigger, number, rect_x, rect_y
            global vel_x, vel_y, vel_a, vel_b  # 因为这个是个独立方法，所以用global声明全局变量，作为类的成员函数时可以用self
            global image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12
            if location1 > 0:
                location1 = 0
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(button_up, (0, 0))
                screen.blit(button_down, (0, 50))
                screen.blit(button_back, (1150, 0))
            if location2 > 0:
                location2 = 0
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(button_up, (0, 0))
                screen.blit(button_down, (0, 50))
                screen.blit(button_back, (1150, 0))
            if -(location1 - 1200) > 1000 * (number + 1):
                location1 = -1000 * (number + 1) + 1200
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(button_up, (0, 0))
                screen.blit(button_down, (0, 50))
                screen.blit(button_back, (1150, 0))
            if -(location2 - 600) > 750 * (number + 1):
                location2 = -750 * (number + 1) + 600
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(button_up, (0, 0))
                screen.blit(button_down, (0, 50))
                screen.blit(button_back, (1150, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if 0 < pos_x < 50 and 0 < pos_y < 50:
                    bigger = True
                    if number >= 10:
                        location1 += 500
                        location2 += 250
                    elif number >= 9:
                        number += 1
                        image1 = image1001
                        image2 = image1002
                        image3 = image1003
                        image4 = image1004
                        image5 = image1005
                        image6 = image1006
                        image7 = image1007
                        image8 = image1008
                        image9 = image1009
                        image10 = image1010
                        image11 = image1011
                        image12 = image1012
                    elif number >= 8:
                        number += 1
                        image1 = image2001
                        image2 = image2002
                        image3 = image2003
                        image4 = image2004
                        image5 = image2005
                        image6 = image2006
                        image7 = image2007
                        image8 = image2008
                        image9 = image2009
                        image10 = image2010
                        image11 = image2011
                        image12 = image2012
                    elif number >= 7:
                        number += 1
                        image1 = image301
                        image2 = image302
                        image3 = image303
                        image4 = image304
                        image5 = image305
                        image6 = image306
                        image7 = image307
                        image8 = image308
                        image9 = image309
                        image10 = image310
                        image11 = image311
                        image12 = image312
                    elif number >= 6:
                        number += 1
                        image1 = image401
                        image2 = image402
                        image3 = image403
                        image4 = image404
                        image5 = image405
                        image6 = image406
                        image7 = image407
                        image8 = image408
                        image9 = image409
                        image10 = image410
                        image11 = image411
                        image12 = image412
                    elif number >= 5:
                        number += 1
                        image1 = image501
                        image2 = image502
                        image3 = image503
                        image4 = image504
                        image5 = image505
                        image6 = image506
                        image7 = image507
                        image8 = image508
                        image9 = image509
                        image10 = image510
                        image11 = image511
                        image12 = image512
                    elif number >= 4:
                        number += 1
                        image1 = image601
                        image2 = image602
                        image3 = image603
                        image4 = image604
                        image5 = image605
                        image6 = image606
                        image7 = image607
                        image8 = image608
                        image9 = image609
                        image10 = image610
                        image11 = image611
                        image12 = image612
                    else:
                        number += 1
                        image1 = pygame.image.load('{}/1.png'.format(number))
                        image2 = pygame.image.load('{}/2.png'.format(number))
                        image3 = pygame.image.load('{}/3.png'.format(number))
                        image4 = pygame.image.load('{}/4.png'.format(number))
                        image5 = pygame.image.load('{}/5.png'.format(number))
                        image6 = pygame.image.load('{}/6.png'.format(number))
                        image7 = pygame.image.load('{}/7.png'.format(number))
                        image8 = pygame.image.load('{}/8.png'.format(number))
                        image9 = pygame.image.load('{}/9.png'.format(number))
                        image10 = pygame.image.load('{}/10.png'.format(number))
                        image11 = pygame.image.load('{}/11.png'.format(number))
                        image12 = pygame.image.load('{}/12.png'.format(number))
                    location1 -= 500
                    location2 -= 250
                    screen.fill((0, 0, 0))
                    screen.blit(image1, (location1, location2))
                    screen.blit(image2, (location1 + 250 * (number + 1), location2))
                    screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                    screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                    screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                    screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                    screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                    screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image11,
                                (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image12,
                                (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(button_up, (0, 0))
                    screen.blit(button_down, (0, 50))
                    screen.blit(button_back, (1150, 0))
                elif 0 < pos_x < 50 and 50 < pos_y < 100:
                    bigger = True
                    if number <= 1:
                        location1 -= 500
                        location2 -= 250
                    elif number == 10:
                        number -= 1
                        image1 = image2001
                        image2 = image2002
                        image3 = image2003
                        image4 = image2004
                        image5 = image2005
                        image6 = image2006
                        image7 = image2007
                        image8 = image2008
                        image9 = image2009
                        image10 = image2010
                        image11 = image2011
                        image12 = image2012
                    elif number == 9:
                        number -= 1
                        image1 = image301
                        image2 = image302
                        image3 = image303
                        image4 = image304
                        image5 = image305
                        image6 = image306
                        image7 = image307
                        image8 = image308
                        image9 = image309
                        image10 = image310
                        image11 = image311
                        image12 = image312
                    elif number == 8:
                        number -= 1
                        image1 = image401
                        image2 = image402
                        image3 = image403
                        image4 = image404
                        image5 = image405
                        image6 = image406
                        image7 = image407
                        image8 = image408
                        image9 = image409
                        image10 = image410
                        image11 = image411
                        image12 = image412
                    elif number == 7:
                        number -= 1
                        image1 = image501
                        image2 = image502
                        image3 = image503
                        image4 = image504
                        image5 = image505
                        image6 = image506
                        image7 = image507
                        image8 = image508
                        image9 = image509
                        image10 = image510
                        image11 = image511
                        image12 = image512
                    elif number == 6:
                        number -= 1
                        image1 = image601
                        image2 = image602
                        image3 = image603
                        image4 = image604
                        image5 = image605
                        image6 = image606
                        image7 = image607
                        image8 = image608
                        image9 = image609
                        image10 = image610
                        image11 = image611
                        image12 = image612
                    else:
                        number -= 1
                        image1 = pygame.image.load('{}/1.png'.format(number))
                        image2 = pygame.image.load('{}/2.png'.format(number))
                        image3 = pygame.image.load('{}/3.png'.format(number))
                        image4 = pygame.image.load('{}/4.png'.format(number))
                        image5 = pygame.image.load('{}/5.png'.format(number))
                        image6 = pygame.image.load('{}/6.png'.format(number))
                        image7 = pygame.image.load('{}/7.png'.format(number))
                        image8 = pygame.image.load('{}/8.png'.format(number))
                        image9 = pygame.image.load('{}/9.png'.format(number))
                        image10 = pygame.image.load('{}/10.png'.format(number))
                        image11 = pygame.image.load('{}/11.png'.format(number))
                        image12 = pygame.image.load('{}/12.png'.format(number))
                    location1 += 500
                    location2 += 250
                    screen.fill((0, 0, 0))
                    screen.blit(image1, (location1, location2))
                    screen.blit(image2, (location1 + 250 * (number + 1), location2))
                    screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                    screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                    screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                    screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                    screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                    screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(button_up, (0, 0))
                    screen.blit(button_down, (0, 50))
                    screen.blit(button_back, (1150, 0))
                elif 1150 < pos_x < 1200 and 0 < pos_y < 50:
                    hop = False
                    continue
                else:
                    moving = True
                    vel_x, vel_y = location1, location2
                    vel_a, vel_b = pygame.mouse.get_pos()
            vel_c, vel_d = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if bigger:
                    bigger = False
                else:
                    moving = False
                    location1 = -(vel_a - vel_x) + vel_c
                    location2 = -(vel_b - vel_y) + vel_d
                    vel_x, vel_y = 0, 0
                    vel_a, vel_b = 0, 0
                    screen.fill((0, 0, 0))
                    screen.blit(image1, (location1, location2))
                    screen.blit(image2, (location1 + 250 * (number + 1), location2))
                    screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                    screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                    screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                    screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                    screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                    screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(button_up, (0, 0))
                    screen.blit(button_down, (0, 50))
                    screen.blit(button_back, (1150, 0))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
            if moving:
                location1 = -(vel_a - vel_x) + vel_c
                location2 = -(vel_b - vel_y) + vel_d
                screen.fill((0, 0, 0))
                screen.blit(image1, (location1, location2))
                screen.blit(image2, (location1 + 250 * (number + 1), location2))
                screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                screen.blit(button_up, (0, 0))
                screen.blit(button_down, (0, 50))
                screen.blit(button_back, (1150, 0))
            pygame.display.flip()


if True:
    screen.blit(open_image2, (0, 0))
    pygame.display.flip()
    image301 = pygame.image.load('8/1.png')
    image302 = pygame.image.load('8/2.png')
    image1007 = pygame.image.load('10/7.png')
    screen.blit(open_image2, (0, 0))
    pygame.display.flip()
    image303 = pygame.image.load('8/3.png')
    image304 = pygame.image.load('8/4.png')
    image305 = pygame.image.load('8/5.png')
    screen.blit(open_image2, (0, 0))
    pygame.display.flip()
    image306 = pygame.image.load('8/6.png')
    image307 = pygame.image.load('8/7.png')
    image308 = pygame.image.load('8/8.png')
    screen.blit(open_image2, (0, 0))
    pygame.display.flip()
    image309 = pygame.image.load('8/9.png')
    image310 = pygame.image.load('8/10.png')
    image311 = pygame.image.load('8/11.png')
    image312 = pygame.image.load('8/12.png')
    screen.blit(open_image3, (0, 0))
    pygame.display.flip()
    clip3 = VideoFileClip(r'video/10z.mp4')
    clip4 = VideoFileClip(r'video/1z.mp4')
    image401 = pygame.image.load('7/1.png')
    image402 = pygame.image.load('7/2.png')
    image403 = pygame.image.load('7/3.png')
    image404 = pygame.image.load('7/4.png')
    image405 = pygame.image.load('7/5.png')
    screen.blit(open_image3, (0, 0))
    pygame.display.flip()
    image406 = pygame.image.load('7/6.png')
    image407 = pygame.image.load('7/7.png')
    image408 = pygame.image.load('7/8.png')
    image409 = pygame.image.load('7/9.png')
    image410 = pygame.image.load('7/10.png')
    screen.blit(open_image3, (0, 0))
    pygame.display.flip()
    image411 = pygame.image.load('7/11.png')
    image412 = pygame.image.load('7/12.png')
    screen.blit(open_image4, (0, 0))
    pygame.display.flip()
    clip5 = VideoFileClip(r'video/1l.mp4')
    image501 = pygame.image.load('6/1.png')
    image502 = pygame.image.load('6/2.png')
    image503 = pygame.image.load('6/3.png')
    image504 = pygame.image.load('6/4.png')
    screen.blit(open_image4, (0, 0))
    pygame.display.flip()
    image505 = pygame.image.load('6/5.png')
    image506 = pygame.image.load('6/6.png')
    image507 = pygame.image.load('6/7.png')
    screen.blit(open_image4, (0, 0))
    pygame.display.flip()
    image508 = pygame.image.load('6/8.png')
    image509 = pygame.image.load('6/9.png')
    image510 = pygame.image.load('6/10.png')
    screen.blit(open_image5, (0, 0))
    pygame.display.flip()
    image511 = pygame.image.load('6/11.png')
    image512 = pygame.image.load('6/12.png')
    screen.blit(open_image5, (0, 0))
    pygame.display.flip()
    image601 = pygame.image.load('5/1.png')
    image602 = pygame.image.load('5/2.png')
    screen.blit(open_image5, (0, 0))
    pygame.display.flip()
    image603 = pygame.image.load('5/3.png')
    image604 = pygame.image.load('5/4.png')
    image1010 = pygame.image.load('10/10.png')
    screen.blit(open_image5, (0, 0))
    pygame.display.flip()
    image605 = pygame.image.load('5/5.png')
    image606 = pygame.image.load('5/6.png')
    image607 = pygame.image.load('5/7.png')
    image608 = pygame.image.load('5/8.png')
    screen.blit(open_image5, (0, 0))
    pygame.display.flip()
    image609 = pygame.image.load('5/9.png')
    image610 = pygame.image.load('5/10.png')
    image611 = pygame.image.load('5/11.png')
    image612 = pygame.image.load('5/12.png')
    screen.blit(open_image6, (0, 0))
    pygame.display.flip()
    image2001 = pygame.image.load('9/1.png')
    image2002 = pygame.image.load('9/2.png')
    image2003 = pygame.image.load('9/3.png')
    screen.blit(open_image6, (0, 0))
    pygame.display.flip()
    image2004 = pygame.image.load('9/4.png')
    image2005 = pygame.image.load('9/5.png')
    image2006 = pygame.image.load('9/6.png')
    screen.blit(open_image7, (0, 0))
    pygame.display.flip()
    image2007 = pygame.image.load('9/7.png')
    image2008 = pygame.image.load('9/8.png')
    image2009 = pygame.image.load('9/9.png')
    screen.blit(open_image7, (0, 0))
    pygame.display.flip()
    image2010 = pygame.image.load('9/10.png')
    image2011 = pygame.image.load('9/11.png')
    image2012 = pygame.image.load('9/12.png')
    screen.blit(open_image8, (0, 0))
    pygame.display.flip()
    image1001 = pygame.image.load('10/1.png')
    image1002 = pygame.image.load('10/2.png')
    image1003 = pygame.image.load('10/3.png')
    screen.blit(open_image8, (0, 0))
    pygame.display.flip()
    image1004 = pygame.image.load('10/4.png')
    image1005 = pygame.image.load('10/5.png')
    image1006 = pygame.image.load('10/6.png')
    screen.blit(open_image8, (0, 0))
    pygame.display.flip()
    image1008 = pygame.image.load('10/8.png')
    image1009 = pygame.image.load('10/9.png')
    screen.blit(open_image8, (0, 0))
    pygame.display.flip()
    image1011 = pygame.image.load('10/11.png')
    image1012 = pygame.image.load('10/12.png')
    screen.blit(open_image9, (0, 0))
    pygame.display.flip()
    pygame.mixer.music.load(musiclist[musicplayer])
    pygame.mixer.music.play()
for i in range(10):  # 这是奖池的主页面图片
    local_image_main.set_alpha(50 * i)
    screen.blit(local_image_main, (0, 0))
    pygame.display.flip()
while True:
    size = weight, height = 1200, 600
    screen = pygame.display.set_mode(size)
    screen.blit(local_image_main, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 955 < mouse_x < 1010 and 0 < mouse_y < 110:
                super_super = True
                aa = True
                pr1 = listw[0]
                pr2 = listw[1]
                pr3 = listw[2]
                pr4 = listw[3]
                pr5 = listw[4]
                while super_super:
                    tupian = pygame.transform.scale(tupian, (1200, 600))
                    tupian.set_alpha(55555)
                    back_local = False
                    size = weight, height = 1200, 600
                    screen = pygame.display.set_mode(size)
                    for i in range(10):
                        tupian.set_alpha(50 * i)
                        screen.blit(tupian, (0, 0))
                        pygame.display.flip()
                    while aa:
                        screen.fill(bg)
                        screen.blit(tupian, (0, 0))
                        if musicplay:
                            screen.blit(musicing2, (1140, 60))
                        else:
                            screen.blit(musicing1, (1140, 60))
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                if (mouse_x > 905) and (mouse_x < 1200) and (mouse_y > 525) and (
                                        mouse_y < 600):  # 十连-------------------------------------------------------
                                    t4 = 10
                                    aa = False
                                    movie_play = True
                                    fff = True
                                elif (mouse_x > 633) and (mouse_x < 905) and (mouse_y > 525) and (
                                        mouse_y < 600):  # 单发-----------------------------------------------------
                                    t4 = 1
                                    aa = False
                                    movie_play = True
                                    gg = True
                                elif (mouse_x > 1125) and (mouse_x < 1200) and (mouse_y > 53) and (
                                        mouse_y < 100):  # 背景音乐---------------------------------------------------
                                    screen.blit(tupian, (0, 0))
                                    if musicplay:
                                        pygame.mixer.music.load(musiclist[musicplayer])
                                        pygame.mixer.music.play()
                                        musicplay = False
                                        screen.blit(musicing1, (1140, 60))
                                    else:
                                        pygame.mixer.music.stop()
                                        musicplay = True
                                        screen.blit(musicing2, (1140, 60))
                                    pygame.display.flip()
                                elif (mouse_x > 390) and (mouse_x < 633) and (mouse_y > 525) and (
                                        mouse_y < 600):  # 自定义抽奖次数-------------------------------------------------
                                    bb = True
                                    while bb:
                                        t4 = enterbox('请输入一个小于等于2000的正整数', image='ooops6.jpg')
                                        try:
                                            if t4.isdecimal():
                                                t4 = int(t4)
                                                if 0 < t4 <= 2000:
                                                    bb = False
                                                    aa = False
                                                    movie_play = False
                                                    oiu = True
                                                else:
                                                    msgbox('请输入一个在0-2000范围内的数字')
                                                    bb = False
                                            else:
                                                msgbox('请输入一个正整数')
                                                bb = False
                                        except AttributeError:  # 这句话用于处理‘用户关闭窗口’的事件------------------------------
                                            bb = False
                                elif (mouse_x > 1072) and (mouse_x < 1104) and (mouse_y > 0) and (
                                        mouse_y < 53):  # 玩家点击原石按钮-----------------------------------------------
                                    msgbox('你想得美')
                                elif (mouse_x > 183) and (mouse_x < 330) and (mouse_y > 553) and (
                                        mouse_y < 600):  # 角色演示播放------------------------------------------------
                                    msgbox('暂无角色演示')
                                elif (mouse_x > 0) and (mouse_x < 150) and (mouse_y > 425) and (mouse_y < 550):  # 定轨
                                    if not wuqi1:
                                        if dingguiobject == 'wuqi':
                                            picture1 = pygame.image.load("guii.jpg")
                                            picture1 = pygame.transform.scale(picture1, (1200, 600))
                                            screen.blit(picture1, (0, 0))
                                            pygame.display.flip()
                                            shenzhudinggui = True
                                            while shenzhudinggui:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                                        if (mouse_x > 750) and (mouse_x < 900) and (mouse_y > 190) and (
                                                                mouse_y < 380):
                                                            buttoning = buttonbox(
                                                                msg='确定要选择“苍古自由之誓”作为你的定轨武器吗？',
                                                                choices=['取消', '确定'],
                                                                image='canggu.jpg')
                                                            if buttoning == '确定':
                                                                shenzhudinggui = False
                                                                dingguiobject = 'canggu'
                                                                tupian = pygame.image.load("gui0.jpg")
                                                                tupian = pygame.transform.scale(tupian, (1200, 600))
                                                                screen.blit(tupian, (0, 0))
                                                                if musicplay:
                                                                    screen.blit(musicing2, (1140, 60))
                                                                else:
                                                                    screen.blit(musicing1, (1140, 60))
                                                                pygame.display.flip()
                                                            else:
                                                                pass
                                                        elif (mouse_x > 900) and (mouse_x < 1050) and (
                                                                mouse_y > 190) and (
                                                                mouse_y < 380):
                                                            buttoning = buttonbox(
                                                                msg='确定要选择“四风原典”作为你的定轨武器吗？',
                                                                choices=['取消', '确定'],
                                                                image='sifeng.jpg')
                                                            if buttoning == '确定':
                                                                shenzhudinggui = False
                                                                dingguiobject = 'sifeng'
                                                                tupian = pygame.image.load("gui0.jpg")
                                                                tupian = pygame.transform.scale(tupian, (1200, 600))
                                                                screen.blit(tupian, (0, 0))
                                                                if musicplay:
                                                                    screen.blit(musicing2, (1140, 60))
                                                                else:
                                                                    screen.blit(musicing1, (1140, 60))
                                                                pygame.display.flip()
                                                            else:
                                                                pass
                                                        elif (mouse_x > 1100) and (mouse_x < 1200) and (
                                                                mouse_y > 0) and (
                                                                mouse_y < 100):
                                                            shenzhudinggui = False
                                                            dingguiobject = 'wuqi'
                                                            screen.blit(tupian, (0, 0))
                                                            if musicplay:
                                                                screen.blit(musicing2, (1140, 60))
                                                            else:
                                                                screen.blit(musicing1, (1140, 60))
                                                            pygame.display.flip()
                                        else:
                                            if dingguiobject == 'canggu':
                                                picture1 = pygame.image.load("guiic.jpg")
                                            elif dingguiobject == 'sifeng':
                                                picture1 = pygame.image.load("guiis.jpg")
                                            picture1 = pygame.transform.scale(picture1, (1200, 600))
                                            screen.blit(picture1, (0, 0))
                                            pygame.display.flip()
                                            shenzhudinggui = True
                                            while shenzhudinggui:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mouse_x, mouse_y = pygame.mouse.get_pos()
                                                        if (mouse_x > 1100) and (mouse_x < 1200) and (mouse_y > 0) and (
                                                                mouse_y < 100):
                                                            shenzhudinggui = False
                                                            screen.blit(tupian, (0, 0))
                                                            if musicplay:
                                                                screen.blit(musicing2, (1140, 60))
                                                            else:
                                                                screen.blit(musicing1, (1140, 60))
                                                            pygame.display.flip()
                                                        elif (mouse_x > 800) and (mouse_x < 1000) and (
                                                                mouse_y > 450) and (
                                                                mouse_y < 510):
                                                            buttoning = buttonbox(msg='确定要取消定轨吗？',
                                                                                  choices=['取消', '确定'])
                                                            if buttoning == '确定':
                                                                shenzhudinggui = False
                                                                dingguiobject = 'wuqi'
                                                                dinggui = 0
                                                                tupian = pygame.image.load("gui.jpg")
                                                                tupian = pygame.transform.scale(tupian, (1200, 600))
                                                                screen.blit(tupian, (0, 0))
                                                                if musicplay:
                                                                    screen.blit(musicing2, (1140, 60))
                                                                else:
                                                                    screen.blit(musicing1, (1140, 60))
                                                                pygame.display.flip()
                                                            else:
                                                                pass
                                    else:
                                        pass
                                elif (mouse_x > 0) and (mouse_x < 90) and (mouse_y > 0) and (
                                        mouse_y < 200):  # 切换祈愿池--------------------------------------------------
                                    prize = choicebox(msg='请选择祈愿奖池', choices=prize_list)
                                    oh = True
                                    if prize is None:
                                        oh = False
                                        screen.fill(bg)
                                        screen.blit(tupian, (0, 0))
                                        pygame.display.flip()
                                        if musicplay:
                                            screen.blit(musicing2, (1140, 60))
                                        else:
                                            screen.blit(musicing1, (1140, 60))
                                        pygame.display.flip()
                                    elif prize == '温迪':
                                        prize1 = '温迪'
                                        prize2 = '温迪'
                                        tupian = pygame.image.load("image/venty.jpg")
                                        listw = ['芭芭拉', '菲谢尔', '香菱', '芭芭拉', '菲谢尔']
                                        wuqi1 = True
                                    elif prize == '甘雨':
                                        prize1 = '甘雨'
                                        prize2 = '甘雨'
                                        tupian = pygame.image.load("image/甘雨.jpg")
                                        listw = ['多莉', '砂糖', '行秋', '多莉', '砂糖']
                                        wuqi1 = True
                                    elif prize == '钟离':
                                        prize1 = '钟离'
                                        prize2 = '钟离'
                                        tupian = pygame.image.load("image/钟离.jpg")
                                        listw = ['柯莱', '迪奥娜', '菲谢尔', '柯莱', '迪奥娜']
                                        wuqi1 = True
                                    elif prize == '武器池':
                                        prize1 = '苍古自由之誓'
                                        prize2 = '四风原典'
                                        tupian = pygame.image.load("gui.jpg")
                                        listw = ['暗巷闪光', '幽夜华尔兹', '雨裁', '西风长枪', '流浪乐章']
                                        wuqi1 = False
                                    else:
                                        prize1 = '刻晴，歪了，但没完全歪！'
                                        prize2 = '刻晴，歪了，但没完全歪！'
                                        tupian = pygame.image.load("image/nb.jpg")
                                        listw = ['芭芭拉', '凝光', '班尼特', '芭芭拉', '凝光']
                                        wuqi1 = True
                                    if oh:
                                        dingguiobject = 'wuqi'
                                        dinggui = 0
                                        a = 0
                                        c = 0
                                        d = 0
                                        sixingfangwai = 0
                                        b1 = 0
                                        b2 = 0
                                        b3 = 0
                                        b4 = 0
                                        b5 = 0
                                        b6 = 0
                                        p = 0
                                        oo = 0
                                        c1 = 0
                                        c2 = 0
                                        c3 = 0
                                        u = 0
                                        po = 0
                                        four_start_low = 0
                                        d1 = 0
                                        d2 = 0
                                        d3 = 0
                                        d4 = 0
                                        d5 = 0
                                        d6 = 0
                                        d7 = 0
                                        d8 = 0
                                        d9 = 0
                                        d10 = 0
                                        m0 = 0
                                        m1 = 0
                                        m2 = 0
                                        m3 = 0
                                        m4 = 0
                                        m5 = 0
                                        m6 = 0
                                        m7 = 0
                                        m8 = 0
                                        m9 = 0
                                        m10 = 0
                                        m11 = 0
                                        m12 = 0
                                        m13 = 0
                                        m14 = 0
                                        m15 = 0
                                        m16 = 0
                                        m17 = 0
                                        m18 = 0
                                        m19 = 0
                                        m20 = 0
                                        m21 = 0
                                        m22 = 0
                                        m23 = 0
                                        m24 = 0
                                        m25 = 0
                                        m26 = 0
                                        m27 = 0
                                        m28 = 0
                                        m29 = 0
                                        m30 = 0
                                        m31 = 0
                                        m32 = 0
                                        m33 = 0
                                        m34 = 0
                                        m35 = 0
                                        m36 = 0
                                        m37 = 0
                                        m38 = 0
                                        m39 = 0
                                        wushichou = 0
                                        liushichou = 0
                                        qishichou = 0
                                        bashichou = 0
                                        wuxingbaodi = 0
                                        chouzhongprize1 = 0
                                        chouzhongprize2 = 0
                                        linshixingchen = 0
                                        linshixinghui = 0
                                        xingchen = 0
                                        xinghui = 0
                                        pr1 = listw[0]
                                        pr2 = listw[1]
                                        pr3 = listw[2]
                                        pr4 = listw[3]
                                        pr5 = listw[4]
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        pygame.init()
                                        screen.fill(bg)
                                        tupian = pygame.transform.scale(tupian, (1200, 600))
                                        screen.blit(tupian, (0, 0))
                                        if musicplay:
                                            screen.blit(musicing2, (1140, 60))
                                        else:
                                            screen.blit(musicing1, (1140, 60))
                                        pygame.display.flip()
                                        msgbox('刷新成功（抽奖数据已被重置）')
                                        screen.fill(bg)
                                        screen.blit(tupian, (0, 0))
                                        pygame.display.flip()
                                        if musicplay:
                                            screen.blit(musicing2, (1140, 60))
                                        else:
                                            screen.blit(musicing1, (1140, 60))
                                        pygame.display.flip()
                                elif (mouse_x > 40) and (mouse_x < 185) and (mouse_y > 550) and (
                                        mouse_y < 600):  # 历史记录查看------------------------------------------------
                                    size = weight, height = 1200, 600
                                    screen = pygame.display.set_mode(size)
                                    screen.fill((0, 0, 0))
                                    msgboxx1 = (
                                        '累计共抽{}发，抽中五星{}发,获得无主的星尘x{},无主的星辉x{}'.format(a, d,
                                                                                                           xingchen,
                                                                                                           xinghui))
                                    if not wuqi1:
                                        msgboxx1535 = (
                                            '在五十抽以下出金{}发,50-59出金{}发,60-69出金{}发,70-79出金{}发,保底{}发'.format(
                                                d - bashichou - liushichou - qishichou - wuxingbaodi, liushichou,
                                                qishichou,
                                                bashichou, wuxingbaodi))
                                        msgboxx2 = (
                                            '歪了{}发，其中天空之刃{}发，天空之琴{}发，天空之傲{}发，天空之卷{}发，天空之脊{}发。'.format(
                                                p, b1 + b5, b2, b3, b4, b6))
                                        msgboxx3 = (
                                            '累计共抽中{}{}发,{}{}发,没歪{}发。累计共抽中四星{}发,保底{}发。'.format(
                                                prize1,
                                                chouzhongprize1,
                                                prize2,
                                                chouzhongprize2,
                                                d - p,
                                                po, four_start_low))
                                        msgboxx4 = (
                                            '其中{}{}发,{}{}发,{}{}发,{}{}发,{}{}发，祭礼剑{}发'.format(pr1, c1, pr2, c2,
                                                                                                       pr3, c3,
                                                                                                       pr4, c4, pr5, c5,
                                                                                                       m1))
                                    else:
                                        msgboxx1535 = (
                                            '在六十抽以下出金{}发,60-69出金{}发,70-79出金{}发,80-89出金{}发,保底{}发'.format(
                                                d - liushichou - qishichou - bashichou - wuxingbaodi, liushichou,
                                                qishichou,
                                                bashichou, wuxingbaodi))
                                        msgboxx2 = (
                                            '歪了{}发，其中迪卢克{}发，刻晴{}发，七七{}发，莫娜{}发，提纳里{}发，琴{}发。'.format(
                                                p, b1,
                                                b2, b3,
                                                b4, b5,
                                                b6))
                                        msgboxx3 = (
                                            '累计共抽中{}{}发。累计共抽中四星{}发，保底{}发。'.format(prize1, d - p, po,
                                                                                                   four_start_low))
                                        msgboxx4 = (
                                            '其中{}{}发,{}{}发,{}{}发,祭礼剑{}发'.format(pr1, c1 + c4, pr2, c2 + c5,
                                                                                         pr3, c3, m1))
                                    msgboxx5 = (
                                        '祭礼残章{}发,祭礼弓{}发,祭礼大剑{}发,西风剑{},发西风秘典{}发,西风猎弓{}发'.format(
                                            m2, m3,
                                            m4, m5,
                                            m6, m7))
                                    msgboxx6 = (
                                        '西风大剑{}发,西风长枪{}发,暗巷闪光{}发,暗巷猎手{}发,暗巷的酒与诗{}发,笛剑{}发'.format(
                                            m8,
                                            m9,
                                            m10,
                                            m11,
                                            m12,
                                            m13))
                                    msgboxx7 = (
                                        '辰纱之纺锤{},发匣里龙吟{}发,匣里灭辰{}发,绝弦,{}发，弓藏{}发,恶王丸{}发'.format(
                                            m14, m15,
                                            m16, m17,
                                            m18, m19, ))
                                    msgboxx8 = (
                                        '幽夜华尔兹{}发,雨裁{}发,千岩古剑{}发,千岩长枪{}发,昭心{}发,流浪乐章{}发'.format(
                                            m20, m21,
                                            m22, m23,
                                            m24, m25))
                                    msgboxx9 = (
                                        '芭芭拉{}发,行秋{}发,菲谢尔{}发,云堇{}发,凝光{}发,罗莎莉亚{}发,雷泽{}发'.format(
                                            m26, m27,
                                            m28, m29,
                                            m30, m31,
                                            m32))
                                    msgboxx10 = (
                                        '重云{}发,早柚{},砂糖{}发,班尼特{}发,烟绯{}发,香菱{}发,托马{}发'.format(m33,
                                                                                                                m34,
                                                                                                                m35,
                                                                                                                m36,
                                                                                                                m37,
                                                                                                                m38,
                                                                                                                m39))
                                    msgboxx11 = (
                                        '累计共抽中三星{}发，其中飞天御剑{}发，飞天大御剑{}发'.format(a - d - po, d1, d2))
                                    msgboxx1147 = (
                                        '神射手之誓{}发，黑缨枪{}发,以理服人{}发,冷刃{}发'.format(d3, d4, d5, d6))
                                    msgboxx1148 = (
                                        '黎明神剑{}发，讨龙英杰谭{}发，魔导绪论{}发，沐浴龙血的剑{}发。'.format(d7, d8, d9,
                                                                                                            d10))
                                    backing = '返回'
                                    fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                                    font1 = fonting.render(msgboxx1, True, (255, 255, 0))
                                    font1535 = fonting.render(msgboxx1535, True, (255, 255, 0))
                                    font2 = fonting.render(msgboxx2, True, (255, 255, 0))
                                    font3 = fonting.render(msgboxx3, True, (255, 255, 0))
                                    font4 = fonting.render(msgboxx4, True, green)
                                    font5 = fonting.render(msgboxx5, True, green)
                                    font6 = fonting.render(msgboxx6, True, green)
                                    font7 = fonting.render(msgboxx7, True, green)
                                    font8 = fonting.render(msgboxx8, True, green)
                                    font9 = fonting.render(msgboxx9, True, green)
                                    font10 = fonting.render(msgboxx10, True, green)
                                    font11 = fonting.render(msgboxx11, True, green)
                                    font12 = fonting.render(backing, True, (255, 0, 0))
                                    font13 = fonting.render(msgboxx1147, True, green)
                                    font14 = fonting.render(msgboxx1148, True, green)
                                    screen.blit(font1, (30, 30))
                                    screen.blit(font1535, (30, 70))
                                    screen.blit(font2, (30, 110))
                                    screen.blit(font3, (30, 150))
                                    screen.blit(font4, (30, 190))
                                    screen.blit(font5, (30, 230))
                                    screen.blit(font6, (30, 270))
                                    screen.blit(font7, (30, 310))
                                    screen.blit(font8, (30, 350))
                                    screen.blit(font9, (30, 390))
                                    screen.blit(font10, (30, 430))
                                    screen.blit(font11, (30, 470))
                                    screen.blit(font12, (1130, 30))
                                    screen.blit(font13, (30, 510))
                                    screen.blit(font14, (30, 550))
                                    pygame.display.flip()
                                    flags = True
                                    while flags:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit(0)
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                                if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (
                                                        mouse_y < 100):  # 退出历史记录查看----------------------------------------
                                                    flags = False
                                                    screen.fill((0, 0, 0))
                                                    screen.blit(tupian, (0, 0))
                                                    if musicplay:
                                                        screen.blit(musicing2, (1140, 60))
                                                    else:
                                                        screen.blit(musicing1, (1140, 60))
                                                    pygame.display.flip()
                                elif (mouse_x > 1126) and (mouse_x < 1200) and (mouse_y > 0) and (
                                        mouse_y < 53):
                                    super_super = False
                                    aa = False
                                    back_local = True
                                    for i in range(10):
                                        screen.fill(bg)
                                        tupian.set_alpha(500 - (50 * i))
                                        screen.blit(tupian, (0, 0))
                                        pygame.display.flip()
                                    for i in range(10):
                                        screen.fill(bg)
                                        local_image_main.set_alpha(50 * i)
                                        screen.blit(local_image_main, (0, 0))
                                        pygame.display.flip()
                                    if musicplay:
                                        screen.blit(musicing2, (1140, 60))
                                    else:
                                        screen.blit(musicing1, (1140, 60))
                                    continue
                            elif event.type == pygame.KEYDOWN:
                                try:
                                    if chr(event.key) == 'h':
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill((0, 0, 0))
                                        msgboxx3 = '帮助:'
                                        msgboxx4 = '按左上角可以切换祈愿池，按右上角可以重置祈愿，按左下角对应按键可以观看角色演示和历史记录。'
                                        msgboxx5 = '注：自定义抽奖次数的抽奖结果需要去shell界面查看。点击祈愿后，会有1-2秒延迟，属正常现象'
                                        msgboxx6 = '可使用「神铸定轨」对本期五星UP武器「单手剑·苍古自由之誓」或「法器·四风原典」进行定轨'
                                        msgboxx7 = '一般情况下所有角色或武器均适用基础概率，如触发概率UP，保底等以具体规则为准'
                                        msgboxx8 = '退出此页面后按‘F’键或点击右上角暂停图标播放/暂停音乐,按‘E’键强制刷新当前页面'
                                        msgboxx9 = '退出此页面后按‘R’键播放下一首,按‘T’键播放上一首,按‘O’键调高音量,按‘P’键调低音量'
                                        # msgboxxc = '关于背景音乐详细信息请退出此页面后按‘L’键查询'
                                        msgboxx100 = '定轨功能之后会进一步更新'
                                        msgboxx101 = '关于祈愿物品公示请退出此页面后按‘M’键查询'
                                        msgboxx102 = '关于祈愿内置详细信息请退出此页面后按‘N’键查询'
                                        backing = '返回'
                                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                                        font3 = fonting.render(msgboxx3, True, (255, 0, 0))
                                        font4 = fonting.render(msgboxx4, True, green)
                                        font5 = fonting.render(msgboxx5, True, green)
                                        font6 = fonting.render(msgboxx6, True, green)
                                        font7 = fonting.render(msgboxx7, True, green)
                                        font8 = fonting.render(msgboxx8, True, green)
                                        font9 = fonting.render(msgboxx9, True, green)
                                        font100 = fonting.render(msgboxx100, True, (255, 0, 255))
                                        font101 = fonting.render(msgboxx101, True, (255, 0, 255))
                                        font102 = fonting.render(msgboxx102, True, (255, 0, 255))
                                        font103 = fonting.render(backing, True, (255, 0, 0))
                                        screen.blit(font3, (30, 30))
                                        screen.blit(font4, (30, 70))
                                        screen.blit(font5, (30, 110))
                                        screen.blit(font6, (30, 150))
                                        screen.blit(font7, (30, 190))
                                        screen.blit(font8, (30, 230))
                                        screen.blit(font9, (30, 270))
                                        screen.blit(font100, (30, 310))
                                        screen.blit(font101, (30, 350))
                                        screen.blit(font102, (30, 390))
                                        screen.blit(font103, (1130, 30))
                                        pygame.display.flip()
                                        flags = True
                                        while flags:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit(0)
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                                    if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (
                                                            mouse_y < 100):  # 退出历史记录查看---------------------------
                                                        flags = False
                                                        screen.fill((0, 0, 0))
                                                        screen.blit(tupian, (0, 0))
                                                        if musicplay:
                                                            screen.blit(musicing2, (1140, 60))
                                                        else:
                                                            screen.blit(musicing1, (1140, 60))
                                                        pygame.display.flip()
                                    elif chr(event.key) == 'f':
                                        screen.blit(tupian, (0, 0))
                                        if musicplay:
                                            pygame.mixer.music.load(musiclist[musicplayer])
                                            pygame.mixer.music.play()
                                            musicplay = False
                                            screen.blit(musicing1, (1140, 60))
                                        else:
                                            pygame.mixer.music.stop()
                                            musicplay = True
                                            screen.blit(musicing2, (1140, 60))
                                        pygame.display.flip()
                                    elif chr(event.key) == 'r':
                                        if musicplayer == yinyueshuliang:
                                            musicplayer = 0
                                        else:
                                            musicplayer += 1
                                        pygame.mixer.music.load(musiclist[musicplayer])
                                        pygame.mixer.music.play()
                                    elif chr(event.key) == 't':
                                        if musicplayer == 0:
                                            musicplayer = yinyueshuliang
                                        else:
                                            musicplayer -= 1
                                        pygame.mixer.music.load(musiclist[musicplayer])
                                        pygame.mixer.music.play()
                                    elif chr(event.key) == 'o':
                                        if musicloud >= 1:
                                            musicloud = 1
                                            msgbox('音量已是最大')
                                        else:
                                            musicloud += 0.2
                                        pygame.mixer.music.set_volume(musicloud)
                                    elif chr(event.key) == 'p':
                                        if musicloud <= 0:
                                            musicloud = 0
                                            msgbox('音量已是最小')
                                        else:
                                            musicloud -= 0.2
                                        pygame.mixer.music.set_volume(musicloud)
                                    elif chr(event.key) == 'e':
                                        screen.blit(tupian, (0, 0))
                                        if musicplay:
                                            screen.blit(musicing2, (1140, 60))
                                        else:
                                            screen.blit(musicing1, (1140, 60))
                                        pygame.display.flip()
                                    elif chr(event.key) == 'l':
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill((0, 0, 0))
                                        msgboxx1 = '歌曲列表'
                                        msgboxx2 = '1.镇守之森(Her Legacy·Hanachirusato·Time to say Farewell)'
                                        msgboxx4 = '2.何妄何执(雷电将军)'
                                        msgboxx5 = '3.甘雨(角色演示)'
                                        msgboxx6 = '4.璃月港-昼'
                                        msgboxx7 = '5.飞彩镌流年·海灯节2022'
                                        msgboxx8 = '6.温迪(角色演示)'
                                        msgboxx10 = '7.徐浚皓1'
                                        msgboxx11 = '8.徐浚皓2'
                                        backing = '返回'
                                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                                        font1 = fonting.render(msgboxx1, True, (255, 0, 255))
                                        font2 = fonting.render(msgboxx2, True, green)
                                        font4 = fonting.render(msgboxx4, True, green)
                                        font5 = fonting.render(msgboxx5, True, green)
                                        font6 = fonting.render(msgboxx6, True, green)
                                        font7 = fonting.render(msgboxx7, True, green)
                                        font8 = fonting.render(msgboxx8, True, green)
                                        font10 = fonting.render(msgboxx10, True, green)
                                        font11 = fonting.render(msgboxx11, True, green)
                                        font12 = fonting.render(backing, True, (255, 0, 0))
                                        screen.blit(font1, (30, 30))
                                        screen.blit(font2, (30, 70))
                                        screen.blit(font4, (30, 110))
                                        screen.blit(font5, (30, 150))
                                        screen.blit(font6, (30, 190))
                                        screen.blit(font7, (30, 230))
                                        screen.blit(font8, (30, 270))
                                        screen.blit(font10, (30, 310))
                                        screen.blit(font11, (30, 350))
                                        screen.blit(font12, (1130, 30))
                                        pygame.display.flip()
                                        flags = True
                                        while flags:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit(0)
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                                    if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (
                                                            mouse_y < 100):
                                                        flags = False
                                                        screen.fill((0, 0, 0))
                                                        screen.blit(tupian, (0, 0))
                                                        if musicplay:
                                                            screen.blit(musicing2, (1140, 60))
                                                        else:
                                                            screen.blit(musicing1, (1140, 60))
                                                        pygame.display.flip()
                                    elif chr(event.key) == 'm':
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill((0, 0, 0))
                                        msg1 = 'Available five-star characters(不包括UP的角色)'
                                        msgboxx2 = '迪卢克、刻晴、七七、莫娜、提纳里、琴'
                                        msgboxx3 = 'Available five-star weapons(不包括UP的武器)'
                                        msgboxx4 = '天空之刃、天空之琴、天空之傲、天空之卷、天空之脊'
                                        msgboxx5 = 'Available four-star objects(不包括UP的角色或武器)'
                                        msgboxx6 = '祭礼剑、祭礼残章、祭礼弓、祭礼大剑、西风剑、西风秘典、西风猎弓、西风大剑、西风长枪、暗巷闪光'
                                        msgboxx7 = '暗巷猎手、暗巷的酒与诗、笛剑、辰纱之纺锤、匣里龙吟、匣里灭辰、绝弦、弓藏、恶王丸、幽夜华尔兹'
                                        msgboxx8 = '雨裁、千岩古剑、千岩长枪、昭心、流浪乐章、芭芭拉、行秋、菲谢尔、云堇、凝光、罗莎莉亚、雷泽'
                                        msgboxx9 = '重云、早柚、砂糖、班尼特、烟绯、香菱。'
                                        msgboxx10 = 'Available three-star weapons'
                                        msgboxx11 = '飞天御剑、飞天大御剑、神射手之誓、黑缨枪、以理服人、冷刃、黎明神剑、讨龙英杰谭、魔导绪论、沐'
                                        msgboxx12 = '浴龙血的剑'
                                        backing = '返回'
                                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                                        font1 = fonting.render(msg1, True, (255, 0, 0))
                                        font2 = fonting.render(msgboxx2, True, green)
                                        font3 = fonting.render(msgboxx3, True, (255, 0, 0))
                                        font4 = fonting.render(msgboxx4, True, green)
                                        font5 = fonting.render(msgboxx5, True, (255, 0, 0))
                                        font6 = fonting.render(msgboxx6, True, green)
                                        font7 = fonting.render(msgboxx7, True, green)
                                        font8 = fonting.render(msgboxx8, True, green)
                                        font9 = fonting.render(msgboxx9, True, green)
                                        font10 = fonting.render(msgboxx10, True, (255, 0, 0))
                                        font11 = fonting.render(msgboxx11, True, green)
                                        font12 = fonting.render(backing, True, (255, 0, 0))
                                        font13 = fonting.render(msgboxx12, True, green)
                                        screen.blit(font1, (30, 30))
                                        screen.blit(font2, (30, 70))
                                        screen.blit(font3, (30, 110))
                                        screen.blit(font4, (30, 150))
                                        screen.blit(font5, (30, 190))
                                        screen.blit(font6, (30, 230))
                                        screen.blit(font7, (30, 270))
                                        screen.blit(font8, (30, 310))
                                        screen.blit(font9, (30, 350))
                                        screen.blit(font10, (30, 390))
                                        screen.blit(font11, (30, 430))
                                        screen.blit(font12, (1130, 30))
                                        screen.blit(font13, (30, 470))
                                        pygame.display.flip()
                                        flags = True
                                        while flags:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit(0)
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                                    if (mouse_x > 1090) and (mouse_x < 1200) and (mouse_y > 0) and (
                                                            mouse_y < 100):  # 退出历史记录查看----------------------------------------
                                                        flags = False
                                                        screen.fill((0, 0, 0))
                                                        screen.blit(tupian, (0, 0))
                                                        if musicplay:
                                                            screen.blit(musicing2, (1140, 60))
                                                        else:
                                                            screen.blit(musicing1, (1140, 60))
                                                        pygame.display.flip()
                                    elif chr(event.key) == 'n':
                                        size = weight, height = 1200, 600
                                        screen = pygame.display.set_mode(size)
                                        screen.fill((0, 0, 0))
                                        msgbox1 = '官方公布的祈愿机制'
                                        msgboxx1 = '在活动祈愿中,五星角色祈愿的基础概率为0.6%,综合概率(含保底)为1.6%,五星武器祈愿的基'
                                        msgboxx2 = '础概率为0.7%,综合概率(含保底)为1.85%,最多90次祈愿内必定能通过保底获取5星物品。当祈'
                                        msgboxx3 = '愿获取到五星角色或武器时,有50%的概率为本期UP角色或武器。如果本次祈愿获取的五星角色'
                                        msgbox3 = (
                                            '或武器非本期UP角色或武器,下次祈愿获取的五星角色必定为本期UP的五星角色或武器。')
                                        msgboxx4 = (
                                            '在活动祈愿中，四星物品祈愿的基础概率为5.1%(角色武器各占一半)，综合概率(含保底)为13%')
                                        msgboxx5 = (
                                            '，最多10次祈愿内必定能通过保底获取4星或以上物品，通过保底获取四星物品的概率为99.4%,')
                                        msgboxx6 = (
                                            '获取五星角色的概率为0.6%。当祈愿获取到四星角色或武器时，有50%的概率为本期UP角色或')
                                        msgboxx7 = (
                                            '武器。如果本次祈愿获取的四星角色或武器非本期UP角色或武器，下次祈愿获取的四星角色必定')
                                        msgboxx8 = '为本期UP的四星角色或武器。'  # https://www.bilibili.com/video/BV1mb4y1S7Td/?spm_id_from=trigger_reload
                                        msgboxx9 = '获得四星武器时，会同时获得两个无主的星辉作为副产物，获得三星武器时，会同时获得十五个'
                                        msgboxx10 = '无主的星尘作为副产物。第2-7次获得相同的角色时，五星会转化为10个无主的星辉和一个对应'
                                        msgboxx11 = '角色的命星，四星会转化为2个无主的星辉和一个对应角色的命星。第八次及以上获得重复角色'
                                        backing = '返回'
                                        backing2 = '下一页'
                                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 26)
                                        font1113 = fonting.render(msgbox1, True, (255, 0, 0))
                                        font1 = fonting.render(msgboxx1, True, green)
                                        font2 = fonting.render(msgboxx2, True, green)
                                        font3 = fonting.render(msgboxx3, True, green)
                                        font31 = fonting.render(msgbox3, True, green)
                                        font4 = fonting.render(msgboxx4, True, green)
                                        font5 = fonting.render(msgboxx5, True, green)
                                        font6 = fonting.render(msgboxx6, True, green)
                                        font7 = fonting.render(msgboxx7, True, green)
                                        font8 = fonting.render(msgboxx8, True, green)
                                        font9 = fonting.render(msgboxx9, True, green)
                                        font10 = fonting.render(msgboxx10, True, green)
                                        font11 = fonting.render(msgboxx11, True, green)
                                        font12 = fonting.render(backing, True, (255, 0, 0))
                                        font0 = fonting.render(backing2, True, (255, 0, 0))
                                        screen.blit(font1113, (30, 30))
                                        screen.blit(font1, (30, 70))
                                        screen.blit(font2, (30, 110))
                                        screen.blit(font3, (30, 150))
                                        screen.blit(font31, (30, 190))
                                        screen.blit(font4, (30, 230))
                                        screen.blit(font5, (30, 270))
                                        screen.blit(font6, (30, 310))
                                        screen.blit(font7, (30, 350))
                                        screen.blit(font8, (30, 390))
                                        screen.blit(font9, (30, 430))
                                        screen.blit(font10, (30, 470))
                                        screen.blit(font11, (30, 510))
                                        screen.blit(font12, (1130, 30))
                                        screen.blit(font0, (1100, 560))
                                        pygame.display.flip()
                                        flags = True
                                        while flags:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit(0)
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                                    if 1090 < mouse_x < 1200 and 0 < mouse_y < 100:
                                                        flags = False
                                                        screen.fill((0, 0, 0))
                                                        screen.blit(tupian, (0, 0))
                                                        if musicplay:
                                                            screen.blit(musicing2, (1140, 60))
                                                        else:
                                                            screen.blit(musicing1, (1140, 60))
                                                        pygame.display.flip()
                                                    elif (mouse_x > 1070) and (mouse_x < 1200) and (mouse_y > 500) and (
                                                            mouse_y < 600):  # 退出历史记录查看----------------------------------------
                                                        flags = False
                                                        screen.fill((0, 0, 0))
                                                        msgboxx12 = '时，五星将转化为25个无主的星辉，四星会转化为5个无主的星辉'
                                                        msgboxx1 = '官方实质的祈愿机制'
                                                        msgboxx2 = '在角色活动祈愿中,五星0-73发基础概率为0.6%,74-89发基础概率为0.6%+(n-73)*6%,综合'
                                                        msgboxx3 = (
                                                            '概率(含保底)为1.605%,在武器活动祈愿中,五星祈愿1-62的基础概率为0.7%,63-73的基础概率')
                                                        msgboxx4 = (
                                                            '为0.7%+(n-62)*7%,74-79发的基础概率为77.7%+(n-73)*3.5%,综合概率(含保底)为1.878%')
                                                        msgboxx5 = (
                                                            '在角色活动祈愿中四星1-8发基础概率为5.1%,第九发基础概率为56.1%,综合概率(含保底)为')
                                                        msgboxx6 = (
                                                            '13.057%。在武器活动祈愿中,四星1-7发的基础概率为6%,第八发的基础概率为66%,第九发的')
                                                        msgboxx7 = '基础概率为96%,综合概率(含保底)为14.841%。'
                                                        backing = '返回'
                                                        pygame.display.flip()
                                                        font111 = fonting.render(msgboxx12, True, green)
                                                        font1 = fonting.render(msgboxx1, True, (255, 0, 0))
                                                        font2 = fonting.render(msgboxx2, True, green)
                                                        font3 = fonting.render(msgboxx3, True, green)
                                                        font4 = fonting.render(msgboxx4, True, green)
                                                        font5 = fonting.render(msgboxx5, True, green)
                                                        font6 = fonting.render(msgboxx6, True, green)
                                                        font7 = fonting.render(msgboxx7, True, green)
                                                        font12 = fonting.render(backing, True, (255, 0, 0))
                                                        screen.blit(font111, (30, 30))
                                                        screen.blit(font1, (30, 70))
                                                        screen.blit(font2, (30, 110))
                                                        screen.blit(font3, (30, 150))
                                                        screen.blit(font4, (30, 190))
                                                        screen.blit(font5, (30, 230))
                                                        screen.blit(font6, (30, 270))
                                                        screen.blit(font7, (30, 310))
                                                        screen.blit(font12, (1130, 30))
                                                        pygame.display.flip()
                                                        flags = True
                                                        while flags:
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    sys.exit(0)
                                                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                                                    if (mouse_x > 1090) and (mouse_x < 1200) and (
                                                                            mouse_y > 0) and (
                                                                            mouse_y < 100):
                                                                        flags = False
                                                                        screen.fill((0, 0, 0))
                                                                        screen.blit(tupian, (0, 0))
                                                                        if musicplay:
                                                                            screen.blit(musicing2, (1140, 60))
                                                                        else:
                                                                            screen.blit(musicing1, (1140, 60))
                                                                        pygame.display.flip()
                                except Exception:
                                    screen.blit(tupian, (0, 0))
                                    if musicplay:
                                        screen.blit(musicing2, (1140, 60))
                                    else:
                                        screen.blit(musicing1, (1140, 60))
                                    pygame.display.flip()
                    if movie_play:
                        screen = pygame.display.set_mode((1200, 673))
                        for i in range(10):
                            great_img.set_alpha(500 - 50 * i)
                            screen.blit(great_img, (0, 0))
                            pygame.display.flip()
                    if True:
                        if back_local:
                            continue
                        for itt in range(t4):
                            screen.fill((0, 0, 0))
                            a += 1
                            aa = True
                            bb = True
                            if wuqi1:
                                if c <= 60:
                                    b = 3
                                elif c <= 73:
                                    b = 10
                                elif c <= 88:
                                    b = 30 * (c - 73)
                                else:
                                    b = 500
                            else:
                                if c <= 50:
                                    b = 3
                                elif c <= 63:
                                    b = 10
                                elif c <= 73:
                                    b = 35 * (c - 62)
                                elif c < 79:
                                    b = 388 + 17.5 * (c - 73)
                                else:
                                    b = 500
                            e = random.randint(1, 500)
                            if e <= b:
                                xinghui += 10
                                linshixinghui += 10
                                if wuqi1:
                                    julibaodi = 89 - c
                                else:
                                    julibaodi = 79 - c
                                if 20 < julibaodi <= 30:
                                    liushichou += 1
                                elif 10 < julibaodi <= 20:
                                    qishichou += 1
                                elif 0 < julibaodi <= 10:
                                    bashichou += 1
                                elif julibaodi <= 0:
                                    wuxingbaodi += 1
                                kq1 = 1
                                d += 1
                                if not wuqi1:
                                    if dingguiobject != 'wuqi':
                                        if dinggui >= 2:
                                            if dingguiobject == 'canggu':
                                                listing.append(
                                                    '{}，距离保底{}发---------------'.format(prize1, julibaodi))
                                                chouzhongprize1 += 1
                                                dinggui = 0
                                                oo = 0
                                                dingguiobject = 'wuqi'
                                            elif dingguiobject == 'sifeng':
                                                listing.append(
                                                    '{}，距离保底{}发---------------'.format(prize2, julibaodi))
                                                dinggui = 0
                                                chouzhongprize2 += 1
                                                dingguiobject = 'wuqi'
                                                oo = 0
                                            c = 0
                                            continue
                                if oo >= 1:
                                    wuxingpanding = random.randint(1, 2)
                                    if wuxingpanding == 1:
                                        listing.append('{}，距离保底{}发---------------'.format(prize1, julibaodi))
                                        chouzhongprize1 += 1
                                        if not wuqi1:
                                            if dingguiobject == 'canggu':
                                                dinggui = 0
                                                dingguiobject = 'wuqi'
                                            else:
                                                dinggui += 1
                                    else:
                                        listing.append('{}，距离保底{}发---------------'.format(prize2, julibaodi))
                                        chouzhongprize2 += 1
                                        if not wuqi1:
                                            if dingguiobject == 'sifeng':
                                                dinggui = 0
                                                dingguiobject = 'wuqi'
                                            else:
                                                dinggui += 1
                                    oo = 0
                                else:
                                    if wuqi1:
                                        g = random.randint(2, 3)
                                    else:
                                        g = random.randint(0, 3)
                                    if g <= 2:
                                        oo += 1
                                        if not wuqi1:
                                            dinggui += 1
                                        f = random.randint(0, 30)
                                        p += 1
                                        if f <= 4:
                                            if wuqi1:
                                                listing.append('迪卢克，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之刃，距离保底{}发---------------'.format(julibaodi))
                                            b1 += 1
                                        elif f <= 9:
                                            if wuqi1:
                                                listing.append('刻晴，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之琴，距离保底{}发---------------'.format(julibaodi))
                                            b2 += 1
                                        elif f <= 15:
                                            if wuqi1:
                                                listing.append('七七，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之傲，距离保底{}发---------------'.format(julibaodi))
                                            b3 += 1
                                        elif f <= 21:
                                            if wuqi1:
                                                listing.append('莫娜，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之卷，距离保底{}发---------------'.format(julibaodi))
                                            b4 += 1
                                        elif f <= 24:
                                            if wuqi1:
                                                listing.append('提纳里，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之刃，距离保底{}发---------------'.format(julibaodi))
                                            b5 += 1
                                        else:
                                            if wuqi1:
                                                listing.append('琴，距离保底{}发---------------'.format(julibaodi))
                                            else:
                                                listing.append('天空之脊，距离保底{}发---------------'.format(julibaodi))
                                            b6 += 1
                                    else:
                                        wuxingpanding = random.randint(1, 2)
                                        if wuxingpanding == 1:
                                            listing.append('{}，距离保底{}发---------------'.format(prize1, julibaodi))
                                            chouzhongprize1 += 1
                                            if not wuqi1:
                                                if dingguiobject == 'canggu':
                                                    dinggui = 0
                                                    dingguiobject = 'wuqi'
                                                else:
                                                    dinggui += 1
                                        else:
                                            listing.append('{}，距离保底{}发---------------'.format(prize2, julibaodi))
                                            chouzhongprize2 += 1
                                            if not wuqi1:
                                                if dingguiobject == 'sifeng':
                                                    dinggui = 0
                                                    dingguiobject = 'wuqi'
                                                else:
                                                    dinggui += 1
                                        oo = 0
                                c = 0
                            else:
                                c += 1
                                if u < 7:
                                    sixing = 17
                                elif u == 7:
                                    sixing = 8
                                elif u == 8:
                                    sixing = 4
                                elif u == 9:
                                    sixing = 1
                                    four_start_low += 1
                                v = random.randint(1, sixing)
                                if v == 1:
                                    xinghui += 2
                                    linshixinghui += 2
                                    kq2 = 1
                                    po += 1
                                    if sixingfangwai >= 1:
                                        sixingfangwai = 0
                                        k = random.randint(0, 48)
                                        if k <= 9:
                                            listing.append('{}，距离保底{}发'.format(pr1, 9 - u))
                                            c1 += 1
                                        elif k <= 18:
                                            listing.append('{}，距离保底{}发'.format(pr2, 9 - u))
                                            c2 += 1
                                        elif k <= 30:
                                            listing.append('{}，距离保底{}发'.format(pr3, 9 - u))
                                            c3 += 1
                                        elif k <= 39:
                                            listing.append('{}，距离保底{}发'.format(pr4, 9 - u))
                                            c4 += 1
                                        else:
                                            listing.append('{}，距离保底{}发'.format(pr5, 9 - u))
                                            c5 += 1
                                    else:
                                        kk = random.randint(1, 2)
                                        if kk <= 1:
                                            sixingfangwai = 0
                                            k = random.randint(0, 48)
                                            if k <= 9:
                                                listing.append('{}，距离保底{}发'.format(pr1, 9 - u))
                                                c1 += 1
                                            elif k <= 18:
                                                listing.append('{}，距离保底{}发'.format(pr2, 9 - u))
                                                c2 += 1
                                            elif k <= 30:
                                                listing.append('{}，距离保底{}发'.format(pr3, 9 - u))
                                                c3 += 1
                                            elif k <= 39:
                                                listing.append('{}，距离保底{}发'.format(pr4, 9 - u))
                                                c4 += 1
                                            else:
                                                listing.append('{}，距离保底{}发'.format(pr5, 9 - u))
                                                c5 += 1
                                        else:
                                            sixingfangwai += 1
                                            mm = random.randint(0, 13)
                                            if mm <= 6:
                                                m = random.randint(1, 9)
                                                if m == 1:
                                                    listing.append('祭礼剑，距离保底{}发'.format(9 - u))
                                                    m1 += 1
                                                elif m == 2:
                                                    listing.append('祭礼残章，距离保底{}发'.format(9 - u))
                                                    m2 += 1
                                                elif m == 3:
                                                    listing.append('祭礼弓，距离保底{}发'.format(9 - u))
                                                    m3 += 1
                                                elif m == 4:
                                                    listing.append('祭礼大剑，距离保底{}发'.format(9 - u))
                                                    m4 += 1
                                                elif m == 5:
                                                    listing.append('西风剑，距离保底{}发'.format(9 - u))
                                                    m5 += 1
                                                elif m == 6:
                                                    listing.append('西风秘典，距离保底{}发'.format(9 - u))
                                                    m6 += 1
                                                elif m == 7:
                                                    listing.append('西风猎弓，距离保底{}发'.format(9 - u))
                                                    m7 += 1
                                                elif m == 8:
                                                    listing.append('西风大剑，距离保底{}发'.format(9 - u))
                                                    m8 += 1
                                                else:
                                                    listing.append('西风长枪，距离保底{}发'.format(9 - u))
                                                    m9 += 1
                                            elif mm <= 10:
                                                m = random.randint(0, 72)
                                                if m <= 5:
                                                    listing.append('暗巷闪光，距离保底{}发'.format(9 - u))
                                                    m10 += 1
                                                elif m <= 10:
                                                    listing.append('暗巷猎手，距离保底{}发'.format(9 - u))
                                                    m11 += 1
                                                elif m <= 15:
                                                    listing.append('暗巷的酒与诗，距离保底{}发'.format(9 - u))
                                                    m12 += 1
                                                elif m <= 20:
                                                    listing.append('笛剑，距离保底{}发'.format(9 - u))
                                                    m13 += 1
                                                elif m <= 23:
                                                    listing.append('辰砂之纺锤，距离保底{}发'.format(9 - u))
                                                    m14 += 1
                                                elif m <= 28:
                                                    listing.append('匣里龙吟，距离保底{}发'.format(9 - u))
                                                    m15 += 1
                                                elif m <= 33:
                                                    listing.append('匣里灭辰，距离保底{}发'.format(9 - u))
                                                    m16 += 1
                                                elif m <= 38:
                                                    listing.append('绝弦，距离保底{}发'.format(9 - u))
                                                    m17 += 1
                                                elif m <= 43:
                                                    listing.append('弓藏，距离保底{}发'.format(9 - u))
                                                    m18 += 1
                                                elif m <= 46:
                                                    listing.append('恶王丸，距离保底{}发'.format(9 - u))
                                                    m19 += 1
                                                elif m <= 49:
                                                    listing.append('幽夜华尔兹，距离保底{}发'.format(9 - u))
                                                    m20 += 1
                                                elif m <= 54:
                                                    listing.append('雨裁，距离保底{}发'.format(9 - u))
                                                    m21 += 1
                                                elif m <= 58:
                                                    listing.append('千岩古剑，距离保底{}发'.format(9 - u))
                                                    m22 += 1
                                                elif m <= 62:
                                                    listing.append('千岩长枪，距离保底{}发'.format(9 - u))
                                                    m23 += 1
                                                elif m <= 66:
                                                    listing.append('昭心，距离保底{}发'.format(9 - u))
                                                    m24 += 1
                                                elif m <= 72:
                                                    listing.append('流浪乐章，距离保底{}发'.format(9 - u))
                                                    m25 += 1
                                            else:
                                                m = random.randint(0, 66)
                                                if m <= 5:
                                                    listing.append('芭芭拉，距离保底{}发'.format(9 - u))
                                                    m26 += 1
                                                elif m <= 10:
                                                    listing.append('行秋，距离保底{}发'.format(9 - u))
                                                    m27 += 1
                                                elif m <= 15:
                                                    listing.append('菲谢尔，距离保底{}发'.format(9 - u))
                                                    m28 += 1
                                                elif m <= 19:
                                                    listing.append('云堇，距离保底{}发'.format(9 - u))
                                                    m29 += 1
                                                elif m <= 24:
                                                    listing.append('凝光，距离保底{}发'.format(9 - u))
                                                    m30 += 1
                                                elif m <= 28:
                                                    listing.append('罗莎莉亚，距离保底{}发'.format(9 - u))
                                                    m31 += 1
                                                elif m <= 33:
                                                    listing.append('雷泽，距离保底{}发'.format(9 - u))
                                                    m32 += 1
                                                elif m <= 38:
                                                    listing.append('重云，距离保底{}发'.format(9 - u))
                                                    m33 += 1
                                                elif m <= 42:
                                                    listing.append('早柚，距离保底{}发'.format(9 - u))
                                                    m34 += 1
                                                elif m <= 46:
                                                    listing.append('砂糖，距离保底{}发'.format(9 - u))
                                                    m35 += 1
                                                elif m <= 51:
                                                    listing.append('班尼特，距离保底{}发'.format(9 - u))
                                                    m36 += 1
                                                elif m <= 56:
                                                    listing.append('烟绯，距离保底{}发'.format(9 - u))
                                                    m37 += 1
                                                elif m <= 61:
                                                    listing.append('香菱，距离保底{}发'.format(9 - u))
                                                    m38 += 1
                                                else:
                                                    listing.append('托马，距离保底{}发'.format(9 - u))
                                                    m39 += 1
                                    u = 0
                                else:
                                    xingchen += 15
                                    linshixingchen += 15
                                    u += 1
                                    hh = random.randint(1, 10)
                                    if hh == 1:
                                        listing.append('飞天御剑')
                                        d1 += 1
                                    elif hh == 2:
                                        listing.append('飞天大御剑')
                                        d2 += 1
                                    elif hh == 3:
                                        listing.append('神射手之誓')
                                        d3 += 1
                                    elif hh == 4:
                                        listing.append('黑缨枪')
                                        d4 += 1
                                    elif hh == 5:
                                        listing.append('以理服人')
                                        d5 += 1
                                    elif hh == 6:
                                        listing.append('冷刃')
                                        d6 += 1
                                    elif hh == 7:
                                        listing.append('黎明神剑')
                                        d7 += 1
                                    elif hh == 8:
                                        listing.append('讨龙英杰谭')
                                        d8 += 1
                                    elif hh == 9:
                                        listing.append('魔导绪论')
                                        d9 += 1
                                    else:
                                        listing.append('沐浴龙血的剑')
                                        d10 += 1
                    iyu = False
                    if movie_play:
                        movie_play = False
                        if kq1 != 0:
                            if fff:
                                fff = False
                                zipping.preview(clip1, eventa=aff)
                            if gg:
                                gg = False
                                iyu = True
                                zipping.preview(clip2, eventa=aff)
                        else:
                            if kq2 != 0:
                                if fff:
                                    zipping.preview(clip3, eventa=aff)
                                if gg:
                                    zipping.preview(clip4, eventa=aff)
                            else:
                                zipping.preview(clip5, eventa=aff)
                    number_blouse = 0
                    flags = True
                    screen.fill((0, 0, 0))
                    if gg:
                        gg = False
                        screen.fill((0, 0, 0))
                        for i in listing:
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
                            fonting2 = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                            lkjd = str(i)
                            msgboxx13 = ('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen, linshixinghui))
                            font1 = fonting.render(lkjd, True, green)
                            font13 = fonting2.render(msgboxx13, True, (255, 255, 0))
                            screen.blit(font1, (30, 30))
                            screen.blit(font13, (300, 550))
                            pygame.display.flip()
                    if oiu:
                        screen.fill((0, 0, 0))
                        fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
                        font1 = fonting.render('Loading...', True, (255, 0, 0))
                        screen.blit(font1, (350, 250))
                        pygame.display.flip()
                    if fff:
                        number_blouse = 0
                        fff = False
                        screen.fill((0, 0, 0))
                        for i in listing:
                            fonting = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                            lkjd = str(i)
                            msgboxx13 = ('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen, linshixinghui))
                            font1 = fonting.render(lkjd, True, green)
                            font13 = fonting.render(msgboxx13, True, (255, 255, 0))
                            screen.blit(font1, (20, 20 + 50 * number_blouse))
                            screen.blit(font13, (300, 550))
                            pygame.display.flip()
                            number_blouse += 1
                    if not oiu:
                        while flags:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit(0)
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    flags = False
                    for i in listing:  # -----------------------------------------------------------------------------
                        print(i)
                    if kq1 != 0 and not oiu:
                        flags = True
                        if iyu:
                            for i in listing:
                                fonting = pygame.font.Font('hk4e_zh-cn.ttf', 100)
                                fonting2 = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                                lkjd = str(i)
                                msgboxx13 = ('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen, linshixinghui))
                                font1 = fonting.render(lkjd, True, green)
                                font13 = fonting2.render(msgboxx13, True, (255, 255, 0))
                                screen.blit(font1, (30, 30))
                                screen.blit(font13, (300, 550))
                                pygame.display.flip()
                        else:
                            number_blouse = 0
                            for i in listing:
                                fonting = pygame.font.Font('hk4e_zh-cn.ttf', 50)
                                lkjd = str(i)
                                msgboxx13 = ('获得无主的星尘x{},无主的星辉x{}'.format(linshixingchen, linshixinghui))
                                font1 = fonting.render(lkjd, True, green)
                                font13 = fonting.render(msgboxx13, True, (255, 255, 0))
                                screen.blit(font1, (20, 20 + 50 * number_blouse))
                                screen.blit(font13, (300, 550))
                                pygame.display.flip()
                                number_blouse += 1
                        while flags:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit(0)
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    flags = False
                    iyu = False
                    listing = []
                    kq1 = 0
                    kq2 = 0
                    linshixingchen = 0
                    linshixinghui = 0
                    screen.blit(tupian, (0, 0))
                    if not oiu:
                        screen.blit(musicing2, (1140, 60))
                        musicplay = True
                    pygame.display.flip()
                    number_blouse = 0
                    if not wuqi1:
                        if dingguiobject != 'wuqi':
                            if dinggui == 0:
                                tupian = pygame.image.load("gui0.jpg")
                            elif dinggui == 1:
                                tupian = pygame.image.load("gui1.jpg")
                            elif dinggui == 2:
                                tupian = pygame.image.load("gui2.jpg")
                        else:
                            tupian = pygame.image.load("gui.jpg")
                    tupian = pygame.transform.scale(tupian, (1200, 600))
                    screen.blit(tupian, (0, 0))
                    pygame.display.flip()
                    if oiu:
                        oiu = False
                        while cc:
                            msgbox('请前往shell界面查看抽奖结果  点击“历史记录”查看更多结果')
                            cc = False
                    print('\n' * 2)
            elif 0 < mouse_x < 60 and 0 < mouse_y < 60:
                local_menu = True
                font_oh = pygame.font.Font('hk4e_zh-cn.ttf', 21)
                font_name = pygame.font.Font('hk4e_zh-cn.ttf', 13)
                name_oh = font_oh.render(name, True, (255, 255, 255))
                if len(name_second) > 19:
                    number_fuck = 0
                    name_list_one = []
                    for i in name_second:
                        number_fuck += 1
                        if number_fuck < 15:
                            name_list_one.append(i)
                    name_list_one.append('...')
                    name_third = ''.join(name_list_one)
                else:
                    name_third = name_second
                name_name = font_name.render(name_third, True, (255, 255, 255))
                for i in range(20):
                    screen.blit(local_image_one, (-380 + 20 * i, 0))
                    screen.blit(name_oh, (-210 + 20 * i, 23))
                    screen.blit(name_name, (-210 + 20 * i, 52))
                    pygame.display.flip()
                while local_menu:
                    name_oh = font_oh.render(name, True, (255, 255, 255))
                    if len(name_second) > 18:
                        number_fuck = 0
                        name_list_one = []
                        for i in name_second:
                            number_fuck += 1
                            if number_fuck < 15:
                                name_list_one.append(i)
                        name_list_one.append('...')
                        name_third = ''.join(name_list_one)
                    else:
                        name_third = name_second
                    name_name = font_name.render(name_third, True, (255, 255, 255))
                    screen.blit(local_image_one, (0, 0))
                    screen.blit(name_oh, (170, 23))
                    screen.blit(name_name, (170, 52))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if (426 < mouse_x < 1200 and 0 < mouse_y < 600) or (0 < mouse_x < 50 and 0 < mouse_y < 50):
                                local_menu = False
                                for i in range(5):
                                    screen.blit(local_image_main, (0, 0))
                                    screen.blit(local_image_one, (0 - 80 * i, 0))
                                    pygame.display.flip()
                            elif 380 < mouse_x < 420 and 15 < mouse_y < 60:  # 重命名
                                msg = '重命名'
                                field = ['用户名', '签名']
                                input_value = multenterbox(msg=msg, fields=field, values=[name, name_second])
                                if input_value is None:
                                    pass
                                else:
                                    if input_value[0].strip() == '':
                                        msgbox('姓名不能为空')
                                    elif len(input_value[0].strip()) > 6:
                                        msgbox('姓名长度不能超过六个字符')
                                    else:
                                        name = input_value[0].strip()
                                        ff = open(r'C:\name.txt', 'w')
                                        ff.write(name)
                                        ff.close()
                                    if input_value[0].strip() == '':
                                        msgbox('签名不能为空')
                                    elif len(input_value[1].strip()) > 30:
                                        msgbox('签名长度不能超过三十个字符')
                                    else:
                                        name_second = input_value[1].strip()
                                        ff = open(r'C:\name2.txt', 'w')
                                        ff.write(name_second)
                                        ff.close()
                            elif 60 < mouse_x < 150 and 185 < mouse_y < 270:  # 商城
                                pass
                            elif 60 < mouse_x < 150 and 270 < mouse_y < 350:  # 图鉴
                                pass
                            elif 150 < mouse_x < 240 and 185 < mouse_y < 270:  # 队伍配置
                                pass
                            elif 150 < mouse_x < 240 and 270 < mouse_y < 350:  # 角色图鉴
                                pass
                            elif 240 < mouse_x < 325 and 185 < mouse_y < 270:  # 指南
                                textbox(msg='从入门到入土         现代丘丘语辞典', text='''

Aba [名] 食物；东西。
Adam [动] 生气。

Beru [动] 帮助。   [例句] Yo mimi beru si?
Biadam [副] 生气地。
Biat [动] 草。几乎只见于粗口话。
Biat ye [短] Fuck you。此短语堪称经典，是丘丘语中最有代表性的粗口话。
Biodomu [副] 客气地；恭恭敬敬地。与词组ya odomu相对。   [例句] Mani nini Biodomu!
Buka [名] 肚子。   [例句] Todo yo, buka guruguru nye.

Celi [副] 一天；整天。   [名] 天气。   [名] 火；火元素。

Dada [官方][副] 最强。   [动] 表示感谢。   [助] 奥力给！（表确信或语势增强）
Dala [名] 谁；某人。
Dala si [短] 什么人？
Domu [动] 躺下；躺着。

Eleka [动] 让；使；令。

Guru-guru [名][本义] 肚子饿时发出的咕噜咕噜声。   [形][引申] 肚子饿。
Gusha [官方][名][本义] 草、谷物、蔬菜等可食用植物。   [官方][形][引申] 倒霉。

Ika [名] 这个。

Ka [副] ……吗？用于句末，表示疑问或反问。可能与日语ka的用法相同。   [例句] Yo mosi ka?
Kucha [官方][形] 弱的；较弱的。
Kundala [名] 垫底者；最弱的人。
Kuzi [动] 觉得。

Lata [名][本义] 冰；冰元素。   [动][引申] 下雪。
Lata movo [名][动] 水；流动的冰。
Lawa [名] 大哥；强者。（表示尊敬）

Mi [名] 我。
Mani [动] 给；向……献上。   [例句] Muhe vin plata? Mani ye! Mani dada!
Mimi [名] 我们。Mi的简单复数形式。
Mita [官方][名][本义] 肉。   [官方][形][引申] 愉悦；心情好。
Mosi [官方][动] 吃。
Mosi gusha [官方][短][本义] 吃植物。   [官方][短][引申] 真倒霉；不开心。
Mosi mita [官方][短][本义] 吃肉。   [官方][短][引申] 幸运；愉快。
Movo [动][本义] 打架。   [动][引申] 跳舞。   [动] 流动。   [名] 风；风元素。
Muhe [动] 想要。
Muhe ye [短] 想要你。表示希望与对方产生互动，这种互动可以是积极的（如一起吃肉），也可以是消极的（如相约打架）。

Nini [名] 贡品。   [名] 雷；雷元素。
Nunu [官方][动][本义] 睡觉。   [官方][动][引申] 晚安。
Nye [名][形] 那个。

Olah [官方][助] 你好。
Odomu [动] 客气。

Plata [动] 打。
Pupu [名] 屁股。

Sada [动] 唱歌；念诗。   [名] 岩；岩元素。
Shato [名] 晴天。   [动] 天晴。
Si [副] 什么？（特殊疑问词）

Tiga [名] 丘丘；丘丘人。
Tiga mitono [名] 丘丘人战士。
Todo [动] 赠送。
Tomo [动] 聚集。

Unta [动] 决定；裁判；裁决。
Unu [名] 神；元素力量。
Upa [副][本义] 在……上面。   [副][引申] 层层叠加；一个又一个。

Valo [助] 再见。
Vin [动] 防止；阻止；免疫。
Vin plata [名] 防打（人类语言中称为“盾牌”）。

Ya [副] 不；不是。（表否定）   [动] 不要。（表拒绝）   [助] 呀；啊。（表惊叹）
Ya odomu [短] 别客气。
Yaya [动] 尝试。
Yaya ika [短] 尝尝这个！
Ye [名] 你。
Yeye [名] 你们。Ye的简单复数形式。
Yika [名] 坏东西。
Yo [名] 您。Ye的尊称。
Yoyo [名][本义] 酒。   [动][引申] 喝酒。

Zido [形] 好。
                                ''')
                            elif 240 < mouse_x < 325 and 270 < mouse_y < 350:  # 反馈
                                save_as = textbox(msg='请输入你的意见', text='写点什么......')
                                if save_as == '写点什么......' or save_as is None:
                                    pass
                                else:
                                    ff = open(r'C:\意见反馈.txt', 'a')
                                    ff.write(save_as)
                                    ff.write('\n')
                                    ff.write('====================================================')
                                    ff.write('\n')
                                    ff.close()
                                    msgbox('感谢您的反馈')
                            elif 325 < mouse_x < 420 and 185 < mouse_y < 270:  # 成就
                                msgbox('你其实听得见吧')
                            elif 0 < mouse_x < 60 and 250 < mouse_y < 310:  # 公告
                                pass
                            elif 0 < mouse_x < 60 and 310 < mouse_y < 365:  # 邮箱
                                pass
                            elif 0 < mouse_x < 60 and 365 < mouse_y < 490:  # 设置
                                for i in range(10):
                                    image_strong.set_alpha(50 * i)
                                    screen.blit(image_strong, (0, 0))
                                    pygame.display.flip()
                                text_music = '{}'.format(int(10 * music_main_loud))
                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                screen.blit(font_go, (650, 123))
                                text_music = '{}'.format(int(10 * musicloud))
                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                screen.blit(font_go, (650, 173))
                                location10 = 695 + 160 * music_main_loud + 2
                                location20 = 695 + 160 * musicloud + 2
                                screen.blit(image_go1, (location10, 125))
                                screen.blit(image_go1, (location20, 175))
                                flags = True
                                while flags:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit(0)
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_x, mouse_y = pygame.mouse.get_pos()
                                            if 680 < mouse_x < 900 and 120 < mouse_y < 155:
                                                moved = True
                                            elif 680 < mouse_x < 900 and 155 < mouse_y < 205:
                                                moved2 = True
                                            vel_aa, vel_ab = pygame.mouse.get_pos()
                                            if 170 < mouse_x < 900 and 250 < mouse_y < 300:
                                                gift = enterbox('请输入兑换码')
                                                if gift == 'SBqcs':
                                                    msgbox('兑换成功')
                                                elif gift is None:
                                                    pass
                                                else:
                                                    msgbox('无效的兑换码')
                                            elif 1120 < mouse_x < 1200 and 0 < mouse_y < 80:
                                                flags = False
                                                for i in range(10):
                                                    local_image_main.set_alpha(50 * i)
                                                    screen.blit(local_image_main, (0, 0))
                                                    screen.blit(local_image_one, (0, 0))
                                                    pygame.display.flip()
                                                break
                                        if event.type == pygame.MOUSEBUTTONUP:
                                            if moved:
                                                moved = False
                                                location10 = vel_aa
                                                vel_aa = 0
                                                if location10 < 695:
                                                    location10 = 695
                                                if location10 > 870:
                                                    location10 = 870
                                                screen.blit(image_strong, (0, 0))
                                                text_music = '{}'.format(int(10 * music_main_loud))
                                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                                screen.blit(font_go, (650, 123))
                                                text_music = '{}'.format(int(10 * musicloud))
                                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                                screen.blit(font_go, (650, 173))
                                                screen.blit(image_go1, (location10, 125))
                                                screen.blit(image_go1, (location20, 175))
                                            if moved2:
                                                moved2 = False
                                                location20 = vel_aa
                                                vel_aa = 0
                                                if location20 < 695:
                                                    location20 = 695
                                                if location20 > 870:
                                                    location20 = 870
                                                screen.blit(image_strong, (0, 0))
                                                text_music = '{}'.format(int(10 * music_main_loud))
                                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                                screen.blit(font_go, (650, 123))
                                                text_music = '{}'.format(int(10 * musicloud))
                                                font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                                screen.blit(font_go, (650, 173))
                                                screen.blit(image_go1, (location10, 125))
                                                screen.blit(image_go1, (location20, 175))
                                        if moved:
                                            vel_aa, vel_ab = pygame.mouse.get_pos()
                                            location10 = vel_aa
                                            if location10 < 695:
                                                location10 = 695
                                            if location10 > 870:
                                                location10 = 870
                                            if 695 <= location10 < 712:
                                                music_main_loud = 0
                                            elif 712 <= location10 < 727:
                                                music_main_loud = 0.1
                                            elif 727 <= location10 < 743:
                                                music_main_loud = 0.2
                                            elif 743 <= location10 < 759:
                                                music_main_loud = 0.3
                                            elif 759 <= location10 < 775:
                                                music_main_loud = 0.4
                                            elif 775 <= location10 < 791:
                                                music_main_loud = 0.5
                                            elif 791 <= location10 < 807:
                                                music_main_loud = 0.6
                                            elif 807 <= location10 < 819:
                                                music_main_loud = 0.7
                                            elif 819 <= location10 < 835:
                                                music_main_loud = 0.8
                                            elif 835 <= location10 < 855:
                                                music_main_loud = 0.9
                                            else:
                                                music_main_loud = 1
                                            if count_hi <= 400:
                                                count_hi += 1
                                                main_music.set_volume(music_main_loud)
                                                main_music.play()
                                            else:
                                                count_hi = 0
                                                main_music.stop()
                                                for i in range(5):
                                                    main_music2.play()
                                                moved = False
                                            screen.blit(image_strong, (0, 0))
                                            text_music = '{}'.format(int(10 * musicloud))
                                            font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                            screen.blit(font_go, (650, 173))
                                            text_music = '{}'.format(int(10 * music_main_loud))
                                            font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                            screen.blit(font_go, (650, 123))
                                            screen.blit(image_go1, (location10, 125))
                                            screen.blit(image_go1, (location20, 175))
                                        if moved2:
                                            vel_aa, vel_ab = pygame.mouse.get_pos()
                                            location20 = vel_aa
                                            if location20 < 695:
                                                location20 = 695
                                            if location20 > 870:
                                                location20 = 870
                                            if 695 <= location20 < 712:
                                                musicloud = 0
                                            elif 712 <= location20 < 727:
                                                musicloud = 0.1
                                            elif 727 <= location20 < 743:
                                                musicloud = 0.2
                                            elif 743 <= location20 < 759:
                                                musicloud = 0.3
                                            elif 759 <= location20 < 775:
                                                musicloud = 0.4
                                            elif 775 <= location20 < 791:
                                                musicloud = 0.5
                                            elif 791 <= location20 < 807:
                                                musicloud = 0.6
                                            elif 807 <= location20 < 819:
                                                musicloud = 0.7
                                            elif 819 <= location20 < 835:
                                                musicloud = 0.8
                                            elif 835 <= location20 < 855:
                                                musicloud = 0.9
                                            else:
                                                musicloud = 1
                                            pygame.mixer.music.set_volume(musicloud)
                                            screen.blit(image_strong, (0, 0))
                                            text_music = '{}'.format(int(10 * music_main_loud))
                                            font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                            screen.blit(font_go, (650, 123))
                                            text_music = '{}'.format(int(10 * musicloud))
                                            font_go = font_music_loud.render(text_music, True, (0, 0, 0))
                                            screen.blit(font_go, (650, 173))
                                            screen.blit(image_go1, (location10, 125))
                                            screen.blit(image_go1, (location20, 175))
                                        pygame.display.flip()
                            elif 0 < mouse_x < 60 and 520 < mouse_y < 600:
                                pygame.quit()
                                sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 60 < mouse_x < 190 and 0 < mouse_y < 160:
                for i in range(10):
                    image1.set_alpha(50 * i)
                    image2.set_alpha(50 * i)
                    image3.set_alpha(50 * i)
                    image4.set_alpha(50 * i)
                    image5.set_alpha(50 * i)
                    image6.set_alpha(50 * i)
                    image7.set_alpha(50 * i)
                    image8.set_alpha(50 * i)
                    image9.set_alpha(50 * i)
                    image10.set_alpha(50 * i)
                    image11.set_alpha(50 * i)
                    image12.set_alpha(50 * i)
                    screen.blit(image1, (location1, location2))
                    screen.blit(image2, (location1 + 250 * (number + 1), location2))
                    screen.blit(image3, (location1 + 2 * (250 * (number + 1)), location2))
                    screen.blit(image4, (location1 + 3 * (250 * (number + 1)), location2))
                    screen.blit(image5, (location1, location2 + 250 * (number + 1)))
                    screen.blit(image6, (location1 + 250 * (number + 1), location2 + 250 * (number + 1)))
                    screen.blit(image7, (location1 + 2 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image8, (location1 + 3 * (250 * (number + 1)), location2 + 250 * (number + 1)))
                    screen.blit(image9, (location1, location2 + 2 * (250 * (number + 1))))
                    screen.blit(image10, (location1 + 250 * (number + 1), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image11, (location1 + 2 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(image12, (location1 + 3 * (250 * (number + 1)), location2 + 2 * (250 * (number + 1))))
                    screen.blit(button_up, (0, 0))
                    screen.blit(button_down, (0, 50))
                    screen.blit(button_back, (1150, 0))
                    pygame.display.flip()
                hop = True
                move()
                for i in range(10):
                    local_image_main.set_alpha(50 * i)
                    screen.blit(local_image_main, (0, 0))
                    pygame.display.flip()
