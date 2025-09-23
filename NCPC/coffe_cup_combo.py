

def coffee():
    n = int(input())
    s = input().strip()

    #print(n)
    #print(s)
    awake   = 0
    coffees = 0

    for i in range(len(s)):
        val = int(s[i])
        if val == 1:
            awake  += 1
            coffees = 2
        elif val == 0 and coffees > 0:
            awake   += 1
            coffees -= 1
    print(awake)



if __name__ == "__main__":
    coffee()