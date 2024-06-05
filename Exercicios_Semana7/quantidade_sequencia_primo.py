'''
Semana 7 - Exercícios Adicionais

Exercício 1 - Primos
Escreva a função n_primos que recebe como argumento um número inteiro
maior ou igual a 2 como parâmetro e devolve a quantidade de números
primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
'''

def verificacao(num):
    
    i = 1
    cont = 0
    while i <= num:
        divisoes = num % i
        if divisoes == 0:
            cont += 1
        i += 1

    if cont == 2:
        return True
    else:
        return False


def n_primos(num):
    
    cont_2 = 0
    while num >= 2:
        num_verificado = verificacao(num)
        if num_verificado == True:
            cont_2 += 1
        num -= 1

    return cont_2

num = int(input('Digite um número inteiro maior ou igual a 2: '))
while num < 2:
    num = int(input('Digite um número inteiro maior ou igual a 2: '))

cont_primos = n_primos(num)
print(cont_primos)
