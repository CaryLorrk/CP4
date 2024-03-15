import sys


def print_board(board):
    print('\n'.join([' '.join([str(x) for x in row]) for row in board]))


def left(board):
    for r in range(0, 4):
        combined = -1
        for c in range(1, 4):
            if board[r][c] == 0:
                continue
            
            n = 0
            while board[r][c-n-1] == 0:
                n += 1

            if n > 0:
                board[r][c-n], board[r][c] = board[r][c], board[r][c-n]

            if board[r][c-n] == board[r][c-n-1] and c-n-1 > combined:
                board[r][c-n-1] = board[r][c-n-1] * 2
                board[r][c-n] = 0
                combined = c-n-1


def rotate(board):
    return list(zip(*reversed(board)))


def rotate_ccw(board):
    return [list(line) for line in reversed(list(zip(*board)))]



def main():
    lines = sys.stdin.read().splitlines()
    board = [[int(x) for x in line.split()] for line in lines[:4]]
    direction = int(lines[4])

    for _ in range(direction):
        board = rotate_ccw(board)

    left(board)

    for _ in range(direction):
        board = rotate(board)

    print_board(board)


if __name__ == "__main__":
    main()
