'''
Semana 3 - Exercícios adicionais

Exercício 1 - Distância entre dois pontos

Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto
'''

from math import sqrt

X1 = int(input('Para calcularmos a distância entre pontos determine a distancias dos quatros pontos \nQual a coordenada X do ponto inicial: '))
Y1 = int(input('Qual a coordenada Y do ponto inicial: '))
X2 = int(input('Qual a coordenada X do ponto final: '))
Y2 = int(input('Qual a coordenada Y do ponto final: '))


distancia = sqrt( ( (X1 - X2)**2 + (Y1 - Y2)**2 ) )

if distancia < 10:
    print('A distância entre os pontos é considerada perto.')
else:
    print('A distância entre os pontos é considerada longe..')

    
