import pygame
from interface.nivel.layout import Nivel
from interface.nivel.layout import Coletavel
from personagem.jogador import Jogador

# constantes
TELA_LARGURA = 1200
TELA_ALTURA = 700

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
TELA_FUNDO = pygame.image.load('assets/tela_fundo/cenario.png').convert() #adicionando a tela de fundo

pygame.init()
pygame.display.set_caption('Fobia')

pygame.mixer.music.set_volume(0.4) # Controle de volume da musica ENTRE 0 E 1
musica_de_fundo = pygame.mixer.music.load('assets/sons/musica_fundo.wav') # Variavel para criar a música do jogo
pygame.mixer.music.play(-1) # Função para que a música toque repetidamente


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
    you_won = False
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

            if jogador.jogador_rect.top > (TELA_ALTURA + rolagem[1] + 390):
                game_over = True

            if jogador.rosas_coletados == 3 and jogador.azuis_coletados == 3 and jogador.verdes_coletados == 3:
                win = pygame.image.load('assets/tela_fundo/win.png').convert()
                tela.blit(win, (0, 0))

                if pygame.key.get_pressed()[pygame.K_SPACE] and you_won:
                    main()
                if pygame.key.get_pressed()[pygame.K_x]:
                    executando = False
                

                you_won = True

        elif game_over:
            lose = pygame.image.load('assets/tela_fundo/game_over.png').convert()
            tela.blit(lose, (0, 0))

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                main()
            if pygame.key.get_pressed()[pygame.K_x]:
                executando = False

        pygame.display.update()
        clock.tick(60)


main()
