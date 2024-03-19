import sys
import itertools

def run1(A):
    S = set(A)
    for i in A:
        if (7777 - i) in S:
            print('Yes')
            return
    print('No')


def run2(A):
    for n in range(1, len(A)):
        if A[n] == A[n-1]:
            print('Contains duplicate')
            return
    print('Unique')


def run3(A):
    stats = {}

    for x in A:
        stats[x] = stats.get(x, 0) + 1

    found = False
    for k, v in stats.items():
        if v > len(A)/2:
            print(k)
            found = True

    if not found :
        print(-1)




def run4(A):
    N = len(A)
    if N % 2 == 0:
        print(f"{A[N//2 - 1]} {A[N//2]}")
    else:
        print(f"{A[N//2]}")


def run5(A):
    print(' '.join(str(x) for x in A if 100 <= x <= 999))



def main():
    lines = sys.stdin.read().splitlines()

    N, t = [int(x) for x in lines[0].split()]
    A = sorted([int(x) for x in lines[1].split()])

    if t == 1:
        run1(A)
    if t == 2:
        run2(A)
    if t == 3:
        run3(A)
    if t == 4:
        run4(A)
    if t == 5:
        run5(A)


if __name__ == "__main__":
    main()
