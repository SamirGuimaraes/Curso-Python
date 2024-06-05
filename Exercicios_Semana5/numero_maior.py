'''
Semana 5

Exercício 1 - Máximo
Escreva a função maximo que recebe 2 números
inteiros como parâmetro e devolve o maior deles.
'''

def maximo(n1, n2):

    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input('Insira um número inteiro e positivo: '))
n2 = int(input('Insira um segundo número inteiro e positivo: '))

maximo = maximo(n1, n2)
print(maximo)


    
