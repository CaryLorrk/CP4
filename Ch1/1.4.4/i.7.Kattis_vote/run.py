import sys


def main():
    lines = sys.stdin.read().splitlines()
    n_case = int(lines[0])

    i = 1
    while i < len(lines):
        n_candidates = int(lines[i])

        highest_votes = -1
        highest_candidate = -1
        second_votes = -1
        total_votes = 0
        
        for n, vs in enumerate(lines[i+1:i+n_candidates+1]):
            v = int(vs)
            total_votes = total_votes + v
            if v > highest_votes:
                highest_votes = v
                highest_candidate = n + 1
            elif v == highest_votes:
                second_votes = v

        if highest_votes == second_votes:
            print("no winner")
        else:
            prefix = "minority"
            if highest_votes > (total_votes - highest_votes):
                prefix = "majority"
            print(prefix, "winner", highest_candidate)




        i = i + n_candidates + 1



if __name__ == "__main__":
    main()
