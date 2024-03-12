import sys


def main():
    lines = sys.stdin.read().splitlines()

    N, M = [int(x) for x in lines[0].split()]

    lines = lines[1:]

    count = 1
    for m in range(M):
        all_underscore = True
        for n in range(N):
            if lines[n][m] != '_':
                all_underscore = False
                break
        if all_underscore:
            count += 1
            
    print(count)





if __name__ == "__main__":
    main()
