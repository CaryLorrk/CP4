import sys


def main():
    lines = sys.stdin.read().splitlines()
    answer = []
    while N := int(lines[0]):
        names = lines[1:N+1]
        answer.append('\n'.join(sorted(names, key=lambda x: x[:2])))
        lines = lines[N+1:]

    print('\n\n'.join(answer))


if __name__ == "__main__":
    main()
