'''
Semana 6

Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente
dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente,
retirando pelo menos 1 e no máximo m peças cada um.
Quem tirar as últimas peças possíveis ganha o jogo.
'''

def computador_escolhe_jogada(n, m):
    remove_computador = 1

    while remove_computador != m:
        if (n - remove_computador) % (m + 1) == 0:
            return remove_computador
        else:
            remove_computador += 1

    return remove_computador


def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        remove_jogador = int(input('Quantas peças você vai tirar? '))
        if remove_jogador > m or remove_jogador < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            jogada_valida = True

    return remove_jogador


def campeonato():
    numero_rodada = 1
    while numero_rodada <= 3:
        print()
        print('**** Rodada', numero_rodada, '****')
        print()
        partida()
        numero_rodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vez_do_pc = False

    if n % (m + 1) == 0:
        print()
        print('Você começa!')
    else:
        print()
        print('Computador começa!')
        vez_do_pc = True

    while n > 0:
        if vez_do_pc:
            remove_computador = computador_escolhe_jogada(n, m)
            n = n - remove_computador
            if remove_computador == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', remove_computador, 'peças')

            vez_do_pc = False
        else:
            remove_jogador = usuario_escolhe_jogada(n, m)
            n = n - remove_jogador
            if remove_jogador == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', remove_jogador, 'peças')
            vez_do_pc = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipo_de_partida = int(input('2 - para jogar um campeonato '))

if tipo_de_partida == 2:
    print()
    print('Você escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipo_de_partida == 1:
        print()
        partida()
