
d = int(input("Enter value for d: "))
t = int(input("Enter value for t: "))

days = 1
while d <= t:
    d += d * 0.1
    days += 1

print(f"{d:.2f} km, {days} days")
