'''
Semana 7

Exercício 2
Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
'''

coluna = int(input('Digite a largura: '))
linha = int(input('Digite a altura: '))

i = 1
while i <= linha:

    j = 1
    while j <= coluna:
        if (i == 1 or j == 1) or (i == linha or j == coluna):
            print('#', end='')
        else:
            print(' ', end='')
        j += 1
    print()
    i += 1
