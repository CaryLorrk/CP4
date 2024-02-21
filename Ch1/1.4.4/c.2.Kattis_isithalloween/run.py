import sys

def main():
    lines = sys.stdin.read().splitlines()
    m, d = lines[0].split()
    if (
        (m == 'OCT' and d == '31')
        or (m == 'DEC' and d == '25')
    ):
        print('yup')
    else:
        print('nope')

if __name__ == "__main__":
    main()
