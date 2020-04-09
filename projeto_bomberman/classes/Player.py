from Constantes import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Constantes.bloco_width, Constantes.bloco_height])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load('Images\perso.png')
        self.rect.x = Constantes.bloco_width
        self.rect.y = Constantes.bloco_height
        self.limitacao = True

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.image = pygame.image.load('Images\perso_left.png')
            self.rect.x -= Constantes.bloco_width
        elif keys[pygame.K_RIGHT]:
            self.image = pygame.image.load('Images\perso_right.png')
            self.rect.x += Constantes.bloco_width
        elif keys[pygame.K_DOWN]:
            self.image = pygame.image.load('Images\perso.png')
            self.rect.y += Constantes.bloco_height
        elif keys[pygame.K_UP]:
            self.image = pygame.image.load('Images\perso_up.png')
            self.rect.y -= Constantes.bloco_height

    '''def collision_block(self, keys, gets_hit, gets_hit_destrutivel):
        if gets_hit or gets_hit_destrutivel:
            if keys[pygame.K_LEFT]:
                self.rect.x += Constantes.bloco_width
            elif keys[pygame.K_RIGHT]:
                self.rect.x -= Constantes.bloco_width
            elif keys[pygame.K_UP]:
                self.rect.y += Constantes.bloco_height
            elif keys[pygame.K_DOWN]:
                self.rect.y -= Constantes.bloco_height'''

    '''def collision_block(self, gets_hit, gets_hit_destrutivel, xant, yant):
        if gets_hit or gets_hit_destrutivel:
            print('colidiu', xant, yant)
            self.rect.left, self.rect.top = xant, yant'''

    def update(self, gets_hit, gets_hit_destrutivel, xant, yant):
        print(self.rect.x, self.rect.y)
        if gets_hit or gets_hit_destrutivel:
            self.rect.left, self.rect.top = xant, yant
        if self.limitacao or gets_hit or gets_hit_destrutivel:
            if self.rect.left <= Constantes.bloco_width:
                self.rect.left = Constantes.bloco_width
            if self.rect.right > Constantes.window_width - Constantes.bloco_width:
                self.rect.right = Constantes.window_width - Constantes.bloco_width
            if self.rect.top <= Constantes.bloco_height:
                self.rect.top = Constantes.bloco_height
            if self.rect.bottom >= Constantes.window_height - Constantes.bloco_height:
                self.rect.bottom = Constantes.window_height - Constantes.bloco_height
