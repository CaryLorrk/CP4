import sys


def main():
    n = int(sys.stdin.read().splitlines()[0])
    if n <= 3:
        print(1)
        return
    print(n-2)


if __name__ == "__main__":
    main()
