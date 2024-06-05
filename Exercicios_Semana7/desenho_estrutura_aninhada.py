'''
Semana 7

Exercício 1
Escreva um programa que recebe como entradas (utilize a função input)
dois números inteiros correspondentes à largura e à altura de um retângulo,
respectivamente. O programa deve imprimir, usando repetições encaixadas
(laços aninhados), uma cadeia de caracteres que represente o retângulo
informado com caracteres '#' na saída.
'''

coluna = int(input('Digite a largura: '))
linha = int(input('Digite a altura: '))

i = 1
while i <= linha:

    j = 1
    while j <= coluna:
        print('#', end='')
        j += 1
    print()
    i += 1
