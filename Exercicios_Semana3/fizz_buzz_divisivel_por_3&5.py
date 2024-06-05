'''
Semana 3

Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima

FizzBuzz
'''

num = int(input('Didite um número qualquer: '))

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
else:
    print(num)
