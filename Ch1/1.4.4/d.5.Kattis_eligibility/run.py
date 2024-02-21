import sys
import datetime as dt

date_convert = lambda s: dt.datetime.strptime(s, '%Y/%m/%d').date()

def check(post_secondary_date, birth_date, n_courses):
    if post_secondary_date >= dt.date(2010, 1, 1):
        return "eligible"
    if birth_date >= dt.date(1991, 1, 1):
        return "eligible"
    if n_courses >= 41:
        return "ineligible"
    return "coach petitions"

def main():
    lines = sys.stdin.read().splitlines()
    for line in lines[1:]:
        name, post_secondary_date, birth_date, n_courses = (
            new_type(item)
            for item, new_type
            in zip(
                line.split(),
                (str,
                 date_convert,
                 date_convert,
                 int
                )
            )
        )
        print(name, check(post_secondary_date, birth_date, n_courses))

if __name__ == "__main__":
    main()
