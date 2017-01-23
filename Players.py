__author__ = 'vinnie'
import pygame

class Players:

    def __init__(self,gravidade,tela):
        #ATRIBUTOS
        self.grav = gravidade
        self.jump_power = 200
        self.jump = self.jump_power
        self.jump_bool = False

        #POSICOES
        self.pos_cat = [300,tela.get_height()+200]
        self.dir_cat = 'left'
        self.spriteleft = True
        rec_player = 0

        #sadasdasd
        self.sprite_player = pygame.image.load("cat_fall.png").convert_alpha()
        self.fall_player = "cat_fall.png"
        self.rise_player = "cat_rise.png"

    def acao_gravidade(self):
        if not self.jump_bool:
            self.grav *= 1.05
            self.pos_cat[1] += self.grav

    def colisao(self,stage,gravidade,sound_trampolin):
        self.rec_player = self.sprite_player.get_rect()
        self.rec_player.move_ip(self.pos_cat)
        indice = self.rec_player.collidelist(stage.blocks)
        if indice >= 0:
            stage.remove_bloco(indice)
            sound_trampolin.play()
            self.jump_bool = True
            if not self.spriteleft:
                self.sprite_player = pygame.image.load(self.rise_player).convert_alpha()
                self.sprite_player = pygame.transform.flip(self.sprite_player,True,False)
            else:
                self.sprite_player = pygame.image.load(self.rise_player).convert_alpha()
            self.grav = gravidade + (self.grav*0.2)
        if self.jump_bool:
            self.grav /= 1.02
            self.pos_cat[1] -= self.grav
            self.jump -= gravidade
            if self.jump <= 0:
                self.jump_bool = False
                if not self.spriteleft:
                    self.sprite_player = pygame.image.load(self.rise_player).convert_alpha()
                    self.sprite_player = pygame.transform.flip(self.sprite_player,True,False)
                else:
                    self.sprite_player = pygame.image.load(self.rise_player).convert_alpha()
                self.jump = self.jump_power

    def movimentos(self,move_speed,player_sel):
        if player_sel == 1:

            teclas = {"ESQ": pygame.K_a,
                      "DIR": pygame.K_d,
                      "ACAO": pygame.K_w}
        elif player_sel == 2:
            teclas = {"ESQ": pygame.K_LEFT,
                      "DIR": pygame.K_RIGHT,
                      "ACAO": pygame.K_UP}
        elif player_sel == 3:
            teclas = {"ESQ": pygame.K_v,
                      "DIR": pygame.K_b,
                      "ACAO": pygame.K_SPACE}

        if pygame.key.get_pressed()[teclas["ESQ"]]:
            self.pos_cat[0] -= move_speed  #move para esquerda
            if not self.spriteleft:
                self.spriteleft = True
                self.sprite_player = pygame.transform.flip(self.sprite_player,True,False)
                self.dir_cat = 'left'
        elif pygame.key.get_pressed()[teclas["DIR"]]:
            self.pos_cat[0] += move_speed  #move para direta
            if self.spriteleft:
                self.spriteleft = False
                self.sprite_player = pygame.transform.flip(self.sprite_player,True,False)
                self.dir_cat = 'right'
        ##########FAZER A DA ACAO##########

    def out_of_screen(self,tela):
        if self.pos_cat[0] <= 0:
            self.pos_cat[0] = 0
        elif self.pos_cat[0]+self.sprite_player.get_width() >= tela.get_width():
            self.pos_cat[0] = tela.get_width() - self.sprite_player.get_width()

    def cat_over(self,gato):
            return gato.rec_player.colliderect(self.rec_player) and gato.rec_player[1]+20 > self.rec_player[1]

    def gato_sobe(self,gato):
            self.grav = gato.grav
            self.jump = gato.jump
            self.jump_bool = True
            gato.jump_bool = False

