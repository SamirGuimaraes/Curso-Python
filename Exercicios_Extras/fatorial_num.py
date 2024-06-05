def fatorial(n):

    fatorial = 1
    while n >= 1:
        fatorial *= n
        n -= 1

    return(fatorial)

n = int(input('Digite um número inteiro: '))

fatorial = fatorial(n)
print(f'O fatorial de {n} corresponde a: {fatorial}.')
    
