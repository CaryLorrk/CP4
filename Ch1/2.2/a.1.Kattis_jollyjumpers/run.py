import sys
import math


def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        values = [int(x) for x in line.split()]
        N = int(values[0])
        exists = [False] * N
        for n, v in enumerate(zip(values[1:], values[2:])):
            try:
                exists[abs(v[1] - v[0])] = True
            except IndexError:
                ...

        if all(exists[1:]):
            print("Jolly")
        else:
            print("Not jolly")

        
        


if __name__ == "__main__":
    main()
