import random as rd
user_input = input("Guess a number: ")
# def filter(num, user_input):
#     try:
#         dif = num - int(user_input)
#     except:
#         raise
while user_input != "exit":
    num = rd.randint(1,9)
    # print(num)
    dif = num - int(user_input)
    while dif != 0:
        if dif < 0:
            user_input = input("Your guess is too high, try again: ")
            dif = num -int(user_input)
        elif dif > 0:
            user_input = input("Your guess is too low, try again: ")
            dif = num -int(user_input)
        else:
            break

    user_input = input("Congrats, your guess is correct. Let's play one more round. What's your guess? ")
        
