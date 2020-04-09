from Constantes import *
import pygame
import random


class Bloco_destrutivel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([42, 44])
        self.image = pygame.image.load('Images/Bloco_destrutivel.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(42, Constantes.window_width - 42, 42)
        self.rect.y = random.randrange(44, Constantes.window_height - 44, 44)
        count = 0
        while count != 3:
            count = 0
            for i in Constantes.list_position:
                if i[0] == self.rect.x and i[1] == self.rect.y:
                    self.rect.x = random.randrange(42, Constantes.window_width - 42, 42)
                    self.rect.y = random.randrange(44, Constantes.window_height - 44, 44)
                else:
                    count += 1
