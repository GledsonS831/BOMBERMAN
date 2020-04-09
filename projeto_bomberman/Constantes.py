import pygame


class Constantes:
    blackground = pygame.image.load('Images\Tela de fundo.jpg')

    window_width, window_height = 966, 572
    bloco_width, bloco_height = 42, 44
    cor_vermellha = (199, 41, 14)
    cor_branca = (255, 255, 255)
    cor_verde = (67, 237, 18)
    list_position = [[bloco_width, bloco_height], [bloco_width*2, bloco_height], [bloco_width, bloco_height*2]]
    pos_vertical1 = []
    for i in range(0, 572 + 44, 44):
        pos_vertical1.append([0, i])

    pos_vertical2 = []
    for i in range(0, 572 + 44, 44):
        pos_vertical2.append([924, i])

    pos_horizontal1 = []
    for i in range(0, 966 + 42, 42):
        pos_horizontal1.append([i, 0])

    pos_horizontal2 = []
    for i in range(0, 966 + 42, 42):
        pos_horizontal2.append([i, 528])

