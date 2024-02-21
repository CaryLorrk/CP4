import sys
import math

def main():
    lines = sys.stdin.read().splitlines()
    p, a, b, c, d, n = (int(x) for x in lines[0].split())
    if n == 1:
        print(0)
        return

    price_func = lambda k: p*(math.sin(a*k+b)+math.cos(c*k+d)+2)
    prices = [price_func(n) for n in range(1, n+1)]

     
    max_decline = 0
    curr_highest = prices[0]

    for price in prices[1:]:
        if price > curr_highest:
            curr_highest = price
            continue
        curr_decline = curr_highest - price
        if (curr_decline) > max_decline:
            max_decline = curr_decline

    print(max_decline)

if __name__ == "__main__":
    main()
