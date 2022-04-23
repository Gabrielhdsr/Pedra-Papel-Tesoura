import random


def play():
    # r > s, s > p, p > r
    print('Para jogar use "P"(papel), "S"(tesoura) e "R"(pedra)')
    user = input('Faça sua jogada: ').upper()
    pc = random.choice(['P', 'S', 'R'])
    print(f'Player: {user}  X  PC: {pc} \n')

    if (user != 'P') and (user != 'S') and (user != 'R'):
        return 'Comando inválido'
    elif user == pc:
        return 'Empate'
    elif win(user, pc):
        return 'Você venceu! :)'
    else:
        return 'Você perdeu! :('


def win(player, opponent):
    if (player == 'P' and opponent == 'R') or (player == 'R' and opponent == 'S') or \
            (player == 'S' and opponent == 'P'):
        return True


play_again = 'Y'

print('****** PEDRA, PAPEL E TESOURA ****** \n')

while play_again == 'Y':
    score = play()
    print(score)
    play_again = input('Se deseja jogar novamente, digite "Y": ').upper()






