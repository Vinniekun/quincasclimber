__author__ = 'vinnie'
import pygame
from pygame import gfxdraw

class Stage_structure:
    def __init__(self):
        self.blocks = [pygame.Rect(i*20, pygame.display.get_surface().get_height()-20 ,20,20) for i in range(40)]


    def vazia(self):
        return len(self.blocks) == 0

    def desenha_blocos(self,tela):
        for bloco in self.blocks:
            pygame.gfxdraw.box(tela, bloco, (0,0,0))

    def desenha_blocos2(self,tela):
        for bloco in self.blocks2:
            pygame.gfxdraw.box(tela, bloco, (0,0,0))

    def remove_bloco(self,n):
        self.blocks.pop(n)