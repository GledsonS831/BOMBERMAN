from classes.Bloco import *
from classes.Bloco_destrutivel import *
from classes.Player import *
from classes.Bomb import *
from Constantes import *
from classes.Explosion_Bomb import *
import pygame
import random
import time
import threading
from ret import *
import _thread as thread
import os

pygame.init()
pygame.display.set_caption('BOMBERMAN')
tela = pygame.display.set_mode([Constantes.window_width, Constantes.window_height])

player = Player()
clock = pygame.time.Clock()
bomba = Bomb()
bomba_left = Explosion()
bomba_right = Explosion()
bomba_up = Explosion()
bomba_down = Explosion()
bomba_center = Explosion()

count_start_bomb = True
count_start_bomb_explosion = True
grupo_blocos = pygame.sprite.Group()
grupo_blocos_destrutiveis = pygame.sprite.Group()
grupo_bomba = pygame.sprite.Group()
grupo_bombacollide = pygame.sprite.Group()
group = pygame.sprite.Group()

grupo_bomba.add(bomba)
group.add(player)


def init():
    county = 0
    for y in range(Constantes.bloco_height * 2, Constantes.window_height - (Constantes.bloco_height * 2),
                   Constantes.bloco_height):
        if county % 2 == 0:
            countx = 0
            for x in range(Constantes.bloco_width * 2, Constantes.window_width - (Constantes.bloco_width * 2),
                           Constantes.bloco_width):
                if countx % 2 == 0:
                    bloco = Bloco(x, y)
                    grupo_blocos.add(bloco)
                countx += 1
        county += 1

    for i in range(100):
        bloco_destrutivel = Bloco_destrutivel
        grupo_blocos_destrutiveis.add(bloco_destrutivel())


def active_bomb():
    global count_start_bomb
    global grupo_bomba

    count_start_bomb = False
    time.sleep(3)
    count_start_bomb = True


def expasion():
    global count_start_bomb_explosion
    global bomba_left
    global bomba_right
    global bomba_up
    global bomba_down

    bomba_up.coordinate_explosion(bomba.rect.x, bomba.rect.y - Constantes.bloco_height)
    bomba_left.coordinate_explosion(bomba.rect.x - Constantes.bloco_width, bomba.rect.y)
    bomba_right.coordinate_explosion(bomba.rect.x + Constantes.bloco_width, bomba.rect.y)
    bomba_down.coordinate_explosion(bomba.rect.x, bomba.rect.y + Constantes.bloco_height)
    bomba_center.coordinate_explosion(bomba.rect.x, bomba.rect.y)

    grupo_bombacollide.add(bomba_down)
    grupo_bombacollide.add(bomba_up)
    grupo_bombacollide.add(bomba_left)
    grupo_bombacollide.add(bomba_right)
    grupo_bombacollide.add(bomba_center)

    time.sleep(3)
    count_start_bomb_explosion = False
    time.sleep(1)
    count_start_bomb_explosion = True


def main():
    global count_start_bomb
    stay = True

    while stay:

        keys = pygame.key.get_pressed()
        xant, yant = player.rect.left, player.rect.top
        tela.blit(Constantes.blackground, (0, 0))

        if keys[pygame.K_ESCAPE]:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stay = False
                break

            player.move(keys)
        if keys[pygame.K_b] and count_start_bomb:
            bomba.cordenadas(player.rect.x, player.rect.y)
            bomba.image = pygame.image.load('Images/bomba.png')
            t = threading.Thread(target=active_bomb)
            t.start()

        if not count_start_bomb:
            grupo_bomba.draw(tela)

        if keys[pygame.K_b] and count_start_bomb_explosion:
            bomba.cordenadas(player.rect.x, player.rect.y)
            t2 = threading.Thread(target=expasion)
            t2.start()

        if not count_start_bomb_explosion:
            bomba_center.collision_wall(grupo_bombacollide, bomba_left, bomba_right, bomba_up, bomba_down)
            grupo_bombacollide.draw(tela)

            pygame.sprite.spritecollide(bomba_left, grupo_blocos_destrutiveis, True)
            pygame.sprite.spritecollide(bomba_right, grupo_blocos_destrutiveis, True)
            pygame.sprite.spritecollide(bomba_up, grupo_blocos_destrutiveis, True)
            pygame.sprite.spritecollide(bomba_down, grupo_blocos_destrutiveis, True)
            pygame.sprite.spritecollide(bomba_center, grupo_blocos_destrutiveis, True)

        gets_hit = pygame.sprite.spritecollide(player, grupo_blocos, False)
        gets_hit_destrutivel = pygame.sprite.spritecollide(player, grupo_blocos_destrutiveis, False)
        grupo_blocos_destrutiveis.update()
        grupo_blocos.update()
        group.update(gets_hit, gets_hit_destrutivel, xant, yant)


        grupo_blocos_destrutiveis.draw(tela)
        grupo_blocos.draw(tela)
        group.draw(tela)
        pygame.display.update()



        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    init()
    main()
