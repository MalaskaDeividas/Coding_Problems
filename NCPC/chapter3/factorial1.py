

def factorial(n):

    if n == 0 or n == 1:
        return 1
    else:
       return n*factorial(n-1)
    


def factorial1():
    n = int(input())

    if 0<= n < 10:
        print(factorial(n))


if __name__ == "__main__":
    factorial1()