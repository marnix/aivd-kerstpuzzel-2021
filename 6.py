#!/usr/bin/env python3

from fractions import Fraction

opgave = [
        4.5, 0.5, 2, 18, 0.5625, 20.25, 10.125, 364.5, 182.25, 6561, 2916, 1458, 648, 324, 144,
    ]

for x in opgave:
    # powers of 2 and 3 in x, assume no negative powers of 3
    p2 = 0
    while x != int(x): p2 -= 1; x *= 2
    while x%2 == 0: p2 += 1; x //= 2
    p3 = 0
    while x%3 == 0: p3 += 1; x //= 3
    assert x == 1
    print('2**{:2} * 3**{:2}'.format(p2, p3))
