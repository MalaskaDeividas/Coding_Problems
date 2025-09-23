
def inc(x):
    y = x + 1
    return y

def inc1():
    string = input()
    x = int(string)

    if 0 <= x <= 100000:
        y = inc(x)
        print(y)
    else:
        return

if __name__ == "__main__":
    inc1()