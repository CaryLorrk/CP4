import sys

def main():
    lines = sys.stdin.read().splitlines()
    N, M = [int(x) for x in lines[0].split()]
    lines = lines[1:]

    x = [[int(x) for x in line.split()] for line in lines]

    for m in range(1, M):
        x[0][m] = x[0][m] + x[0][m-1]

    for n in range(1, N):
        x[n][0] = x[n][0] + x[n-1][0]
    

    for n in range(1, N):
        for m in range(1, M):
            l = max(x[n-1][m], x[n][m-1])
            x[n][m] = x[n][m] + l

    print(' '.join([str(i[M-1]) for i in x]))





if __name__ == "__main__":
    main()
