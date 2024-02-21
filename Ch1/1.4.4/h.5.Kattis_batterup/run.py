import sys


def main():
    lines = sys.stdin.read().splitlines()

    n_at_bats = int(lines[0])
    
    bases = 0
    for i in lines[1].split():
        if i == '-1':
            n_at_bats = n_at_bats - 1
            continue
        bases = bases + int(i)

    print(bases/n_at_bats)


if __name__ == "__main__":
    main()
