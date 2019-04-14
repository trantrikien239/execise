import check_tic_tac_toe_26 as check_ttt
import draw_a_game_board_24 as draw_board


#Functions
def brick_builder(player_number):
    #Player number 1 -> X; Player number 2 -> O
    if player_number == 1:
        return ' X |'
    elif player_number == 2:
        return ' O |'
    else:
        return '   |'

def tic_tag_toe_draw(board):
    #Receive a board (3x3 array) and print out the board
    board_width = 3
    board_height = 3
    horizontal_line = ' ---' * board_width
    print(horizontal_line)
    for i in range(board_height):
        board_line = '|'
        for j in range(board_width):
            board_line = board_line + brick_builder(board[i][j])
        print(board_line)
        print(horizontal_line)

def board_update(board,player_number):
    coordinate =[int(coor)-1 for coor in input('Player ' + str(
        player_number) + '! Where is your next move? ((x,y) - with (1,1) is the top left corner): ').split(',')]
    while board[coordinate[0]][coordinate[1]] != 0:
        print('Invalid move, the position you chose has already existed')
        coordinate = [int(coor) - 1 for coor in input('Player ' + str(
            player_number) + '! Where is your next move? ((x,y) - with (1,1) is the top left corner): ').split(',')]

    board[coordinate[0]][coordinate[1]] = player_number
    tic_tag_toe_draw(board)
    return board


if __name__ == '__main__':
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    game_finished_count = False
    turn_count = 1
    print('Welcome to a game of tic tac toe!')
    draw_board.draw_board(3,3)
    while not game_finished_count:
        board = board_update(board,turn_count)
        if turn_count == 1:
            turn_count = 2
        else:
            turn_count = 1

        game_finished_count = check_ttt.check_tic_tac_toe(board)