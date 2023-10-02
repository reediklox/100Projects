# Rock Fire Scissors Sponge Paper Air Water
from random import randint
import time


RPS = {
    'Rock': ['Fire', 'Scissors', 'Sponge'],
    'Fire': ['Scissors', 'Sponge', 'Paper'],
    'Scissors': ['Sponge', 'Paper', 'Air'],
    'Sponge': ['Paper', 'Air', 'Water'],
    'Paper': ['Air', 'Water', 'Rock'],
    'Air': ['Water', 'Rock', 'Fire'],
    'Water': ['Rock', 'Fire', 'Scissors']
}

def Game():
    UserChoice = {f'{i + 1}': k for i, k in enumerate(list(RPS.keys()))}
    Output = [f'\n{ind + 1} {key}\n' for ind, key in enumerate(list(RPS.keys()))]
    print('Welcome to game Rock Paper Scissors Advanced!\n')

    while True:
        user = input(f'Choose your gun:\n {"".join(Output)}')
        try:
            int(user)
        except ValueError:
            print('You need input number, try again!')
            continue
        break

    randInd = randint(0, len(RPS) - 1)
    computerChoice = list(RPS.keys())[randInd]

    print('Computer make his choice.', end='')
    for i in range(4):
        time.sleep(1)
        print('.', end='')
    print('\n')

    time.sleep(2)
    print(UserChoice[user], 'vs', computerChoice)
    time.sleep(1)

    if UserChoice[user] == computerChoice:
        return 'Draw'

    if computerChoice in RPS[UserChoice[user]]:
        print('You won the computer, congratulation!')
    else:
        print('Oh noo, you loose... loser')
        for i in range(randint(1, 100)):
            print(f'{i} Take The L')

    return 'Not Draw'

if __name__ == '__main__':
    result = 'Draw'
    while result == 'Draw':
        result = Game()
