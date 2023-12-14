"""
4. Greatest Common Divisor Problem
Compute the greatest common divisor of two positive integers.
    Input: Two positive integers a and b.
    Output: The greatest common divisor of a and b.
Input format: Integers a and b (separated by a space).
Output format: GCD(a,b)
Sample:
    Input: 28851538 1183019
    Output: 17657

"""

import os
for i in os.listdir():
    if i[1]=='.':
        os.rename(i, i.replace('  ', ' '))