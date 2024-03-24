import sys


def main():
    lines = sys.stdin.read().splitlines()
    P = int(lines[0])
    for line in lines[1:P+1]:
        l = [int(x) for x in line.split()]
        K = l[0]
        d = l[1:21]
        c = 0
        while d:
            i = d.index(min(d))
            c += i
            del d[i]

        print(K, c)


if __name__ == "__main__":
    main()
