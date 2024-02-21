import sys
from itertools import permutations


def main():
    line = sys.stdin.read().splitlines()[0]
    
    perms = [''.join(p) for p in  permutations('RBL') ]
    mappings = {
        'R': 'S',
        'B': 'K',
        'L': 'H',
    }

    i = 0
    while i < len(line):
        if i + 2 < len(line):
            if line[i:i+3] in perms:
                print('C', end="")
                i = i + 3
                continue
        print(mappings[line[i]], end="")

        i = i + 1
    print("")


if __name__ == "__main__":
    main()
