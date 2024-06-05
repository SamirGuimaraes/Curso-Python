num = int(input('Digite um número: '))

fator = 2
multiplicidade = 0

while num > 1:
    while num % fator == 0:
        multiplicidade += 1
        num = num / fator
    if multiplicidade > 0:
        print(f'Fator {fator}, multiplicidade = {multiplicidade}.')
    fator += 1
    multiplicidade = 0
