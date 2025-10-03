

def volume(w, h, d):
    return w * h * d

def area(w, h, d):
    return 2 * (w*d + w*h + h*d)

def main():
    w, h, d = map(int, input().split())
    v = volume(w, h, d)
    a = area(w, h, d)
    print(f"The volume of a {w} by {h} by {d} box is {v}.")
    print(f"The surface area of a {w} by {h} by {d} box is {a}.")

if __name__ == "__main__":
    main()