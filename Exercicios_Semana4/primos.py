'''
Semana 4

Exercício 2
Receba um número inteiro positivo na entrada e imprima os 
n primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.
'''

n = int(input('Digite o valor de n: '))

i = 0
while i < n:
    i += 1
    print(2*i - 1)
