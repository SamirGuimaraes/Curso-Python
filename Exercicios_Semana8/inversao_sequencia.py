'''
Semana 8 - Exercícios Adicionais

Exercício 2 - Invertendo sequência
Como pedido na primeira video-aula desta semana,
escreva um programa que recebe uma sequência de
números inteiros e imprima todos os valores em
ordem inversa. A sequência sempre termina pelo número 0.
Note que 0 (ZERO) não deve fazer parte da sequência.
'''

n = int(input('Digite um número: '))
lista = []
while n != 0:
    lista.append(n)
    n = int(input('Digite um número: '))

lista_inversa = lista[::-1]

for i in lista_inversa:
    print(i)
    print()
