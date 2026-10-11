import math

a = int(input())
b = int(input())

nsc = a * b // math.gcd(a, b)

print(nsc)
