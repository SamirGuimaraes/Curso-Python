'''
Semana 4

Exercício 1
Escreva um programa que receba um número natural n na entrada e imprima!

n! (fatorial) na saída.
'''

def fatorial(n):

    p = 1
    i = 0

    while i < n:
        p = p * (n-i)
        i = i + 1
    return p 

n = int(input('Digite o valor de n: '))
fatorial = fatorial(n)
print(fatorial)

