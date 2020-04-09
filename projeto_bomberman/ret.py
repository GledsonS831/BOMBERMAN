import pygame
from Constantes import *
class quadrado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Constantes.bloco_width, Constantes.bloco_height])
        self.rect = self.image.get_rect()
        self.image.fill(Constantes.cor_branca)
        self.rect.x = Constantes.bloco_width
        self.rect.y = Constantes.bloco_height

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= Constantes.bloco_width
        elif keys[pygame.K_RIGHT]:

            self.rect.x += Constantes.bloco_width
        elif keys[pygame.K_DOWN]:

            self.rect.y += Constantes.bloco_height
        elif keys[pygame.K_UP]:

            self.rect.y -= Constantes.bloco_height
    def update(self,  gets_hit, gets_hit_destrutivel, xant, yant):
        if gets_hit or gets_hit_destrutivel:
            self.rect.left, self.rect.top = xant, yant