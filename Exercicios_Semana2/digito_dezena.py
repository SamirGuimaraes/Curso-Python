'''
Semana 2

Exercício 3 - Exercícios Adicionais

Faça um programa em Python que recebe um número inteiro e
imprime seu dígito das dezenas. Observe o exemplo abaixo:
'''

num = int(input('Digite um número qualquer: '))

resto_centena = num % 100
dezena = resto_centena // 10

print(f'O dígito das dezenas é {dezena}')
