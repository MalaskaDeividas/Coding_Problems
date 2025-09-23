



def equilateral(x,y,z):
    if x==y==z:
        return True
    else:
        return False


def isosceles(x,y,z):
    if (x == y and x != z) or (x == z  and x != y) or (y == z and y != x):
        return True
    else:
        return False

def scalene(x,y,z):
    if (x != y and x != z and y != z):
        return True
    else:
        return False

def impossible(x,y,z):
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        return True
    else:
        return False


def main():

    x,y,z = map(int,input().split())

    if 0 < x < 100 and 0 < y < 100 and 0 < z <100:
        if impossible(x,y,z):
            print("impossible")
        elif equilateral(x,y,z):
            print("equilateral")
        elif isosceles(x,y,z):
            print("isosceles")
        elif scalene(x,y,z):
            print("scalene")
        else:
            print("impossible")





if __name__ == "__main__":
    main()