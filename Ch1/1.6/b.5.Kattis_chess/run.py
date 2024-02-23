import sys


def move(x, y, x_offset, y_offset):
    if not (ord('A') <= x+x_offset <= ord('H') and 1 <= y+y_offset <= 8):
        return set()
    return {(x+x_offset, y+y_offset)} | move(x+x_offset, y+y_offset, x_offset, y_offset)
        


def list_all_available(x, y):
    result = set()
    result = result.union(move(x, y, 1, 1))
    result = result.union(move(x, y, 1, -1))
    result = result.union(move(x, y, -1, -1))
    result = result.union(move(x, y, -1, 1))
    return result



def search(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return f"0 {chr(x1)} {y1}"

    if ((x1+y1) % 2) != ((x2+y2)%2):
        return 'Impossible'

    if abs(x1-x2) == abs(y1-y2):
        return f"1 {chr(x1)} {y1} {chr(x2)} {y2}"
    intersection = list_all_available(x1, y1) & list_all_available(x2, y2)
    if intersection:
        xm, ym = (next(iter(intersection)))
        return f"2 {chr(x1)} {y1} {chr(xm)} {ym} {chr(x2)} {y2}"
    return 'Impossible'



def main():
    lines = sys.stdin.read().splitlines()

    for line in lines[1:]:
        x1, y1, x2, y2 = line.split()
        print(search(ord(x1), int(y1), ord(x2), int(y2)))

if __name__ == "__main__":
    main()
