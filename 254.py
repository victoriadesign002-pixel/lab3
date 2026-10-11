d, t = map(float, input().split())

total = d
days = 1

while total <= t:
    d *= 1.1
    total += d
    days += 1

print(f"{total:.2f} km, {days} days")
