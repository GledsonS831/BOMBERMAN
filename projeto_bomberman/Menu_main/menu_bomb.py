# coding=utf-8
"""
EXAMPLE 2
Game menu with 3 difficulty options.

Copyright (C) 2017-2018 Pablo Pizarro @ppizarror

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame
# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *
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
import _thread as thread
import os
from Menu_main import *

ABOUT = ['PROJETO  DA  DICIPLINA  DE  ALGORITOS', 'DESENVOLVIDO  POR:', 'GLEDSON', 'E', 'DAVID']
MODO = ['MOVIMENTO  COM  AS TECLAS:', '-  Cima   Baixo   Direita   Esquerda', 'SOLTAR  BOMBA:', '-  Barra de Espaco ',
        'SAIR DO JOGO:', '-  ESC']
COLOR_BACKGROUND = (128, 0, 128)  # ROXO
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (966, 572)

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
audio = pygame.mixer.Sound('sons/06_Blue Resort.ogg')
imagem = pygame.image.load('star.jpg')

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('BOMBERMAN')
clock = pygame.time.Clock()
dt = 1 / FPS
# Global variables
DIFFICULTY = ['EASY']


# -----------------------------------------------------------------------------

def random_color():
    """
    Return random color.

    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font):
    """
    Main game function

    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    if difficulty == 'EASY':
        audio.stop()


    # Draw random color and text
    bg_color = random_color()
    f_width = f.get_size()[0]
    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)


def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    surface.fill(COLOR_BACKGROUND)


def mainmenu_background():
    """
    Cor de fundo do menu principal, nesta função usuário pode traçar
    imagens, reproduzir sons, etc.
    """
    surface.blit(imagem, (0, 0))
    audio.play()
    audio.set_volume(0.10)


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )

modo_jogo = pygameMenu.TextMenu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.fonts.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size_title=30,
                                font_title=pygameMenu.fonts.FONT_8BIT,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_color_title=COLOR_WHITE,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=PYGAME_MENU_DISABLE_CLOSE,
                                option_shadow=False,
                                text_color=COLOR_BLACK,
                                text_fontsize=20,
                                title='MODO DE JOGO',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )
for m in MODO:
    modo_jogo.add_line(m)
modo_jogo.add_line(PYGAMEMENU_TEXT_NEWLINE)
modo_jogo.add_option('voltar', play_menu)

play_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_option('Modo de jogo', modo_jogo)
play_menu.add_option('voltar', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=mainmenu_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            bgfun=mainmenu_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='BomberMan',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', play_menu)
main_menu.add_option('sobre', about_menu)
main_menu.add_option('sair', PYGAME_MENU_EXIT)
# -----------------------------------------------------------------------------
# Main loop
while True:
    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu.get_title()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()
