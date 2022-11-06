import pygame
from interface.nivel.layout import Vilao
from projetoIP.main import 

class Jogador():
    def __init__(self, nivel, coletavel, rolagem):
        self.jogador_sprite = pygame.image.load('assets/personagens/andar1.png')
        self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (48, 60))
        self.jogador_rect = self.jogador_sprite.get_rect()
        self.direcao = pygame.math.Vector2(0,0)
        self.velocidade = 10
        self.gravidade = 0.9
        self.rolagem = rolagem
        self.posicoes_validas = nivel.posicoes_validas
        self.coletavel = coletavel
        self.no_ar = True
        self.azuis_coletados = 0
        self.verdes_coletados = 0
        self.rosas_coletados = 0

        self.esquerda = False
        self.direita = False
        self.contagem = 0


    def entrada_movimento(self):
        tela = pygame.display.get_surface() # permite se referir a tela sem tomar nenhum parâmetro
        velocidade_pulo = 25
        caminho = 'assets/personagens/'
        andar = [pygame.image.load(caminho + 'andar1.png'), pygame.image.load(caminho + 'andar2.png'),
                 pygame.image.load(caminho + 'andar3.png'),
                 pygame.image.load(caminho + 'andar4.png'), pygame.image.load(caminho + 'andar5.png'),
                 pygame.image.load(caminho + 'andar6.png')]
        self.pulando = False


        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.direcao.x = 1 # adiciona movimento a direcao +x
            self.esquerda = False
            self.direita = True
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direcao.x = -1 # adiciona movimento a direcao -x
            self.direita = False
            self.esquerda = True
        else:
            self.direcao.x = 0
            self.esquerda = False
            self.direita = False

        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.no_ar:
            self.pulando = True

        if self.pulando:
            self.direcao.y = -velocidade_pulo # adiciona movimento para cima
            self.no_ar = True
            self.pulando = False

        if self.contagem + 1 >= 18:
            self.contagem = 0

        if self.direita:
            self.jogador_sprite = andar[self.contagem // 3]
            self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (48, 60))
            self.contagem += 1
        elif self.esquerda:
            self.jogador_sprite = andar[self.contagem // 3]
            self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (48, 60))
            self.jogador_sprite = pygame.transform.flip(self.jogador_sprite, True, False)
            self.contagem += 1
        else:
            self.jogador_sprite = pygame.image.load('assets/personagens/andar1.png')
            self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (48, 60))
            self.contagem = 0

    def add_gravidade(self):
        self.direcao.y += self.gravidade  # equilibra a velocidade do pulo
        self.jogador_rect.y += self.direcao.y

    def cam_jogador(self):
        rolagem = self.rolagem
        self.jogador_pos = (self.jogador_rect.x - rolagem[0], self.jogador_rect.y - rolagem[1])
        return self.jogador_pos

    def colisoes_horizontais(self):
        for sprite in self.posicoes_validas:
            plataforma = sprite[1]
            if plataforma.colliderect(self.jogador_rect):
                if self.direcao.x < 0:
                    self.jogador_rect.left = plataforma.right
                if self.direcao.x > 0:
                    self.jogador_rect.right = plataforma.left

    def colisoes_verticais(self):
         for sprite in self.posicoes_validas:
            plataforma = sprite[1]
            if plataforma.colliderect(self.jogador_rect):
                if self.direcao.y > 0:
                    self.jogador_rect.bottom = plataforma.top
                    self.direcao.y = 0
                    self.no_ar = False
                if self.direcao.y < 0:
                    self.jogador_rect.top = plataforma.bottom
                    self.direcao.y = 0
    
    def colisoes_coletaveis(self):
        self.coletaveis_azuis = self.coletavel.coletaveis_azuis
        self.coletaveis_verdes = self.coletavel.coletaveis_verdes
        self.coletaveis_rosas = self.coletavel.coletaveis_rosas

        self.coletavel_azul = self.coletavel.coletavel_azul
        self.coletavel_verde = self.coletavel.coletavel_verde
        self.coletavel_rosa = self.coletavel.coletavel_rosa

        tela = pygame.display.get_surface()
        
        pygame.font.init()

        fonte = pygame.font.get_default_font()
        fonte_geral = pygame.font.SysFont(fonte, 40)

        texto_azuis = fonte_geral.render(f'{self.azuis_coletados}', 1, (255, 255, 255))
        texto_verdes = fonte_geral.render(f'{self.verdes_coletados}', 1, (255, 255, 255))
        texto_rosas = fonte_geral.render(f'{self.rosas_coletados}', 1, (255, 255, 255))

        tela.blit(texto_azuis, (1180,5))
        tela.blit(texto_verdes, (1100,5))
        tela.blit(texto_rosas, (1020,5))

        contador_azul = pygame.transform.scale(self.coletavel_azul, (33, 33))
        contador_verde = pygame.transform.scale(self.coletavel_verde, (33, 33))
        contador_rosa = pygame.transform.scale(self.coletavel_rosa, (33, 33))

        tela.blit(contador_azul, (1140,0))
        tela.blit(contador_verde, (1060,0))
        tela.blit(contador_rosa, (980,0))

        for sprite in self.coletaveis_azuis:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.azuis_coletados += 1
                self.coletaveis_azuis.remove(sprite)

        
        for sprite in self.coletaveis_verdes:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.verdes_coletados += 1
                self.coletaveis_verdes.remove(sprite)

        
        for sprite in self.coletaveis_rosas:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.rosas_coletados += 1
                self.coletaveis_rosas.remove(sprite)
                
    def colisoes_inimigos(self):
        if pygame.sprite.spritecollide(self, Vilao, False):
            game_over = True
        
    def desenhar_jogador(self):
        tela = pygame.display.get_surface()
        tela.blit(self.jogador_sprite, self.jogador_pos)

    def atualizar_jogador(self):
        self.cam_jogador()
        self.entrada_movimento()
        self.jogador_rect.x += self.direcao.x * self.velocidade
        self.colisoes_horizontais()
        self.add_gravidade()
        self.colisoes_verticais()
        self.colisoes_coletaveis()
