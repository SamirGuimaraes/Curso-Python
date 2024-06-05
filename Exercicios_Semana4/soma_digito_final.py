'''
Semana 4

Exercício 3
Escreva um programa que receba um número inteiro na entrada,
calcule e imprima a soma dos dígitos deste número na saída
'''

num = int(input('Digite um número inteiro e positivo: '))

soma = 0 

while not(num == 0):

    digito = num % 10
    soma = soma + digito
    num = num // 10
    
print(soma)
