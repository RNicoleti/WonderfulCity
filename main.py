import pygame

print('Setup Start')
pygame.init()
screen = pygame.display.set_mode(size=(600, 480)) #Criando a janela
print('Setup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Fechar a janela
            quit()  # Encerrando o Pygame
