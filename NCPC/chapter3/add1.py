


def add(x,y):
    z = x + y
    return z

def add1():
    string = input()
    x,y = string.split()
    x,y = int(x), int(y)

    if 0<= x <= 100000 and 0<= y <= 100000:
        z = add(x,y)
        print(z)
    else:
        return


if __name__ == "__main__":
    add1()