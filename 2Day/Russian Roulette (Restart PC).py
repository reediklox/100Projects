import os
import platform
from random import randint
import time


def restart(Rand: int):
    if Rand:
        print("Just kidding, you'r lucky! :D")
        return 0
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")


def reverseTime(nSec):
    for i in range(nSec, 0, -1):
        print(f'{i}...')
        time.sleep(1)


def CheckAnswer(Tasks: dict, Task: str, Answer: str) -> str:
    return 'Correct! Congratulations!!!' if Answer in Tasks[Task] else 'Wrong Answer! Bye-bye XD'


if __name__ == '__main__':
    TaskDictionary = {
        'The boy paid 11 dollars for a bottle with a cork. '
        'A bottle costs 10 dollars more than a cork. \n'
        'How much does a cork cost? ': ['50cents',
                                        'cents50',
                                        '0.5dollar'],

        'How many times during the day do the minute and hour hands of the clock form a right angle?': ['44',
                                                                                                        '44times'],

        'What is the only number where the number of letters in its name is equal to its value?': ['4',
                                                                                                   'four'],

        'From the numbers 5, 5, 5, 1 and simple arithmetic operations "+", "-" "*", "/" you need to get the number 24.': ['(5-1/5)*5',
                                                                                                                          '(5-1/5)*5=24']
    }

    randIndex = randint(0, len(TaskDictionary) - 1)
    Keys =      list(TaskDictionary.keys())
    answer =    input(f'{Keys[randIndex]}'
                      f'\n\tInput your answer: ').replace(' ', '').lower()

    CorrWrong = CheckAnswer(TaskDictionary,
                            Keys[randIndex],
                            answer)

    if CorrWrong == 'Correct! Congratulations!!!':
        print(CorrWrong)
    else:
        print(CorrWrong)
        ResOrNo = randint(0, 1)
        reverseTime(randint(5, 10))
        restart(ResOrNo)
