import sys

MAPPING = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\/[]',
    'n': '[]\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': "']['",
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '}{',
    'y': '`/',
    'z': '2',
}





def main():
    lines = sys.stdin.read().splitlines()
    text = lines[0]

    for c in text:
        try:
            print(MAPPING[c.lower()], end="")
        except KeyError:
            print(c, end="")
    print("")




if __name__ == "__main__":
    main()
