import sys


def main():
    lines = sys.stdin.read().splitlines()
    text = lines[0]
    print(''.join([x[0] for x in text.split('-')]))


if __name__ == "__main__":
    main()
