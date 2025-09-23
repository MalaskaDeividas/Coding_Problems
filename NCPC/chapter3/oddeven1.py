

def oddeven(x):

    if x % 2 == 0:
        return True
    else:
        return False

def oddeven1():
    string = input()
    x      = int(string)

    if oddeven(x) == 1:
        print("even")
    else:
        print("odd")
    

if __name__ == "__main__":
    oddeven1()