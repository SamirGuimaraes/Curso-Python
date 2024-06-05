'''
Semana 2 
Exercício 2 - Exercícios Adicionais

Uma empresa de cartão de crédito envia suas faturas por email com a
seguinte mensagem:

1 - Olá, Fulano de Tal
2 - A sua fatura com vencimento em 9 de Janeiro no valor de
    R$ 350,00 está fechada.

Escreva um programa que receba (entrada de dados através do teclado)
o nome do cliente, o dia de vencimento, o mês de vencimento
e o valor da fatura  e imprima (saída de dados) a mensagem com
os dados recebidos, no mesmo formato da mensagem acima.
Note que o programa imprime a saída em duas linhas diferentes.
Note também que, como não é preciso realizar cálculos,
o valor não precisa ser convertido para número, pode ser tratado como texto.
'''

nome = input('Insira seu nome completo: ')
dia_fatura = input('Digite o dia do vencimento da sua fatura: ')
mes_fatura = input('Digite o  mês do vencimento da sua fatura: ')
valor_fatura = input('Digite o valor da sua fatura: ')

print(f'Olá, {nome}')
print(f'A sua fatura com vencimento em {dia_fatura} de {mes_fatura} no valor de R$ {valor_fatura} está fechada.')
