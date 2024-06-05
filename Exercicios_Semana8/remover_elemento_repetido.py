'''
Semana 8

Exercício 1 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como
parâmetro uma lista com números inteiros, verifica
se tal lista possui elementos repetidos e os remove.

A função deve devolver uma lista correspondente à primeira lista,
sem elementos repetidos. A lista devolvida deve estar ordenada.
'''

def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))
    lista_sem_repeticao.sort()
    return lista_sem_repeticao 

lista = [2,4,2,2,3,3,1]

resultado = remove_repetidos(lista)
print(resultado)
