
# Projeto IP: Fobia

Aqui encontra-se o sistema interativo denominado Fobia, um jogo desenvolvido para a disciplina de introdução a computação da UFPE. 
![Screenshot 1](https://i.imgur.com/b0JV2xC.png)
![Screenshot 2](https://i.imgur.com/8juhOBP.png)






## Membros da equipe e suas funções

[César Henrique <chcm>](https://www.github.com/octokatherine) - 
implementação do áudio no código

[Jéssyca Ferreira <jfs7>](https://github.com/jessyca-ferreira) - base do jogo e movimentação do personagem principal

[João Lucas Souza <jlss>](https://github.com/jessyca-ferreira) - funcionamento do inimigo e condição de 'game-over'

[Kaylanne Eduarda <kess>](https://github.com/jessyca-ferreira) - implementação de sprites e suas animações no código

[Lucas Francisco <lfasm>](https://github.com/jessyca-ferreira) - colisões horizontais e verticais

[Marcos Antônio <mall>](https://github.com/jessyca-ferreira) - coletáveis e contagem da pontuação

[Thays Cipriano <tvcc>](https://github.com/jessyca-ferreira) -  funcionamento do inimigo e condição de 'game-over'


## Organização do código

![Diagrama de hierarquia de pastas](https://i.imgur.com/JDNvex9.png)

**main.py** - contém a estrutura geral do sistema interativo, como a função main, responsável por controlar o loop principal do jogo e instanciar as suas diferentes classes.

**assets** - contém todas as imagens utilizadas no código, separadas em diferentes pastas.

**interface** - abriga a pasta *nivel*, que, por sua vez, contém o arquivo *layout.py*. *layout.py* abriga a matriz de coordenadas do jogo, responsável pelas coordenadas das plataformas e dos coletáveis desenhados na tela. Armazena também duas classes: *Nivel* e *Coletaveis*. 
\
A *classe Nivel* foi utilizada para organizar as funções que cuidam da câmera do jogo e as funções responsáveis pelos desenhos das plataformas na tela, enquanto a *classe Coletaveis* é responsável pelos desenhos do três diferentes tipos de coletáveis.

**personagem** - o arquivo *jogador.py* contém a *classe Jogador*, que possui funções
que controlam o movimento do jogador, sua câmera, colisões (com as plataformas e também com os coletáveis
), bem como a função de update e draw.
## Bibliotecas
## Conceitos utilizados
## Desafios e erros
## Instruções