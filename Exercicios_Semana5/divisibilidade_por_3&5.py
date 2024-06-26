'''
Semana 5 - Exercícios Adicionais

Exercício 1 - FizzBuzz
Escreva a função fizzbuzz que recebe como parâmetro
um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5,
ela deve devolver o número recebido como parâmetro.
'''

def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return n

n = int(input('Digite um valor inteiro e positivo:' ))

resultado = fizzbuzz(n)
print(resultado)
