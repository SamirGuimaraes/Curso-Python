'''
Semana 8 - Exercícios Adicionais

Exercício 1 - Maior elemento de uma lista
Escreva a função maior_elemento que recebe como parâmetro
uma lista com números inteiros e devolve um número inteiro
correspondente ao maior valor presente na lista recebida.
'''

def maior_elemento(lista):

    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior


lista = [1, 8, 25, 100, 99, 121]

maior_lista = maior_elemento(lista)
print(maior_lista)
