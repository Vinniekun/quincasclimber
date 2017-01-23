import sys
from Stage_structure import Stage_structure
from Players import Players
__author__ = 'vinnie'

import pygame

def main():

    from pygame import gfxdraw
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("Quincas Climber")

    #FONTS
    font1 = pygame.font.Font("fonts/notepaper.ttf",120)
    font2 = pygame.font.Font("fonts/fipps.otf",25)
    font3 = pygame.font.Font("fonts/fipps.otf",20)
    font4 = pygame.font.Font("fonts/hongkong.ttf",150)

    #SOUNDS
    sound_jump = pygame.mixer.Sound("jump.wav")
    sound_dead = pygame.mixer.Sound("dead.wav")
    sound_dead.set_volume(.3)
    sound_select = pygame.mixer.Sound("select.wav")
    sound_trampolin = pygame.mixer.Sound("trampolin.wav")
    pygame.mixer.music.load("intro2.mp3")
    sound_selectyourhero = pygame.mixer.Sound("sound/sfx/selectyourhero.wav")
    sound_ready = pygame.mixer.Sound("sound/sfx/ready.wav")
    sound_fight = pygame.mixer.Sound("sound/sfx/fight.wav")

    #IMAGES
    tela = pygame.display.set_mode((800,600))
    icon = pygame.image.load("icon4.png").convert_alpha()
    logo = pygame.image.load("img/chuhaskell.png").convert_alpha()
    logo = pygame.transform.scale(logo,(800,600))
    background = pygame.image.load("img/wallpaper.jpg").convert_alpha()
    bg_select_char = pygame.image.load("bg_select_char.jpg").convert_alpha()
    char_quincas = pygame.image.load("quincas.png").convert_alpha()
    char_shina = pygame.image.load("shina.png").convert_alpha()
    char_cerveja = pygame.image.load("img/cerveja.png").convert_alpha()
    char_nina = pygame.image.load("img/nina.png").convert_alpha()
    text_quincas = pygame.image.load("img/text_quincas.png").convert_alpha()
    text_shina = pygame.image.load("img/text_shina.png").convert_alpha()
    text_cerveja = pygame.image.load("img/text_cerveja.png").convert_alpha()
    text_nina = pygame.image.load("img/text_nina.png").convert_alpha()
    cursor_sel = pygame.image.load("img/cursor_p1.png").convert_alpha()
    screen_p1 = pygame.image.load("img/white.png").convert_alpha()
    screen_p2 = pygame.image.load("img/white.png").convert_alpha()

    #SPRITES
    #QUINCAS
    sprite_player2 = pygame.image.load("shina_fall.png").convert_alpha()
    sprite_quincasleft = True
    sprite_quincasleft2 = True
    sprite_quincasleft3 = True
    sprite_quincasleft4 = True
    quincas_idle = pygame.image.load("cat_0.png").convert_alpha()
    #SHINA
    sprite_shina = pygame.image.load("shina_fall.png").convert_alpha()
    shina_idle = pygame.image.load("cat_1.png").convert_alpha()
    #CERVEJA
    sprite_cerveja = pygame.image.load("cerveja_fall.png").convert_alpha()
    cerveja_idle = pygame.image.load("cat_2.png").convert_alpha()
    #NINA
    sprite_nina = pygame.image.load("nina_fall.png").convert_alpha()
    nina_idle = pygame.image.load("cat_3.png").convert_alpha()
    #SELECIONADOS
    sprite_p1 = pygame.image.load("cat_fall.png").convert_alpha()
    rise_p1 = "cat_rise.png"
    fall_p1 = "cat_fall.png"
    sprite_p1left = True
    sprite_p2 = pygame.image.load("cat_fall.png").convert_alpha()
    rise_p2 = "cat_rise.png"
    fall_p2 = "cat_fall.png"
    sprite_p2left = True
    sprite_p3 = pygame.image.load("cat_fall.png").convert_alpha()
    rise_p3 = "cat_rise.png"
    fall_p3 = "cat_fall.png"
    sprite_p3left = True
    sprite_p4 = pygame.image.load("cat_fall.png").convert_alpha()
    rise_p4 = "cat_rise.png"
    fall_p4 = "cat_fall.png"
    sprite_p4left = True


    #VARIAVEIS
    gatos = []
    cursor_x = 100
    cursor_y = 530
    player_sel = 2
    player_turn = 1
    move_speed = 10
    gravidade = 8
    somtrue = True

    #POSICOES
    pos_quin = [(tela.get_width()/2-100),100]
    dir_quin = 'left'
    pos_quin2 = [(tela.get_width()/2),100]
    dir_quin2 = 'left'
    pos_quin3 = [(tela.get_width()/2+100),100]
    dir_quin3 = 'left'

    #TEXTOS
    text_selecao = font2.render('Select your cat!',True,(0,0,0))
    #text_jogadores = font2.render(player_sel,True,(0,0,0))
    text9 = font4.render("READY",True,(0,0,0))

    #TELAS
    animation = True
    menu = True
    select_char = True
    game = False
    gameover = False
    text2_off = True
    qtd_player = True

    pygame.display.set_icon(icon) #icone
    stage = Stage_structure()

    #Variaveis de animacao
    x1=10
    y1=0
    size=60
    sprite_teste = pygame.image.load("cat_0.png").convert_alpha()
    sprite_teste = pygame.transform.scale(sprite_teste, (76*size, 60*size))

#################################


#################################

    while(menu):

        stage = []

        #BACKGROUND
        tela.blit(background,(0,0))
        tela.blit(shina_idle,(tela.get_width()/2-80,tela.get_height()/2-25))
        tela.blit(cerveja_idle,(tela.get_width()/2+20,tela.get_height()/2-25))
        if animation == False:
            tela.blit(quincas_idle,(tela.get_width()/2-25,tela.get_height()/2))

        #SAIR DO JOGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("select.mp3")
                pygame.mixer.music.play(-1, 0.0)
                game = True
                menu = False

        #TEXT
        text1 = font1.render('Q u i n c a s   C l i m b e r',True,(0,0,0))
        tela.blit(text1,(90,50))
        if text2_off == False:
            text2 = font2.render('Press space key to start',True,(0,0,0))
            tela.blit(text2,(150,450))
            text2_off = True
        else:
            text2_off = False

        #ANIMATION
        if animation:
            tela.fill((0,0,0))
            tela.blit(logo,(0,0))
            pygame.display.flip()
            pygame.mixer.music.play(0, 0.0)
            pygame.time.delay(1200)
            while(animation):
                if sprite_teste.get_width() >= 150:
                    tela.blit(background,(0,0))
                    tela.blit(shina_idle,(tela.get_width()/2-80,tela.get_height()/2-25))
                    tela.blit(cerveja_idle,(tela.get_width()/2+20,tela.get_height()/2-25))
                    tela.blit(sprite_teste,(0+x1,0+y1))
                    sprite_teste = pygame.transform.rotozoom(sprite_teste, 0, 0.9)
                    x1 += 10
                    y1 += 8
                else:
                    animation = False
                pygame.display.flip()
                pygame.time.Clock().tick(13)


        #FPS
        pygame.display.flip()
        pygame.time.Clock().tick(10)

    while(select_char):

        #ADD gatos
        gatos.append(Players(gravidade,tela))
        gatos.append(Players(gravidade,tela))
        gatos.append(Players(gravidade,tela))
        gatos[2].grav = 0

        tela.fill((255,255,255))
        while(qtd_player):
            tela.fill((255,255,255))
            s = str(player_sel)

            #PRINT TEXTOS
            text6 = font2.render("P1: 'A' e 'D'",True,(0,0,0))
            text7 = font2.render("P2: 'Esquerda' e 'Direita'",True,(0,0,0))
            text8 = font2.render("P3: 'V' e 'B'",True,(0,0,0))
            text5 = font2.render("Como jogar:",True,(0,0,0))
            text4 = font2.render('Quantos jogadores?',True,(0,0,0))
            text_jogadores = font2.render(s,True,(0,0,0))
                #LOCAL DO TEXTO
            tela.blit(text6,(20,50))
            tela.blit(text7,(20,100))
            tela.blit(text8,(20,150))
            tela.blit(text5,(20,5))
            tela.blit(text4,(200,440))
            tela.blit(text_jogadores,(400,500))
            #FPS
            pygame.display.flip()
            pygame.time.Clock().tick(30)

            #KEYBOARD
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    sys.exit()
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    qtd_player = False
                    ############################################################################
                    for i in range (0,player_sel):
                        #gatos.append(Players(gravidade,tela))
                        #Define a posicao de cada gato:
                        gatos[i].pos_cat = [(tela.get_width()/2-200+i*100),100]
                        gatos[i].grav = gravidade
                    break
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if player_sel > 2:
                        player_sel = 2
                    else:
                        player_sel += 1
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    if player_sel < 3:
                        player_sel = 3
                    else:
                        player_sel -=1

        while(player_turn <= player_sel):

            #Som de inicio
            if somtrue:
                sound_selectyourhero.play()
                somtrue = False

            #Personagens selecao
            tela.fill((255,255,255))
            tela.blit(screen_p1,(0,0))
            tela.blit(screen_p2,(200,0))
            tela.blit(text_selecao,(250,410))
            tela.blit(quincas_idle,(60,480))
            tela.blit(shina_idle, (160,480))
            tela.blit(cerveja_idle, (260,480))
            tela.blit(nina_idle, (360,480))

            #Turno de selecao dos personagens
            if player_turn == 1:
                #PLAYER1
                tela.blit(cursor_sel,(cursor_x,cursor_y))
                if cursor_x == 100:
                    gatos[0].sprite_player = pygame.image.load("cat_fall.png").convert_alpha()
                    gatos[0].fall_player = "cat_fall.png"
                    gatos[0].rise_player = "cat_rise.png"
                    screen_p1 = char_quincas
                    tela.blit(screen_p1,(0,0))
                    tela.blit(quincas_idle,(70,300))
                    tela.blit(text_quincas,(100-text_quincas.get_width()//2,365))
                elif cursor_x == 200:
                    gatos[0].sprite_player = pygame.image.load("shina_fall.png").convert_alpha()
                    gatos[0].fall_player = "shina_fall.png"
                    gatos[0].rise_player = "shina_rise.png"
                    screen_p1 = char_shina
                    tela.blit(screen_p1,(0,0))
                    tela.blit(shina_idle,(70,300))
                    tela.blit(text_shina,(100-text_shina.get_width()//2,365))
                elif cursor_x == 300:
                    gatos[0].sprite_player = pygame.image.load("cerveja_fall.png").convert_alpha()
                    gatos[0].fall_player = "cerveja_fall.png"
                    gatos[0].rise_player = "cerveja_rise.png"
                    screen_p1 = char_cerveja
                    tela.blit(screen_p1,(0,0))
                    tela.blit(cerveja_idle,(70,300))
                    tela.blit(text_cerveja,(100-text_cerveja.get_width()//2,365))
                elif cursor_x == 400:
                    gatos[0].sprite_player = pygame.image.load("nina_fall.png").convert_alpha()
                    gatos[0].fall_player = "nina_fall.png"
                    gatos[0].rise_player = "nina_rise.png"
                    screen_p1 = char_nina
                    tela.blit(screen_p1,(0,0))
                    tela.blit(nina_idle,(70,300))
                    tela.blit(text_nina,(100-text_nina.get_width()//2,365))

            if player_turn == 2:
                #PLAYER2
                cursor_sel = pygame.image.load("img/cursor_p2.png").convert_alpha()
                tela.blit(cursor_sel,(cursor_x,cursor_y))
                if cursor_x == 100:
                    gatos[1].sprite_player = pygame.image.load("cat_fall.png").convert_alpha()
                    gatos[1].fall_player = "cat_fall.png"
                    gatos[1].rise_player = "cat_rise.png"
                    screen_p2 = char_quincas
                    tela.blit(screen_p2,(200,0))
                    tela.blit(quincas_idle,(270,300))
                    tela.blit(text_quincas,(300-text_quincas.get_width()//2,365))
                elif cursor_x == 200:
                    gatos[1].sprite_player = pygame.image.load("shina_fall.png").convert_alpha()
                    gatos[1].fall_player = "shina_fall.png"
                    gatos[1].rise_player = "shina_rise.png"
                    screen_p2 = char_shina
                    tela.blit(screen_p2,(200,0))
                    tela.blit(shina_idle,(270,300))
                    tela.blit(text_shina,(300-text_shina.get_width()//2,365))
                elif cursor_x == 300:
                    gatos[1].sprite_player = pygame.image.load("cerveja_fall.png").convert_alpha()
                    gatos[1].fall_player = "cerveja_fall.png"
                    gatos[1].rise_player = "cerveja_rise.png"
                    screen_p2 = char_cerveja
                    tela.blit(screen_p2,(200,0))
                    tela.blit(cerveja_idle,(270,300))
                    tela.blit(text_cerveja,(300-text_cerveja.get_width()//2,365))
                elif cursor_x == 400:
                    gatos[1].sprite_player = pygame.image.load("nina_fall.png").convert_alpha()
                    gatos[1].fall_player = "nina_fall.png"
                    gatos[1].rise_player = "nina_rise.png"
                    screen_p2 = char_nina
                    tela.blit(screen_p2,(200,0))
                    tela.blit(nina_idle,(270,300))
                    tela.blit(text_nina,(300-text_nina.get_width()//2,365))

            if player_turn == 3:
                #PLAYER3
                cursor_sel = pygame.image.load("img/cursor_p3.png").convert_alpha()
                tela.blit(cursor_sel,(cursor_x,cursor_y))
                if cursor_x == 100:
                    gatos[2].sprite_player = pygame.image.load("cat_fall.png").convert_alpha()
                    gatos[2].fall_player = "cat_fall.png"
                    gatos[2].rise_player = "cat_rise.png"
                    screen_p3 = char_quincas
                    tela.blit(screen_p3,(400,0))
                    tela.blit(quincas_idle,(470,300))
                    tela.blit(text_quincas,(500-text_quincas.get_width()//2,365))
                elif cursor_x == 200:
                    gatos[2].sprite_player = pygame.image.load("shina_fall.png").convert_alpha()
                    gatos[2].fall_player = "shina_fall.png"
                    gatos[2].rise_player = "shina_rise.png"
                    screen_p3 = char_shina
                    tela.blit(screen_p3,(400,0))
                    tela.blit(shina_idle,(470,300))
                    tela.blit(text_shina,(500-text_shina.get_width()//2,365))
                elif cursor_x == 300:
                    gatos[2].sprite_player = pygame.image.load("cerveja_fall.png").convert_alpha()
                    gatos[2].fall_player = "cerveja_fall.png"
                    gatos[2].rise_player = "cerveja_rise.png"
                    screen_p3 = char_cerveja
                    tela.blit(screen_p3,(400,0))
                    tela.blit(cerveja_idle,(470,300))
                    tela.blit(text_cerveja,(500-text_cerveja.get_width()//2,365))
                elif cursor_x == 400:
                    gatos[2].sprite_player = pygame.image.load("nina_fall.png").convert_alpha()
                    gatos[2].fall_player = "nina_fall.png"
                    gatos[2].rise_player = "nina_rise.png"
                    screen_p3 = char_nina
                    tela.blit(screen_p3,(400,0))
                    tela.blit(nina_idle,(470,300))
                    tela.blit(text_nina,(500-text_nina.get_width()//2,365))

            #KEYBOARD
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    sys.exit()
                elif pygame.key.get_pressed()[pygame.K_SPACE]:
                    player_turn +=1
                    sound_select.play()
                    pygame.time.delay(300)
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if cursor_x > 301:
                        cursor_x = 100
                    else:
                        cursor_x += 100
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    if cursor_x < 101:
                        cursor_x = 400
                    else:
                        cursor_x -= 100

            #FPS
            pygame.display.flip()
            pygame.time.Clock().tick(30)

        #PRINTS
        text_ready = font1.render("GET READY FOR BATTLE",True,(0,0,0))
        tela.blit(text_ready,(100,150))

        #FPS
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        if player_turn >= player_sel:
            pygame.time.delay(1500)
            pygame.mixer.music.stop()
            pygame.mixer.music.load("battle2.mp3")
            pygame.mixer.music.play(-1, 0.0)
            select_char = False
            game = True
            somtrue = True

    while(game):

        #if stage.vazia():
        if stage == []:
            stage = Stage_structure()

        ####
        tela.blit(text5,(100,300))


        #DESENHA OBJETOS E BACKGROUND
        tela.blit(background,(0,0))
        tela.blit(gatos[0].sprite_player,gatos[0].pos_cat)
        tela.blit(gatos[1].sprite_player,gatos[1].pos_cat)
        tela.blit(gatos[2].sprite_player,gatos[2].pos_cat)
        stage.desenha_blocos(tela)

        stage.desenha_blocos(tela)

        #FPS
        pygame.display.flip()
        pygame.time.Clock().tick(30)

        if somtrue:
            pygame.time.delay(100)
            tela.blit(text9,(150,150))
            sound_ready.play()
            pygame.display.flip()
            pygame.time.delay(1700)
            text10 = font4.render("FIGHT!",True,(0,0,0))
            tela.blit(text10,(150,280))
            sound_fight.play()
            pygame.display.flip()
            pygame.time.delay(600)
            somtrue = False

        #GRAVIDADE
        gatos[0].acao_gravidade()      ######FUNCAO DA CLASSE
        gatos[1].acao_gravidade()
        gatos[2].acao_gravidade()

        #COLISÃO PLAYER 1
        gatos[0].colisao(stage,gravidade,sound_trampolin)

        #COLISÃO PLAYER 2
        gatos[1].colisao(stage,gravidade,sound_trampolin)

        #COLISÃO PLAYER 3
        gatos[2].colisao(stage,gravidade,sound_trampolin)

        #SAIR DO JOGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()

        #MOVIMENTO PLAYER1
        gatos[0].movimentos(move_speed,1)

        #MOVIMENTO PLAYER2
        gatos[1].movimentos(move_speed,2)

        #MOVIMENTO PLAYER3
        gatos[2].movimentos(move_speed,3)

        #TESTE FORA DA TELA PLAYER 1
        gatos[0].out_of_screen(tela)

        #TESTE FORA DA TELA PLAYER 2
        gatos[1].out_of_screen(tela)

        #TESTE FORA DA TELA PLAYER 3
        gatos[2].out_of_screen(tela)

        #COLISÃO GATOS
        for i in range (0,player_sel):
            for j in range (0,player_sel):
                if i!=j and gatos[i].cat_over(gatos[j]):
                    sound_jump.play()
                    gatos[i].gato_sobe(gatos[j])


        #GAMEOVER
        if gatos[0].rec_player[1] > tela.get_height() and gatos[1].rec_player[1] > tela.get_height():
            sound_dead.play()
            win = 3
            gameover = True
            game = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load("victory2.mp3")
            pygame.mixer.music.play(-1,0.0)
        elif gatos[0].rec_player[1] > tela.get_height() and gatos[2].rec_player[1] > tela.get_height():
            sound_dead.play()
            win = 2
            gameover = True
            game = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load("victory2.mp3")
            pygame.mixer.music.play(-1,0.0)
        elif gatos[1].rec_player[1] > tela.get_height() and gatos[2].rec_player[1] > tela.get_height():
            sound_dead.play()
            win = 1
            gameover = True
            game = False
            pygame.mixer.music.stop()
            pygame.mixer.music.load("victory2.mp3")
            pygame.mixer.music.play(-1,0.0)


    while(gameover):
        if win == 1:
            text1 = font1.render('P l a y e r    1   W I N S !',True,(0,0,0))
            tela.blit(text1,(100,50))
        elif win == 2:
            text1 = font1.render('P l a y e r    2   W I N S !',True,(0,0,0))
            tela.blit(text1,(100,50))
        elif win == 3:
            text1 = font1.render('P l a y e r    3   W I N S !',True,(0,0,0))
            tela.blit(text1,(100,50))

        text3 = font2.render('Press space for revenge!',True,(0,0,0))
        tela.blit(text1,(100,50))
        tela.blit(text3,(150,450))

        #SAIR DO JOGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("intro2.mp3")
                pygame.mixer.music.play(-1, 0.0)
                gameover = False
                animation = True
                menu = True
                select_char = True

                main()

        #FPS
        pygame.display.flip()
        pygame.time.Clock().tick(5)

main()
