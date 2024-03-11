import sys


def main():
    lines = sys.stdin.read().splitlines()

    N = int(lines[0])
    H = [int(x) for x in lines[1].split()[:N]]
    c = [0] * 1000001
    result = 0

    for v in H:
        c[v] += 1
        if c[v+1] > 0:
            c[v+1] -= 1
        else:
            result += 1

    print(result)




if __name__ == "__main__":
    main()
