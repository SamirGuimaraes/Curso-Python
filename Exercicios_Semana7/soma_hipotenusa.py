'''
Semana 7 - Exercícios Adicionais

Exercício 2 - (Difícil) Soma das hipotenusas
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe
um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número.
Em outras palavras, h é uma hipotenusa se existem números inteiros  i e  j tais que:

h^2 =i^2 + j^2
 

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo 
n e devolva a soma de todos os inteiros entre 1 e 
n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.
'''

def e_hipotenusa(num):

    for a in range(1, num):  
        for b in range(1, num):
            if a**2 + b**2 == num**2:
                return True

def soma_hipotenusas(num):

    soma = 0
    while num > 1:
        hipotenusa = e_hipotenusa(num)
        if hipotenusa:
            soma += num
        num -= 1
    return soma

num = int(input('Digite um número inteiro e positivo: '))


print(soma_hipotenusa(num))

