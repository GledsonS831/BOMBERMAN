from Constantes import *
import pygame

from classes.Player import *
player = Player()

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([42, 44])
        self.image.fill(Constantes.cor_branca)
        self.rect = self.image.get_rect()
    def coordinate_explosion(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def collision_wall(self, grupo_bombacollide, bomba_left, bomba_right, bomba_up, bomba_down):
        for i in Constantes.pos_vertical1:
            if i[0] == bomba_left.rect.x:
                grupo_bombacollide.remove(bomba_left)

        for i in Constantes.pos_vertical2:
            if i[0] == bomba_right.rect.x and i[1] == bomba_right.rect.y:
                grupo_bombacollide.remove(bomba_right)

        for i in Constantes.pos_horizontal1:
            if i[0] == bomba_up.rect.x and i[1] == bomba_up.rect.y:
                grupo_bombacollide.remove(bomba_up)

        for i in Constantes.pos_horizontal2:
            if i[0] == bomba_down.rect.x and i[1] == bomba_down.rect.y:
                grupo_bombacollide.remove(bomba_down)
