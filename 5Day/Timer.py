import time
import winsound

def timer(t):
    while t:
        mins, sec = divmod(t, 60)

        ter = '{:02d}:{:02d}'.format(mins, sec)
        print(f'\r{ter}', end='')
        time.sleep(1)

        t -= 1

    print('\r00:00')
    print('\n\nTimer completed!')
    winsound.PlaySound('din-iphone.mp3', winsound.MB_OK)


if __name__ == '__main__':
    t = int(input('Enter the time in seconds: '))

    timer(t)