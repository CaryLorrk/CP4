import sys
from datetime import date
from itertools import permutations


def main():
    lines = sys.stdin.read().splitlines()
    cases = permutations(lines[0].split('/'))
    valid_cases = []
    for case in cases:
        try:
            y = '2000'[:4-len(case[0])] + case[0]
            d = date(int(y), int(case[1]), int(case[2]))
        except ValueError:
            ...
        else:
            if date(2000, 1, 1) <= d <= date(2999, 12, 31):
                valid_cases.append(d)
    if valid_cases:
        print(min(valid_cases).strftime('%Y-%m-%d'))
    else:
        print(f"{lines[0]} is illegal")



if __name__ == "__main__":
    main()
