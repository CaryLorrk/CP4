import sys
import operator


def main():
    lines = sys.stdin.read().splitlines()

    N = int(lines[1])

    
    answers = [line.split(', ') for line in lines[2:N+2]]


    diffs = [[0] * N for _ in range(N)]

    for n in range(N):
        for m in range(n+1, N):
            for x in range(len(answers[n])):
                if answers[n][x] != answers[m][x]:
                    diffs[n][m] += 1
                    diffs[m][n] += 1

    costs = [max(row) for row in diffs]
    min_value = min(costs)
    for n, v in enumerate(costs):
        if v == min_value:
            print(lines[n+2])




if __name__ == "__main__":
    main()
