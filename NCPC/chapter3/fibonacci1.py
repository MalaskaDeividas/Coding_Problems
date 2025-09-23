


def fibonacci(n):

    fn = 0
    if n == 0:
        fn = 0
    elif n == 1:
        fn = 1
    else:
        fn = fibonacci(n-1) + fibonacci(n-2)
    return fn



def fibonacci1():
    n = int(input())

    if 0<= n <=21:
        print(fibonacci(n))


if __name__ == "__main__":
    fibonacci1()