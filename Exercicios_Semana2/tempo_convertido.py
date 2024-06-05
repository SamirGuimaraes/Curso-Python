'''
Semana 2

Exercício 2 - Exercícios Adicionais

Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias,
ou seja, faça um programa em Python que, dada a quantidade de segundos,
"quebre" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando
ou outras diferenças são considerados erro
'''

tempo = int(input('Insira um valor em segundos: '))

dias = tempo//86400
horas = (tempo % 86400) // 3600
minutos = ((tempo % 86400) % 3600) // 60
segundos  = ((tempo % 86400) % 3600) % 60

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')
