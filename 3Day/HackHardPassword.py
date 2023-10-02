import random
import string
import time
import re

def MakeHardPassword() -> str:
    print('You need make very hard password!\nPassword should have:\n  '
          '1. Length from 8 to 16\n  '
          '2. LowerCase and Uppercase letters\n  '
          '3. Numbers\n  ')

    while True:
        Password = input('Input there: ')
        if 8 <= len(Password) <= 16:
            Checks = [True, None, None]
            for i in Password:
                if i.islower() or i.isupper() and Checks[1] is None:
                    Checks[1] = True
                if i.isdigit() and Checks[2] is None:
                    Checks[2] = True
            if not None in Checks:
                return Password
            if Checks[1] is None:
                print('!!!LowerCase and Uppercase letters!!!\n')
            if Checks[2] is None:
                print('!!!Numbers!!!')
        else:
            print('Wrong input, check again on what password should have\n  '
                  '1. Length from 8 to 16\n  '
                  '2. LowerCase and Uppercase letters\n  '
                  '3. Numbers\n')


def TryToHackPass(Pass: str, totalSymbols: str) -> None:
    start = time.time()
    i = 0
    while True:
        i += 1
        if i == 50 * 10**6:
            print('I cant hacked your password')
        OneTry = ''.join(random.sample(totalSymbols, random.randint(8, 16)))
        print(f'Test {i}: {OneTry}')
        if Pass == OneTry:
            print('Your Pass is Hacked! It takes', (time.time() - start) * 10**3, 'ms')
            break




if __name__ == "__main__":
    total = string.ascii_letters + string.digits

    NewPassword = MakeHardPassword()
    time.sleep(2)
    TryToHackPass(NewPassword, total)



