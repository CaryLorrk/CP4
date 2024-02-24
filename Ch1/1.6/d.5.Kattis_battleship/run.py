import sys
from itertools import chain


def process(boards, shots, h):
    target = 1
    counts = [
        list(chain.from_iterable(boards[0]) ).count('#'),
        list(chain.from_iterable(boards[1]) ).count('#')
    ]
    for shot in shots:
        if boards[target][h-shot[1]-1][shot[0]] == '#':
            boards[target][h-shot[1]-1][shot[0]] = '_'
            counts[target] -= 1
            if counts[target] == 0:
                target = 0 if target == 1 else 1
        else:
            target = 0 if target == 1 else 1

        if target == 1 and (counts[0] == 0 or counts[1] == 0):
            break

    if counts[0] == 0 and counts[1] != 0:
        print("player two wins")
    elif counts[0] != 0 and counts[1] == 0:
        print("player one wins")
    else:
        print("draw")


def main():
    lines = sys.stdin.read().splitlines()
    n_cases = int(lines[0])
    lines = lines[1:]

    for _ in range(n_cases):
        w, h, n = (int(x) for x in lines[0].split())
        lines = lines[1:]
        board1 = [list(l) for l in lines[0:h]]
        lines = lines[h:]
        board2 = [list(l) for l in lines[0:h]]
        lines = lines[h:]
        shots = [ [int(x) for x in l.split()] for l in lines[:n]]
        lines = lines[n:]

        process([board1, board2], shots, h)


if __name__ == "__main__":
    main()
