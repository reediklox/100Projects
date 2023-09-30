from random import randint
import time


def getRandInd(lenArr):
    return randint(0, lenArr - 1)


def CreatePhrase(someDict, letters, randInt):
    return (someDict[letters[randInt]], letters[randInt]) if letters[randInt] in someDict.keys() else (None, None)


def While(Dict, letters, phrase):
    while None in phrase:
        randInt = getRandInd(lenArr=len(letters))
        Ind, letter = CreatePhrase(Dict, letters, randInt)

        if not Ind and not letter:
            continue

        if isinstance(Ind, list):
            for i in Ind:
                phrase[i] = letter
        else:   phrase[Ind] = letter
    return phrase


def JustPrint(phrase):
    print(f'\n{", ".join(phrase)}!\n')


if __name__ == "__main__":
    lowerCaseLetters = list(map(chr, (range(97, 123))))

    helloDict = {
        'h': 0,
        'e': 1,
        'l': [2, 3],
        'o': 4
    }
    worldDict = {
        'w': 0,
        'o': 1,
        'r': 2,
        'l': 3,
        'd': 4
    }

    Phrase = [[None]*5, [None]*5]

    s = time.time()
    Phrase[0] = While(helloDict, lowerCaseLetters, Phrase[0])
    e = time.time()
    print(f'Time of make word {"".join(Phrase[0]).capitalize()}: {(e - s) * 10**3} ms')

    s = time.time()
    Phrase[1] = While(worldDict, lowerCaseLetters, Phrase[1])
    e = time.time()
    print(f'Time of make word {"".join(Phrase[1]).capitalize()}: {(e - s) * 10**3} ms')
    Phrase[0] = ''.join(Phrase[0])
    Phrase[1] = ''.join(Phrase[1])

    Phrase[0] = Phrase[0].capitalize()

    JustPrint(Phrase)


