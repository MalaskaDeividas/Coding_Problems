def mult(x,y,z):
    v = x*y*z
    return v

def mult1():
    string = input()
    x,y,z = string.split()
    x,y,z = int(x), int(y), int(z)

    if 0<= x <= 999 and 0<= y <= 999 and 0<= z <= 999:
        v = mult(x,y,z)
        print(v)
    else:
        return


if __name__ == "__main__":
    mult1()