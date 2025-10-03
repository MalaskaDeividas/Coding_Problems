


def hello(n):

    for _ in range(n):
        print("Hello, World!")

def hello2():

    n = int(input())

    if 1 <= n <= 1000:
        hello(n)



if __name__ == "__main__":
    hello2()
