import sys
from functools import cmp_to_key
from itertools import zip_longest

RATING = {
    'upper': 3,
    'middle': 2,
    'lower': 1
}


def cmp(x, y):
    for a, b in zip_longest(x[1], y[1], fillvalue=2):
        if a > b:
            return -1
        if b > a:
            return 1

    return -1 if x[0] < y[0] else 1



def process_case(lines):
    people = []
    for line in lines:
        name, r = line.split(': ')
        cls, _ = r.split(' ')
        rating = [RATING[c] for c in reversed(cls.split('-'))]
        people.append((name, rating))
    
    people.sort(key=cmp_to_key(cmp))
    for k in people:
        print(k[0])
    print('==============================')

def main():
    lines = sys.stdin.read().splitlines()
    T = int(lines[0])
    lines = lines[1:]
    for t in range(T):
        n = int(lines[0])
        process_case(lines[1: n+1])
        lines = lines[n+1:]
if __name__ == "__main__":
    main()
