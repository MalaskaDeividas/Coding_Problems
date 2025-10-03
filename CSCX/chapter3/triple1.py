

def triple(x):
    y = x*3
    return y

def triple1():
    string = input()
    x = int(string)

    if 0 <= x <= 100000:
        y = triple(x)
        print(y)
    else:
        return

if __name__ == "__main__":
    triple1()