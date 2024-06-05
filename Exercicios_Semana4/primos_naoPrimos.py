'''
Semana 4 - Exercícios Adicionais

Exercício 1
Escreva um programa que receba um número inteiro positivo
na entrada e verifique se é primo.

Se o número for primo, imprima "primo".
Caso contrário, imprima "não primo".
'''

num = int(input('Digite um número inteiro: '))

i = 1
cont = 0

while i <= num:

    divisao = num % i
    if divisao == 0:
        cont = cont + 1
    
    i = i + 1

if cont == 2:
    print('primo')
else:
    print('não primo')
