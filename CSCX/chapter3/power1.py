
def power(b, n):
    result = 1
    for _ in range(n):
        result = result*b
    return result

def power1():
    b,n = map(int,(input().split()))

    if 0 < b <= 9 and 0 < n <= 9:
        print(power(b,n))


if __name__ == "__main__":
    power1()