import sys
from functools import reduce
from math import fabs


def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        print(reduce(lambda x, y: int(fabs(int(x) - int(y))), line.split()))


if __name__ == "__main__":
    main()
