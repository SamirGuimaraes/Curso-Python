'''
Semana 3 - Exercícios Adicionais

Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros ax^2+bx+c, respectivamente,
e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:
esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X
'''

from math import sqrt

a = int(input('Digite o termo de segundo grau: '))
b = int(input('Digite o termo de primeiro grau: '))
c = int(input('Digite o termo independente: '))
delta = b**2 - (4*a*c)

if delta < 0:
    print('esta equação não possui raízes reais')
elif delta == 0:
    raiz = (-b/(2*a))
    
    print(f'a raiz desta equação é {raiz}.')
else:
    raiz1 = ((-b+sqrt(delta))/(2*a))
    raiz2 = ((-b-sqrt(delta))/(2*a))

    if raiz1 < raiz2:
        print(f'as raízes da equação são {raiz1:.6f} e {raiz2:.6f}.')
    else:
        print(f'as raízes da equação são {raiz2:.6f} e {raiz1:.6f}.')
