import pygame

class Jogador():
    def __init__(self, nivel, rolagem):
        self.jogador_sprite = pygame.image.load('assets/personagens/jogador.png')
        self.jogador_sprite = pygame.transform.scale(self.jogador_sprite, (80, 80))
        self.jogador_rect = self.jogador_sprite.get_rect()
        self.direcao = pygame.math.Vector2()
        self.velocidade = 10
        self.gravidade = 0.7
        self.rolagem = rolagem
        self.posicoes_validas = nivel.posicoes_validas
        self.coletaveis_azuis = nivel.coletaveis_azuis
        self.coletaveis_verdes = nivel.coletaveis_verdes
        self.coletaveis_rosas = nivel.coletaveis_rosas
        self.no_ar = True


    def entrada_movimento(self):
        tela = pygame.display.get_surface() # permite se referir a tela sem tomar nenhum parâmetro
        velocidade_pulo = 16
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
        coletavel_azul = pygame.image.load('assets/coletaveis/azul.png')
        coletavel_verde = pygame.image.load('assets/coletaveis/verde.png')
        coletavel_rosa = pygame.image.load('assets/coletaveis/rosa.png')

        novo_coletavel_azul = pygame.transform.scale(coletavel_azul, (80, 80))
        novo_coletavel_verde = pygame.transform.scale(coletavel_verde, (80, 80))
        novo_coletavel_rosa =  pygame.transform.scale(coletavel_rosa, (80, 80))

        tela = pygame.display.get_surface()

        if self.coletaveis_azuis == []:
            tela.blit(novo_coletavel_azul, (1120,0))
        
        if self.coletaveis_verdes == []:
            tela.blit(novo_coletavel_verde, (1040,0))
        
        if self.coletaveis_rosas == []:
            tela.blit(novo_coletavel_rosa, (960,0))

        for sprite in self.coletaveis_azuis:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_azuis = []

        
        for sprite in self.coletaveis_verdes:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_verdes = []

        
        for sprite in self.coletaveis_rosas:
            objeto = sprite[1]
            if objeto.colliderect(self.jogador_rect):
                self.coletaveis_rosas = []

    def desenhar_jogador(self):
        tela = pygame.display.get_surface()
        tela.blit(self.jogador_sprite, self.jogador_pos)

    def atualizar_jogador(self):
        self.cam_jogador()
        self.entrada_movimento()
        self.jogador_rect.x += self.direcao.x * self.velocidade
        self.jogador_rect.y += self.direcao.y
        self.colisoes_horizontais()
        self.add_gravidade()
        self.colisoes_verticais()
        self.colisoes_coletaveis()
