from Constantes import *
import pygame


class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Constantes.bloco_width, Constantes.bloco_height])
        self.image = pygame.image.load('Images/Block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
