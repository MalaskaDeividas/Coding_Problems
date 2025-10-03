



def main():
    n = int(input())

    total = 0

    for _ in range(n):
        x = int(input())
        if 0 <= x <= 100000:
            total += x
    print(total)

if __name__ == "__main__":
    main()



    