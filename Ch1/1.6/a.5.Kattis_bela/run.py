import sys


def main():
    mapping = {
        "A": (11, 11),
        "K": (4, 4),
        "Q": (3, 3),
        "J": (20, 2),
        "T": (10, 10),
        "9": (14, 0),
        "8": (0, 0),
        "7": (0, 0),
    }
    lines = sys.stdin.read().splitlines()
    _, b = lines[0].split()
    print(
        sum(
            mapping[c[0]][0]
            if c[1] == b
            else mapping[c[0]][1]
            for c in lines[1:]
        )
    )


if __name__ == "__main__":
    main()
