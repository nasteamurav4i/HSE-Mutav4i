import random

alp = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

f = open('src.txt', 'r', encoding='utf-8')

words = f.read().split(' ')
words[0] = words[0].replace('\ufeff', '')

def syllableCount(word):
    """
    Функция, возвращающая кол-во слогов в слове.
    """
    res = 0

    for c in word.upper():
        if (alp.count(c) != 0):
            res += 1

    return res

def syllableEmphasis(word):
    """
    Функция возвращает идекс слога (не символа, именно слога), который находится под ударением
    """
    syllable = 1

    for i in range(len(word)):
        if (alp.count(word[i].upper()) != 0):
            syllable += 1
            if (word[i].isupper() is True):
                syllable -= 1
                break

    return syllable

def getWord(pSyllableCount,pSyllableEmphasis):
    """
    Функция возвращает слово, состоящее из определенного кол-ва слогов(pSyllableCount), в котором ударение падает на определенный слог(pSyllableEmphasis).
    """
    random.shuffle(words)
    #print(words)
    for i in range(len(words)):
        w = words[i]
        if (syllableCount(w) == pSyllableCount) and (syllableEmphasis(w) == pSyllableEmphasis):
            return w



def main():
    # Структура ударений, которой должны придерживаться слоги в строке
    sequence = [False,True,False,True,False,True,False,True]


    for z in range(4):
        for k in range(4):
            prevWordOneSyllable = False
            i = 0
            s = ''
            while (i < len(sequence)):
                    element = sequence[i]

                    # Если нынешний слог должен быть безударным
                    if (element == False):
                            if (random.randint(1, 2) == 1) or (prevWordOneSyllable == True):
                                currentWord = getWord(2, 2)
                                prevWordOneSyllable = False
                                i += 2
                                #print('Word 1: ' + currentWord)
                            else:
                                currentWord = getWord(1, 1)
                                prevWordOneSyllable = True
                                i += 1
                                #print('Word 2: ' + currentWord)
                    else:

                            currentWord = getWord(2, 1)
                            prevWordOneSyllable = False
                            i += 2

                            #print('Word 3: ' + currentWord)
                    s += currentWord + ' '

            print(s.lower().capitalize())
        print()
main()