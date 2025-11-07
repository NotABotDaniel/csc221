x = 0
y = 0
while True:
    for h in range(5):
        for w in range(20):
            if w == x and h == y:
                print("X", end="")
            else:
                print("_", end="")
        print("")
    i = str(input(""))
    print("*" * 20)
    if i == "w":
        y -= 1
    elif i == "s":
        y += 1
    elif i == "a":
        x -= 2
    elif i == "d":
        x += 2
    