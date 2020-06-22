# Advent of Code 2019 Day 3


def manhattan_distance(x_start, y_start, x_index, y_index):
    return abs(x_index - x_start) + abs(y_index - y_start)


def calc_intersection_distances(board):
    min_distance = len(board)
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 2:
                start = int(len(board)/2)
                distance = manhattan_distance(start, start, i, j)

                if distance < min_distance:
                    min_distance = distance

    return min_distance


def init_board(size):
    board = [[0 for i in range(size)] for j in range(size)]
    return board


def print_board_state(board):

    for i in board:
        print(i)


def run_wire(board, wire):

    x_start = y_start = int(len(board)/2)
    board[x_start][y_start] = 7
    x_index = x_start
    y_index = y_start
    print(wire)

    for command in wire:
        direction = command[0:1]
        distance = int(command[1:])

        for j in range(0, distance):
            # print(str(x_index) + ', ' + str(y_index))
            # print_board_state(board)
            if board[x_index][y_index] == 1:
                board[x_index][y_index] = 2
            elif board[x_index][y_index] == 0:
                board[x_index][y_index] = 1

            if direction == 'R':
                x_index += 1
            elif direction == 'L':
                x_index -= 1
            elif direction == 'U':
                y_index += 1
            elif direction == 'D':
                y_index -= 1


if __name__ == '__main__':

    board = init_board(20000)

    with open('input.txt', 'r') as input:

        wire1 = input.readline().split(',')
        wire2 = input.readline().split(',')

        # wire1 = ['R8','U5','L5','D3']
        # wire2 = ['U7','R6','D4','L4']

        # wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        # wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

        # wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        # wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

        run_wire(board, wire1)
        run_wire(board, wire2)
        # print_board_state(board)

        print(calc_intersection_distances(board))