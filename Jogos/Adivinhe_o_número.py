import random

def cabecalho(titulo):
    div = '=' * int(len(titulo) + 4)
    titulo = '  ' + titulo
    print(f'{div}\n{titulo}\n{div}')

def guess(x):
    cabecalho('Adivinhe o número que pensei!')
    num_aleatorio = random.randint(1, x)
    escolha_usuario = 0
    while escolha_usuario != num_aleatorio:
        escolha_usuario = int(input(f'Escolha um número entre 1 e {x}: '))
        if escolha_usuario < num_aleatorio:
            print('Desculpe, tente novamente. o numero é maior.')
        elif escolha_usuario > num_aleatorio:
            print('Desculpe, tente novamente. o numero é menor.')

    print(f'Você acertou! o número é {num_aleatorio}.')

guess(999)