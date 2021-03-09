import random

def play():
    lista = ['pedra', 'papel', 'tesoura']
    print('Faça sua escolha...')
    escolha = int(input('[1]Pedra [2]Papel [3]Tesoura:'))
    usuario = lista[escolha-1]
    computador = random.choice(lista)


    print(f'Usuário: {usuario.upper()} X {computador.upper()} :Computador')

    if usuario == computador:
        return 'Empatou!'

    if ganhador(usuario, computador):
        return 'Você ganhou!'
    return 'Você perdeu!'


def ganhador(jogador, oponente):
    if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel')\
            or (jogador == 'papel' and oponente == 'pedra'):
        return True


print(play())
