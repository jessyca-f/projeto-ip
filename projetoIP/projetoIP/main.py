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



rolagem = [0, 0]

nivel = Nivel(rolagem)
jogador = Jogador(nivel, rolagem)
cam_nivel = nivel.cam_rolagem()
cam_jogador = jogador.cam_jogador()


# loop do jogo
executando = True
pause = False
while executando:
    for entrada in pygame.event.get():
        if entrada.type == pygame.QUIT:
            executando = False
            pygame.quit()
            exit()

        if entrada.type == pygame.KEYDOWN:
            if entrada.key == pygame.K_ESCAPE:
                if pause == True:
                    pause = False
                else:
                    pause = True

    if not pause:
        tela.fill(TELA_FUNDO) # inicia a tela
        nivel.plataformas_nivel() # desenha as plataformas
        rolagem[0] += (jogador.jogador_rect.x - rolagem[0] - 600) / 5
        rolagem[1] += (jogador.jogador_rect.y - rolagem[1] - 100) / 5
        jogador.desenhar_jogador()
        jogador.atualizar_jogador()






    pygame.display.update()
    clock.tick(60)
