import sys


def main():
    lines = sys.stdin.read().splitlines()
    text = lines[0]
    output = 'PER' * int(len(text) / 3)
    count = 0
    for c1, c2 in zip(text, output):
        if c1 != c2:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
