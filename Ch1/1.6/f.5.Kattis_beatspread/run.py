import sys


def main():
    lines = sys.stdin.read().splitlines()

    n_cases = int(lines[0])
    lines = lines[1:]

    for n in range(n_cases):
        s, d = [int(x) for x in lines[n].split()]
        x = int((s + d)/2)
        y = s - x
        if (x < 0 or y < 0 or x + y != s or abs(x - y) != d):
            print('impossible')
        else:
            print(x, y)


if __name__ == "__main__":
    main()
