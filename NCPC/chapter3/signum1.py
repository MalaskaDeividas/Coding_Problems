

def signum1():

    x = int(input())

    if -100 <= x <= 100:
        if x == 0:
            print("zero")
        elif x < 0:
            print("negative")
        else:
            print("positive")

if __name__ == "__main__":
    signum1()