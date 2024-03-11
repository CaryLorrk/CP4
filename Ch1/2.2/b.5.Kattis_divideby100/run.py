import sys


def main():
    lines = sys.stdin.read().splitlines()
    len1 = len(lines[0])
    len2 = len(lines[1])
    if len2 > len1:
        print(f"{0}.{'0'*(len2-len1-1)}{lines[0].rstrip('0')}")
    else:
        l = len(lines[0]) - len(lines[1]) + 1
        result = f"{lines[0][0:l]}.{lines[0][l:]}".rstrip('0')

        if result[-1] == '.':
            result = result[:-1]
        print(result)



if __name__ == "__main__":
    main()
