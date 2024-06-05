'''
Semana 4 - Exercícios Adicionais

Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e
verifique se o número recebido possui ao menos um dígito
com um dígito adjacente igual a ele.

Caso exista, imprima "sim"; se não existir, imprima "não".
'''

num = int(input('Digite um número inteiro: '))

digitoAnterior = -1 
digito = 0
cont = 0 
while not(num==0) :

    digito = num % 10

    if digito == digitoAnterior:
        cont = cont + 1


    digitoAnterior = digito
    
    num = num // 10


if cont == 0:
    print('não')
else:
    print('sim')
