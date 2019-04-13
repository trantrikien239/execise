
def draw_board(width,height):
    horizontal_line = ' ---' * width
    vertical_line = '|' + '   |' * width
    print(horizontal_line)
    for i in range(height):
        print(vertical_line)
        print(horizontal_line)


if __name__ == '__main__':
    valid_input = False
    while not valid_input:
        size_input = input('Please specify the board size (example: 3,3): ')
        size_list = [int(num) for num in size_input.split(',')]
        if len(size_list) == 2:
            valid_input = True
    draw_board(size_list[0],size_list[1])


