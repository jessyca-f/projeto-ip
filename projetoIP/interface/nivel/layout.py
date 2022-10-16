import pygame

# constantes
TAMANHO_TILE = (30, 30)

class Nivel():
    def __init__(self, jogador, rolagem):
        self.jogador_rect = jogador.jogador_rect
        self.rolagem = rolagem
        self.direcao = jogador.direcao

        # matriz de coordenadas onde 1 representa uma plataforma comum
        layout_nivel = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        plat_comum = pygame.image.load('assets/tiles/plataforma_comum.png')

        self.posicoes_validas = [] # lista que irá conter as coordenadas de todos os 1's


        # adicionando todas as coordenadas validas a lista posicoes_validas
        linha_coord = 0
        for linha in layout_nivel:
            valor_coord = 0
            for valor in linha:
                if valor == 1:
                    plat_comum = pygame.transform.scale(plat_comum, TAMANHO_TILE)
                    plat_comum_rect = plat_comum.get_rect()
                    plat_comum_rect.x = valor_coord * TAMANHO_TILE[0]
                    plat_comum_rect.y = linha_coord * TAMANHO_TILE[1]
                    self.posicoes_validas.append((plat_comum, plat_comum_rect))
                valor_coord += 1
            linha_coord += 1

    # camera
    def cam_rolagem(self, plataforma = pygame.math.Vector2(0, 0)):
        rolagem = self.rolagem
        jogador = self.jogador_rect
        jogador_pos = (jogador.x - rolagem[0], jogador.y - rolagem[1])

        plataforma_pos = (plataforma.x - rolagem[0], plataforma.y - rolagem[1])

        return (jogador_pos, plataforma_pos)


    # funcao responsavel por desenhar na tela as plataformas com base na matriz de coordenadas
    def plataformas_nivel(self):

        tela = pygame.display.get_surface() # permite se referir a tela sem pegar nenhum parâmetro
        for posicao in self.posicoes_validas:
            plataforma_pos = self.cam_rolagem(posicao[1])
            tela.blit(posicao[0], plataforma_pos[1])

    def colisoes_horizontais(self):
        for sprite in self.posicoes_validas:
            plataforma = sprite[1]
            if plataforma.colliderect(self.jogador_rect):
                if self.direcao.x < 0:
                    self.jogador_rect.left = plataforma.right
                if self.direcao.x > 0:
                    self.jogador_rect.right = plataforma.left
