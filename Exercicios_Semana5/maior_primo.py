'''
Semana 5

Exercício 2 - Primos
Escreva a função maior_primo que recebe um número inteiro
maior ou igual a 2 como parâmetro e devolve o maior número primo
menor ou igual ao número passado à função
'''

def conta_divisores(n):

    i = 1
    cont = 0 
    while i <= n:

        if n % i == 0:
            cont = cont + 1
        i = i + 1
    return cont

def primo(n):
    cont = conta_divisores(n)

    if cont == 2:
        return True
    else:
        return False
        


def maior_primo(n):

    while not(primo(n)):
        n = n-1

    return n

n = int(input('Digite um número maior ou igual a 2: '))
while n < 2:
    n = int(input('Digite um número maior ou igual a 2: '))
    
resultado = maior_primo(n)
print(resultado)


