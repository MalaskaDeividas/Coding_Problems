


def knot():

    a    = int(input())
    n1   = list(map(int,input().split()))[:a]
    n2   = list(map(int,input().split()))[:a]

    set1 = set(n1)
    set2 = set(n2)

    missing = set1 - set2
    if len(missing) == 1:
        missing = missing.pop()
        print(f"{missing}")
    



if __name__ == "__main__":
    knot()