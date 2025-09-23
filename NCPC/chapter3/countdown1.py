


def countdown(n):
    number = n
    for i in range(n, 0, -1):
        print(i)
        
    print("Go!")

def countdown1():
    n = int(input())
    countdown(n)


if __name__ == "__main__":
    countdown1()         