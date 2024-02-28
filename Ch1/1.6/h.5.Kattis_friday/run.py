import sys


def main():
    lines = sys.stdin.read().splitlines()
    T = int(lines[0])
    lines = lines[1:]
    for t in range(T):
        D, M = [int(x) for x in lines[0].split()]
        lines = lines[1:]
        d = [int(x) for x in lines[0].split()]
        lines = lines[1:]
        
        day_of_week = 0
        count = 0
        for m in range(M):
            for day_of_month in range(1, d[m]+1):
                if day_of_month == 13 and day_of_week ==5:
                    count += 1
                day_of_week = (day_of_week + 1) % 7
        print(count)


if __name__ == "__main__":
    main()
