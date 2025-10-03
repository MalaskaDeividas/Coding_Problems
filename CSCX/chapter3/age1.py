

def age1():
    string = input()
    n, a = string.split()
    a = int(a)
    

    if len(n) <= 30 and 0 <= a <= 180:
        print(f"{n} is {a} years old.")
    else:
        return

if __name__ == "__main__":
    age1()
