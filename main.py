import math
import pygame
import time
import random
from objects import *

''' nas linhas acima, são feitos os imorts das bibliotecas utilizadas para o funcionamento do código
    sendo "from objects import *" uma importação de arquivo com os objetos usados para compor o código.

'''


pygame.init()
bg = "campo.jpg" #bg é nome de variável que representa background (fundo).
screen = pygame.display.set_mode((800, 600)) #a dimensão da imagem corresponde ao tamanho da tela, sendo 800x600 a imagem.
bg = pygame.image.load(bg).convert() #renderiza a imagem para os parâmetros pygame, para que possa ser usada futuramente.
end = False #variável para finalização do algoritmo

distX, distY = 800 / 9, 600 / 6 #aqui temos duas variáveis criadas na mesma linha, sendo distância de X equivalente 800(dimensões da janela)/9(dimensão do campo real em metros) e Y seguindo a mesma linha de raciocínio.
distT = (distX + distY)/2 #temos aqui a média de pixels para cada metro do campo
print("A cada %.2f pixels se tem 1 (um) metro." % distT)


''' os valores abaixo seguem a regra de planos cartesianos para dimensionamento de janelas de software, ou seja,
    os valores em Y se iniciam no canto superior esquerdo da janela pygame, sendo assim, quanto mais pra baixo
    a posição de Y, maior ele é (positivamente), isto é, o eixo Y é o inverso do que estamos acostumados a ver. Com relação ao eixo X, a estrutura permanece a mesma
    (X é crescente para a direita).
'''

if (robo.x > bola.x): #por exemplo, se bola.x = 10 e robo.x = 15, o robô está à direita da bola.
    if (robo.y > bola.y): #se bola.y = 10 e robo.y = 15, o robô está abaixo da bola, em relação ao eixo Y.
        distancia = (robo.x - bola.x) + (robo.y - bola.y) #a posição dos valores é assim, para a conta não dar valores negativos.
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT #está conta indica a conversão da distância entre o robô e abola em pixels para metros.
        print("Distância (em metros) = %.2fm" % distanciaT)
    elif (robo.y < bola.y): #caso o X do robô for maior que o X da bola, mas o Y do robô for menor que o da bola, significa que o robô está acima da bola em relação ao eixo Y.
        distancia = (robo.x - bola.x) + (bola.y - robo.y) #como bola.y é maior que robo.y, o segundo parêntese é dado pela conta inversa em relação à conta acima, justamente pelo mesmo motivo.
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
elif (robo.x < bola.x): #se o X do robô for menor que o X da bola, significa que o robô está à esquerda da bola.
    if(robo.y > bola.y):
        distancia = (bola.x - robo.x) + (robo.y - bola.y) #primeiro parêntese invertido com relação à primeira conta, para que o resultado não seja negativo.
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
    elif (robo.y < bola.y):
        distancia = (bola.x - robo.x) + (bola.y - robo.y)
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)

#def varreduraEsquerda():
#    if (robo.x < bola.x):

while not end: #condição para enquanto end não mudar
    for event in pygame.event.get(): #essa função representa o tipo de evento que acontece, sendo ele qualquer movimento com o mouse na tela, ou qualquer botão pressionado.
        if event.type == pygame.QUIT: #se esse evento for igual a função "pygame.QUIT" (essa função representa o 'X' onde clicamos para fecharmos janelas), o end se tornará True e a janela será fechada.
            end = True
        if (robo.x > bola.x):
                robo.x -= 1
                if (robo.x <= bola.x):
                    robo.x += 1
                if(robo.y > bola.y):
                    robo.y -= 1
                    print("robo y %d" % robo.y)
                    print("bola y %d" % bola.y)
                elif (robo.y < bola.y):
                    robo.y += 1
                    print("robo y %d" % robo.y)
                    print("bola y %d" % bola.y)
                if (robo.x == bola.x and robo.y == bola.y):
                    y = bola.y - robo.y
                    x = robo.x - bola.x
                    print(y)
                    print(x)
                    bola.x -= 30

        elif (robo.x+30 < bola.x):
                    robo.x += 1
                    if(robo.y+15 > bola.y):
                        robo.y -= 1
                    elif (robo.y+15 < bola.y):
                        robo.y += 1
                    if (bola.x-9 - robo.x-10 <=15):
                        if (robo.y-15 - bola.y <= 15):
                            bola.x += 30



    screen.fill((0, 0, 0)) #essa linha preenche a tela com a cor preta, vale ressaltar que ela vem antes da linha de preenchimento com a imagem anteriormente carregada, porém não usada. Se a posição entre essa linha e a próxima fossem invertidas, a janela pygame seria completamente preta, com a imagem do campo atrás da camada preta.
    screen.blit(bg, (0, 0)) #carregamento da imagem (anteriormente renderizada) para que seja mostrada, de fato, na janela pygame.

    #****as linhas abaixo estão sujeitas a alterações.****

    #nessas linhas temos que prestar atenção nas diretrizes que cada objeto toma


    #sendo R (robô) um quadrado (apesar do nome remeter a um retângulo (rect)); screen é a variável da tela usada
    #com a imagem do campo de futebol; robo.color é uma variável de cor, criada dentro da classe robo no arquivo objects.py
    #pygame.Rect (com a letra R maiúscula e dentro de pygame.draw.rect()) representa as características do objeto criado
    #sendo os dois primeiros parâmetros os valores para as coordenadas (nesse caso, as coordenadas pertencem ao objeto robo
    #e são aleatórias) e os dois últimos parâmetros são para a definição da forma do objeto
    #(altura, largura).


    #B é um círculo que toma como base, a maioria dos parâmetros de R, apenas trocando de rect para circle e tendo algumas
    #diferenças nos parâmetros finais, sendo os dois primeiros (entre parênteses), as coordenadas no plano e o último valor
    #como sendo o diâmetro do círculo, esse círculo representa a bola em nosso código.

    #L representa a linha (que também representa a distância entre o robô e a bola) é meramente ilustrativo, podendo ser
    #removida a qualquer momento. Os parâmetros após a definição de tela e cor, são de X inicial e Y inicial (onde a linha deve começar)
    #a adição de 15 pixels em Xi e Yi se deve ao fato de que seu R tem 30 de altura e 30 de largura, sendo sua metade o valor adicionado
    #à variável xi e yi, para que a linha esteja posicionada exatamente no centro do objeto R. Os valores dos parênteses seguintes repre-
    #sentam o X final e Y final (onde a linha deve terminar), esses valores representam a linha encostando na bola (e não em seu centro, apenas tocando
    #a bola). O valor final (thickness) representa a espessura da linha, neste caso definido para 1.



    r = pygame.draw.rect(screen, robo.color, pygame.Rect(robo.x, robo.y, 30, 30))
    b = pygame.draw.circle(screen, bola.color, (bola.x, bola.y), bola.thickness)
    #l = pygame.draw.line(screen, line.color, (line.xi+15, line.yi+15), (line.xf, line.yf), line.thickness)

    pygame.display.flip() #para a atualização da tela após cada ação.
