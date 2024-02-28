import sys


def main():
    lines = sys.stdin.read().splitlines()
    n_cases = int(lines[0])
    lines = lines[1:]

    for n in range(n_cases):
        r, b, m = lines[n].split()
        r = float(r)/100
        b = int(float(b)*1000)
        m = int(float(m)*1000)
        p = 0
        while b >= 5:
            i = int(b * r)
            if i % 10 >= 5:
                i -= i % 10 
                i += 10
            else:
                i -= i % 10
            p += 1
            b += i
            if b % 10 >= 5:
                b -= b % 10 
                b += 10
            else:
                b -= b % 10

            b -= m
            if p > 1200:
                break

        if p > 1200:
            print('impossible')
        else:
            print(p)

    

if __name__ == "__main__":
    main()
