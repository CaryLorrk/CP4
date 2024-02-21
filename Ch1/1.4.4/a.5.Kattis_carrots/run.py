import sys

def main():
    lines = sys.stdin.read().splitlines()

    print(lines[0].split()[1])

if __name__ == "__main__":
    main()
