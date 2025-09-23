


def good(h):

    if 4 <= h <= 11:
        print("Good morning")
    elif 12 <= h <= 17:
        print("Good afternoon")
    elif 18 <= h <= 23:
        print("Good evening")
    else:
        print("Hi")


def good1():

    h = int(input())

    if 0<=h<24:
        good(h)




if __name__ == "__main__":
    good1()