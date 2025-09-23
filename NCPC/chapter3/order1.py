

def order(x,y):
    if x < y:
        return True
    else:
        return False

def order1():
    string = input()
    x,y    = string.split()
    x,y    = int(x), int(y)

    if order(x,y) == 1:
        print("Yes")
    else: 
        print("No")

if __name__ == "__main__":
    order1()