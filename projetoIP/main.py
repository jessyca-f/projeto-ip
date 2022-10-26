import pygame
from interface.nivel.layout import Nivel
from interface.nivel.layout import Coletavel
from personagem.jogador import Jogador

# constantes
TELA_FUNDO = pygame.image.load('assets/tela fundo/cenario.d.png')  #adicionando a tela de fundo
TELA_LARGURA = 1200
TELA_ALTURA = 700

pygame.init()

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Projeto IP')

clock = pygame.time.Clock()  # responsável pela quantidade de frames por segundo

# loop do jogo
def main():
    rolagem = [0, 0]
    nivel = Nivel(rolagem)
    coletaveis = Coletavel(nivel)
    jogador = Jogador(nivel, coletaveis, rolagem)
    cam_nivel = nivel.cam_rolagem()
    cam_jogador = jogador.cam_jogador()

    executando = True
    pause = False
    game_over = False
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


        if not pause and not game_over:
            tela.blit(TELA_FUNDO, (0, 0))
            nivel.plataformas_nivel()  # desenha as plataformas
            coletaveis.objetos_nivel()
            rolagem[0] += (jogador.jogador_rect.x - rolagem[0] - 640) / 10
            rolagem[1] += (jogador.jogador_rect.y - rolagem[1] - 390) / 10
            jogador.desenhar_jogador()
            jogador.atualizar_jogador()

            if jogador.jogador_rect.top > TELA_ALTURA + 640:
                game_over = True
        elif game_over:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()

        pygame.display.update()
        clock.tick(60)


main()
