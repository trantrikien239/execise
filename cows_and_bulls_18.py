import random as rd



def guess_check(answer,guess):
    cows = 0
    bulls = 0
    for index, character in enumerate(guess):
        if character == answer[index]:
            cows = cows + 1
        if character in answer:
            bulls = bulls + 1
    bulls = bulls - cows
    print('You have ' + str(cows) + ' cows')
    print('You have ' + str(bulls) + ' bulls')
    if cows == 4:
        return True
    else:
        return False

if __name__ == '__main__':
    print('Welcome to the Cows and Bulls Game!')
    ANSWER = str(rd.randint(1000,9999))
    # print(ANSWER)
    finished = False
    while not finished:
        guess = input('Enter a 4-digits number (from 1000 to 9999): ')
        finished = guess_check(ANSWER,guess)
    print('The answer is correct, you won!')
