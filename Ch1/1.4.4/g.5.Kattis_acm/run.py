import sys

def main():
    lines = sys.stdin.read().splitlines()

    acc_times = [0] * 26
    statuses = [0] * 26

    total_time = 0
    total_count = 0

    for line in lines:
        line = line.split()
        if line[0] == '-1':
            break
        t = int(line[0])
        problem = ord(line[1]) - ord('A')
        status = line[2]
        if status == 'right':
            total_time = total_time + acc_times[problem] + t
            total_count = total_count + 1
        else:
            acc_times[problem] = acc_times[problem] + 20

    print(total_count, total_time)


            


if __name__ == "__main__":
    main()
