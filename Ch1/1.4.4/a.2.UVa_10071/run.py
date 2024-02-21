import sys

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        v, t = (int(x) for x in line.split())
        print(v*t*2)

if __name__ == "__main__":
    main()
