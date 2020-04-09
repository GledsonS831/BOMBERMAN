import pygame
from Constantes import *
import random

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Constantes.bloco_width, Constantes.bloco_height])
        self.rect = self.image.get_rect()