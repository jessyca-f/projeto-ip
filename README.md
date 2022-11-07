
# Projeto IP: Fobia

Aqui encontra-se o sistema interativo denominado Fobia, um jogo 2D no estilo plataforma, desenvolvido como projeto final da disciplina de introdução à programação da Universidade Federal de Pernambuco. O nome se deve ao conceito elaborado para o jogo: o jogador estaria sempre se movendo a fim de fugir de seu pior medo, ainda que essa fuga possua alguns perigos maiores que o medo imaginário, como as plataformas flutuantes que podem levar à sua queda.


## Instruções

Para execução do código, é necessário que você possua Python e pygame instalados.
- Faça o download do branch main deste repositório e extraia o arquivo .zip.
- Abra a pasta projetoIP no seu editor de escolha.
- Execute o arquivo main.py.

O movimento do jogador é controlado através das setas esquerda e direita. A barra de espaço controla seu pulo.


## Membros da equipe e suas funções

[César de Moura (chcm)](https://github.com/eucesarmoura) - 
implementação do áudio no código

[Jéssyca Ferreira (jfs7)](https://github.com/jessyca-ferreira) - elaboração da matriz de coordenadas e movimentação do personagem principal

[João Lucas Souza (jlss)](https://github.com/jlucassouza) -  organização do código

[Kaylanne Eduarda (kess)](https://github.com/Kaylanneedu) - implementação de sprites e suas animações no código

[Lucas Francisco (lfasm)](https://github.com/lukasales) - colisões horizontais e verticais

[Marcos Antônio (mall)](https://github.com/MarcosLaureano) - criação dos coletáveis e display da contagem de pontuação

[Thays Cipriano (tvcc)](https://github.com/thaysz27) -  implementação das telas de 'vitória' e 'game over'

## Organização do código

![Hierarquia de pastas](https://i.imgur.com/amS0ZUW.jpeg)

*main.py* - contém o que pode ser chamado de estrutura geral do sistema interativo, como a função main, responsável por controlar o loop principal do jogo e instanciar as suas diferentes classes. Também armazena constantes como largura e altura da tela.

*assets* - contém todas as imagens utilizadas no código, separadas em diferentes pastas.

*interface* - abriga a pasta nivel, que, por sua vez, contém layout.py. O arquivo layout.py abriga a matriz de coordenadas do jogo, responsável pelas coordenadas das plataformas e dos coletáveis desenhados na tela. Armazena também duas classes: Nivel e Coletaveis. 

A classe Nivel foi utilizada para organizar as funções que cuidam da câmera do jogo e as funções responsáveis pela adição das plataformas na tela, enquanto a classe Coletaveis é responsável pela adição dos três diferentes tipos de coletáveis.

*personagem* - o arquivo jogador.py contém a classe Jogador, que possui funções responsáveis por controlar o movimento do jogador, sua câmera, colisões (com as plataformas e também com os coletáveis), bem como a função de update e draw.

## Bibliotecas

Escolheu-se utilizar a biblioteca pygame na criação do jogo. Inicialmente, foi considerado também o uso da biblioteca pyglet, utilizada, assim como pygame, no desenvolvimento de jogos. Os fatores que levaram a equipe à escolha do pygame foi a sua maior quantidade de usuários – o que tornou erros mais fáceis de serem corrigidos, já que outras pessoas já haviam passado pela mesma experiência – e documentação mais completa e voltada para iniciantes.

## Conceitos utilizados
  
Foram utilizados desde os conceitos ensinados no início da disciplina, como a noção de listas e estruturas de repetição, até as partes mais avançadas, como noções iniciais de POO.

A ideia de matrizes, por exemplo, foi essencial na construção do jogo, já que os sprites são adicionados à tela através de uma matriz que representa suas coordenadas. Diferentes tipos de sprites (como plataformas ou um coletável azul) são desenhados na tela dependendo de qual valor se encontra na matriz naquela posição. Esses valores são lidos através de uma estrutura de repetição, o *for*.

Outra noção de extrema importância para o projeto foi a introdução a classes e objetos. Além do fato de que toda a estrutura do código tem como base a divisão por classes e suas funções, poder gerenciar cada objeto de maneira independente tornou o processo de escrita do código mais fácil e melhorou sua legibilidade de forma significante.
  
## Desafios, erros e aprendizados
  
Os problemas iniciais surgiram com a dificuldade de compreensão, tanto de programação orientada a objetos, quanto ao funcionamento e uso do pygame, e também em relação ao uso do git e github. Esses problemas foram resolvidos com o estudo e experiência que se adquiriu ao longo do processo de desenvolvimento do jogo.

Quanto a desafios, podem ser citados a dificuldade de escrever um código em conjunto pela primeira vez e o processo de adaptação ao estilo de escrita de um grande grupo de diferentes pessoas. Uma melhor comunicação, tanto dentro do código, em forma de comentários, quanto fora dele, permitiu que esse desafio fosse superado.

Um dos maiores erros cometidos ao desenvolver esse projeto foi subestimar a importância da organização do código. Houve um momento em que diversas funções, referentes a diferentes classes, foram condensadas em uma só, algo que dificultou a identificação de erros (e suas eventuais correções) e que poderia ter sido evitado se tivessemos focado em manter o código limpo desde o início.

Foi a primeira vez de grande parte da equipe desenvolvendo algo em conjunto e, assim, todas as partes que estão envolvidas nas etapas de escrever um código com outras pessoas serviram de aprendizado. Em especial, destacam-se o novo entendimento adquirido quanto a necessidade de separar um código em diferentes pastas e de comentar um código, ambos essenciais no processo de desenvolvimento desse projeto. Também foram adquiridos conhecimentos iniciais em relação a programação orientada a objetos e github.

![Screenshot 1](https://i.imgur.com/VC2Pu2u.png)
![Screenshot 2](https://i.imgur.com/8juhOBP.png)
