import pygame

class Jogador():
    def __init__(self, nivel, coletavel, rolagem):
        self.jogador_sprite = pygame.image.load('assets/personagens/jogador.png')
        self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (100, 74))
        self.jogador_rect = self.jogador_sprite.get_rect()
        self.direcao = pygame.math.Vector2(0,0)
        self.velocidade = 10
        self.gravidade = 0.9
        self.rolagem = rolagem
        self.posicoes_validas = nivel.posicoes_validas
        self.coletavel = coletavel
        self.no_ar = True


    def entrada_movimento(self):
        tela = pygame.display.get_surface() # permite se referir a tela sem tomar nenhum parâmetro
        velocidade_pulo = 25
        self.pulando = False


        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.direcao.x = 1 # adiciona movimento a direcao +x
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direcao.x = -1 # adiciona movimento a direcao -x
        else:
            self.direcao.x = 0

        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.no_ar:
            self.pulando = True

        if self.pulando:
            self.direcao.y = -velocidade_pulo # adiciona movimento para cima
            self.no_ar = True
            self.pulando = False

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
        tela = pygame.display.get_surface()

        self.coletaveis_azuis = self.coletavel.coletaveis_azuis
        self.coletaveis_verdes = self.coletavel.coletaveis_verdes
        self.coletaveis_rosas = self.coletavel.coletaveis_rosas

        self.coletavel_azul = self.coletavel.coletavel_azul
        self.coletavel_verde = self.coletavel.coletavel_verde
        self.coletavel_rosa = self.coletavel.coletavel_rosa

        for sprite in self.coletaveis_azuis:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_azuis.remove(sprite)
        if self.coletaveis_azuis == []:
            tela.blit(self.coletavel_azul, (1120,0))

        
        for sprite in self.coletaveis_verdes:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_verdes.remove(sprite)
        if self.coletaveis_verdes == []:
            tela.blit(self.coletavel_verde, (1040, 0))
        
        for sprite in self.coletaveis_rosas:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_rosas.remove(sprite)
        if self.coletaveis_rosas == []:
            tela.blit(self.coletavel_rosa, (960, 0))

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
