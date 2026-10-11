n = int(input())

for x in range(10, 100):
    a = x // 10
    b = x % 10
    s = a ** 2 + b ** 2

    if s % n == 0:
        print(x, end=" ")

print()

