#!/usr/bin/env python3

def is_prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

for n in range(200):
    if is_prime(n) and is_prime(sum(int(d)**len(str(n)) for d in str(n))):
        print(n, end=' ')


# 2 3 5 7 11 23 41 61 83 101 113 131 139 151 193 199 
#            ^^
#
# Inspiration from http://oeis.org/A052034
