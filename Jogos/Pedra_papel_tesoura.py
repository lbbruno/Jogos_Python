import random

def cabecalho(titulo):
    """ -> Cabeçalho
        Exibe na tela o título do programa e modela de acordo com o número de caracteres

        // Output
        ======================
          Titulo do Programa
        ======================

        :param titulo: dada como parâmetro ao chamar a função
        :return:
        """
    div = '=' * int(len(titulo) + 4)
    titulo = '  ' + titulo
    print(f'{div}\n{titulo}\n{div}')

def play():
    cabecalho('PEDRA / PAPEL / TESOURA')

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
