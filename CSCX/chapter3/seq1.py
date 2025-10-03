




def seq(a,b):
    
    for i in range(a,b + 1):
        print(i)


def seq1():
    a,b = map(int, input().split())

    if -999 <= a <= b <= 999:
        seq(a,b)

if __name__ == "__main__":
    seq1()