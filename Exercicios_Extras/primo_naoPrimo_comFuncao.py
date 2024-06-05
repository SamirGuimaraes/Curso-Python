def divisao(num):

    i = 1
    cont = 0
    while i <= num:

        divisoes = num % i
        if divisoes == 0:
            cont += 1
        i += 1
        
    return cont 

num = int(input('Digite um número inteiro: '))

cont = divisao(num)
if cont == 2:
    print(f'Sim, o número {num} é um número primo.')
else:
    print(f'Não, o número {num} não é um númer primo.')
