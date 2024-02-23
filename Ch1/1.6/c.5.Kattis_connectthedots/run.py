import sys


def connect(lines, x1, y1, x2, y2):
    while True:
        if x1 > x2:
            x1 = x1 - 1
            if x1 == x2 and y1 == y2:
                break
            if lines[y1][x1] in ('.', '-'):
                new_line = list(lines[y1])
                new_line[x1] = '-'
                lines[y1] = ''.join(new_line)
            elif lines[y1][x1] == '|':
                new_line = list(lines[y1])
                new_line[x1] = '+'
                lines[y1] = ''.join(new_line)

        if x2 > x1:
            x1 = x1 + 1
            if x1 == x2 and y1 == y2:
                break
            if lines[y1][x1] in ('.', '-'):
                new_line = list(lines[y1])
                new_line[x1] = '-'
                lines[y1] = ''.join(new_line)
            elif lines[y1][x1] == '|':
                new_line = list(lines[y1])
                new_line[x1] = '+'
                lines[y1] = ''.join(new_line)

        if y1 > y2:
            y1 = y1 - 1
            if x1 == x2 and y1 == y2:
                break
            if lines[y1][x1] in ('.', '|'):
                new_line = list(lines[y1])
                new_line[x1] = '|'
                lines[y1] = ''.join(new_line)
            elif lines[y1][x1] == '-':
                new_line = list(lines[y1])
                new_line[x1] = '+'
                lines[y1] = ''.join(new_line)
        if y2 > y1:
            y1 = y1 + 1
            if x1 == x2 and y1 == y2:
                break
            if lines[y1][x1] in ('.', '|'):
                new_line = list(lines[y1])
                new_line[x1] = '|'
                lines[y1] = ''.join(new_line)
            elif lines[y1][x1] == '-':
                new_line = list(lines[y1])
                new_line[x1] = '+'
                lines[y1] = ''.join(new_line)

def process(lines):
    positions = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if '0' <= c <= '9':
                positions[ord(c) - ord('0')] = (x, y)
            if 'a' <= c <= 'z':
                positions[ord(c) - ord('a') + 10] = (x, y)
            if 'A' <= c <= 'Z':
                positions[ord(c) - ord('A') + 50] = (x, y)

    keys = sorted(positions.keys())
    for n in range(len(keys)-1):
        connect(
            lines,
            positions[keys[n]][0],
            positions[keys[n]][1],
            positions[keys[n+1]][0],
            positions[keys[n+1]][1],
        )
    print('\n'.join(lines))

def main():
    lines = sys.stdin.read().splitlines()

    last_n = 0
    for n, line in enumerate(lines):
        if len(line) == 0:
            process(lines[last_n:n])
            last_n = n + 1
            print("")
    process(lines[last_n:])

if __name__ == "__main__":
    main()
