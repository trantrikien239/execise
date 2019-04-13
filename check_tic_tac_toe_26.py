import numpy as np

def check_linear(list_of_numpy_arrays):
    answer_check_linear = False
    for i in range(len(list_of_numpy_arrays)):
        list_of_differences = []
        for j in range(len(list_of_numpy_arrays)):
            list_of_differences.append(list_of_numpy_arrays[i] - list_of_numpy_arrays[j])
        #check linear
        list_of_all_differences_couples = [[a,b] for k,a in enumerate(list_of_differences) for l,b in enumerate(list_of_differences) if k!=l]
        for couple in list_of_all_differences_couples:
            if (couple[0] == couple[1]).all() or (couple[0] == -couple[1]).all():
                answer_check_linear = True
    return answer_check_linear

def check_tic_tac_toe(board):
    game_finished_count = False
    # Check if board is valid
    if len(board) != 3:
        print('Invalid board')
    else:
        for row in board:
            if len(row) != 3:
                print('Invalid board')
    # Establish list of 1 and list of 2
    list_of_1 = []
    list_of_2 = []
    list_of_0 = []
    for y in range(3):
        for x in range(3):
            if board[y][x] == 1:
                list_of_1.append(np.array([x,y]))
            elif board[y][x] == 2:
                list_of_2.append(np.array([x,y]))
            else:
                list_of_0.append(np.array([x,y]))

    if check_linear(list_of_1):
        print('Player 1 wins!')
        game_finished_count = True
    elif check_linear(list_of_2):
        print('Player 2 wins!')
        game_finished_count = True
    elif len(list_of_0) == 0:
        print('Draw!')
        game_finished_count = True
    else:
        pass
    return game_finished_count

if __name__ == '__main__':
    game = [
        [2, 2, 0],
        [0, 1, 1],
        [2, 1, 1]]
    check_tic_tac_toe(game)

