
# Projeto IP: Fobia

Aqui encontra-se o sistema interativo denominado Fobia, um jogo 2d desenvolvido como projeto final da disciplina de introdução à programação da Universidade Federal de Pernambuco. 


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

**main.py** - contém a estrutura geral do sistema interativo, como a função main, responsável por controlar o loop principal do jogo e instanciar as suas diferentes classes. Também armazena constantes como largura e altura da tela.

**assets** - contém todas as imagens utilizadas no código, separadas em diferentes pastas.

**interface** - abriga a pasta *nivel*, que, por sua vez, contém o arquivo *layout.py*. *layout.py* abriga a matriz de coordenadas do jogo, responsável pelas coordenadas das plataformas e dos coletáveis desenhados na tela. Armazena também duas classes: *Nivel* e *Coletaveis*. 
\
A *classe Nivel* foi utilizada para organizar as funções que cuidam da câmera do jogo e as funções responsáveis pelos desenhos das plataformas na tela, enquanto a *classe Coletaveis* é responsável pelos desenhos dos três diferentes tipos de coletáveis.

**personagem** - o arquivo *jogador.py* contém a *classe Jogador*, que possui funções
que controlam o movimento do jogador, sua câmera, colisões (com as plataformas e também com os coletáveis
), bem como a função de update e draw.
## Bibliotecas
## Conceitos utilizados
## Desafios e erros
  
  Os problemas iniciais surgiram com o a dificuldade de entendimento, tanto da programação orientada a objetos, quanto ao funcionamento e uso do pygame, e também em relação ao uso do git e github problemas que foram resolvidos com um profundo estudo em diversos conceitos que compoem o assunto. Outro problema encontrado em relação ao aúdio, dificuldade na sua implementação e também faze-ló rodar no jogo devido ao seu formato, onde foi preciso encontrar soluções para achar o formato certo o que foi feito com sucesso.
Quanto a desafios, podem ser citados a dificuldade de escrever um código em conjunto pela primeira vez e o processo de adaptação ao estilo de escrita de um grande grupo de diferentes pessoas. Uma melhor comunicação, tanto dentro do código, em forma de comentários, quanto fora dele, permitiu que esse desafio fosse superado. Um dos maiores erros cometidos ao desenvolver esse projeto foi subestimar a importância da organização do código. Houve um momento em que diversas funções, referentes a diferentes classes, foram condensadas em uma só, algo que dificultou a identificação de erros (e suas eventuais correções) e que poderia ter sido evitado se tivessemos focado em manter o código limpo desde o início.
Foi a primeira vez de grande parte da equipe desenvolvendo algo em conjunto e todas as partes que estão envolvidas nas etapas de escrever um código com outras pessoas serviram de aprendizado. Em especial, destacam-se o novo entendimento adquirido quanto a necessidade de separar um código em diferentes pastas e de comentar um código, ambos essenciais no processo de desenvolvimento desse projeto. Também foram adquiridos conhecimentos em relação a programação orientada a objetos, e também como alocar projetos no github.

## Instruções
