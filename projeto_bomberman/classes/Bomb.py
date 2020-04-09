from Constantes import *

import pygame

from classes.Player import *
player = Player()


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([42, 44])
        self.image.fill(Constantes.cor_branca)
        self.rect = self.image.get_rect()

    def cordenadas(self, x, y):

        self.rect.x = x
        self.rect.y = y
