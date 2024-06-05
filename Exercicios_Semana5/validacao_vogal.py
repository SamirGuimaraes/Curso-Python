'''
Semana 5

Exercício 3 - Vogais
Escreva a função vogal que recebe um único caractere
como parâmetro e devolve True se ele for uma vogal e
False se for uma consoante.
'''

def vogal(l):

    if (l == 'a' or l == 'A' or
        l == 'e' or l == 'E' or
        l == 'i' or l == 'I' or
        l == 'o' or l == 'O' or
        l == 'u' or l == 'U'):
        return True
    else:
        return False

l = input('Digite um letra que seja vogal: ')

resultado = vogal(l)
print(resultado)
