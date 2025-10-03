

def swap1():
    string = input()
    n, s = string.split()
    n = int(n)
    
    if len(s) <= 30 and 0 <= n <= 1000:
        print(f"{s} {n}")
    else:
        return

if __name__ == "__main__":
    swap1()