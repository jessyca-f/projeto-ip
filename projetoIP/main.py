import pygame
from interface.nivel.layout import Nivel
from personagem.jogador import Jogador

# constantes
TELA_FUNDO = '#18041f'
TELA_LARGURA = 1200
TELA_ALTURA = 700

pygame.init()

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Projeto IP')

clock = pygame.time.Clock() # responsável pela quantidade de frames por segundo

nivel = Nivel()
jogador = Jogador()


# loop do jogo
executando = True
while executando:
    tela.fill(TELA_FUNDO) # inicia a tela
    nivel.plataformas_nivel() # desenha as plataformas
    jogador.entrada_movimento()

    for entrada in pygame.event.get():
        if entrada.type == pygame.QUIT:
            executando = False
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
