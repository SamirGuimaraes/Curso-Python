'''
Semana 5 - Exercícios Adicionais

Exercício 2 - Máximo com 3 parâmetros
Reescreva a função 'maximo' do outro exercício, que devolve o maior valor
dentre dois inteiros recebidos, para que ela passe a receber
3 valores inteiros como parâmetros e devolva o maior dentre eles.
'''

def maximo(n1, n2, n3):

    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


n1 = int(input('Digite um valor inteiro e positivo: '))
n2 = int(input('Digite um segundo valor inteiro e positivo: '))
n3 = int(input('Digite um terceio valor inteiro e positivo: '))

resultado = maximo(n1, n2, n3)
print(resultado)
