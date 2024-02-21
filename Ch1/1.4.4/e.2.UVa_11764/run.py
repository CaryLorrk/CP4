import sys

def main():
    lines = sys.stdin.read().splitlines()
    n_case = int(lines[0])
    lines = lines[1:]

    for n in range(n_case):
        high_jump = 0
        low_jump = 0
        walls = lines[1].split()
        for i in range(len(walls) - 1):
            if int(walls[i]) > int(walls[i+1]):
                low_jump = low_jump + 1
            elif int(walls[i]) < int(walls[i+1]):
                high_jump = high_jump + 1
        print("Case {}: {} {}".format(n+1, high_jump, low_jump))
        lines = lines[2:]

if __name__ == "__main__":
    main()
