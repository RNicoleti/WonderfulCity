#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # Criando a janela

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #       pygame.quit()  # Fechar a janela
        #      quit()  # Encerrando o Pygame
