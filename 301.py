for _ in range(2):
    a = int(input())
    b = int(input())

    for x in range(1, a + 1):
        y = a - x
        if x * y == b:
            print(x, y)
            break
