num = int(input('Digite um número inteiro e positivo para saber se é divisível por 3 e 5 ao mesmo tempo: '))

if num % 5 == 0 and num % 3 == 0:
    print('FizzBuzz')
else:
    print(num)
