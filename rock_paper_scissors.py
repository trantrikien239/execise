p1_name = input("Player 1, what's your name? ")
p2_name = input("Player 2, what's your name? ")

ask_p1 = p1_name + " what do you choose? (rock/paper/scissors) "
ask_p2 = p2_name + " what do you choose? (rock/paper/scissors) "

choices = ["rock", "paper", "scissors"]
answers = {"Yes": True, "No": False}

def p1_win(choice_1, choice_2):
    if choices.index(choice_1) != 2:
        if choices.index(choice_2) == choices.index(choice_1) + 1:
            return False
        else:
            return True
    else:
        if choices.index(choice_2) == 0:
            return False
        else:
            return True

next_game = "Yes"

while answers[next_game]:

    p1_choice = input(ask_p1)
    p2_choice = input(ask_p2)
    while p1_choice not in choices or p2_choice not in choices:
        print("Wrong input, please only type 'rock', 'paper' or 'scissors'")
        p1_choice = input(ask_p1)
        p2_choice = input(ask_p2)

    if p1_win(p1_choice,p2_choice):
        print("Conratulation " + p1_name + ", you won!!!")
    else:
        print("Conratulation " + p2_name + ", you won!!!")

    next_game = input("Wanna continue? (Yes/No) ")
    while next_game not in ["Yes", "No"]:
        print("Wrong input, please type 'Yes' or 'No'")
        next_game = input("Wanna continue? (Yes/No) ")
