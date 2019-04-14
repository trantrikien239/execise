import math
# User explanation
print('Think of a integer between 0 and 100')
# Start guessing
correct_guess = False
min = 0
max = 100
number_of_guesses = 0

while not correct_guess:
    guess = math.floor((min+max)/2)
    text_guess = 'My guess is ' + str(guess) + ' (correct/low/high) '
    feedback = input(text_guess).lower()
    if feedback == 'correct':
        correct_guess = True
        number_of_guesses += 1
        print('Yas, I got it in ' + str(number_of_guesses) +' guesses!!!')
    elif feedback == 'low':
        number_of_guesses += 1
        min = guess
    elif feedback == 'high':
        number_of_guesses += 1
        max = guess
    else:
        print('Please enter "correct","low" - if the guess is too low, or "high" - if the guess is too high')
