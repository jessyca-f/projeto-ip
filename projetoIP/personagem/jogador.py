import pygame

class Jogador():
    def __init__(self):
        self.jogador_sprite = pygame.image.load('assets/personagens/jogador.png')
        self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (80, 80))
        self.jogador_rect = self.jogador_sprite.get_rect()
        self.direcao = pygame.math.Vector2()
        self.velocidade = 10


    def entrada_movimento(self):
        tela = pygame.display.get_surface() # permite se referir a tela sem tomar nenhum parâmetro

        gravidade = 1
        velocidade_pulo = 20
        self.pulando = False


        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.direcao.x = 1 # adiciona movimento a direcao +x
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direcao.x = -1 # adiciona movimento a direcao -x
        else:
            self.direcao.x = 0 # para o movimento

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.pulando = True

        if self.pulando:
            self.direcao.y = -velocidade_pulo # adiciona movimento para cima

        self.direcao.y += gravidade # equilibra a velocidade do pulo

        self.jogador_rect.x += self.direcao.x * self.velocidade
        self.jogador_rect.y += self.direcao.y

    def desenhar_jogador(self,  jogador_pos):
        tela = pygame.display.get_surface()
        tela.blit(self.jogador_sprite, jogador_pos)