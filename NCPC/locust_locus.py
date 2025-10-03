import math

# read how many pairs there are
k = int(input())

# keep track of the earliest year found
earliest_year = None

for _ in range(k):
    # read the data for this pair
    y, c1, c2 = map(int, input().split())

    # find the LCM of the two cycles
    gcd = math.gcd(c1, c2) # greatest common divisor
    lcm = (c1 * c2) // gcd #least common multiple

    # start checking years after the last known year
    year = y + lcm

    # keep moving forward until we reach at least 2022
    while year < 2022:
        year += lcm

    # update the earliest year if this one is smaller
    if earliest_year is None or year < earliest_year:
        earliest_year = year

# print the final answer
print(earliest_year)