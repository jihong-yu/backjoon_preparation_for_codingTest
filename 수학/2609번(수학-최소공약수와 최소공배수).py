import math

x, y = map(int, input().split())

gcd = 0
lcm = 0

for i in range(1, min(x, y)+1):
    if x % i == 0 and y % i == 0:
        gcd = max(gcd, i)

lcm = gcd * (x//gcd) * (y//gcd)

print(gcd)
print(lcm)
