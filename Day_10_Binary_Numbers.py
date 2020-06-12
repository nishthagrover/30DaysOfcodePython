# Link to the complete problem statement: https://www.hackerrank.com/challenges/30-binary-numbers/problem

# Solution

import math
import os
import random
import re
import sys

# Appraoch : and operation of x and left shift x replaces one '1'  with zero from each set of consective ones.
# Number of iterations required to convert x to 0 using this process gives the maximum number of consecutive ones.

if __name__ == '__main__':
    x = int(input())
    i=0
    while (x!=0):
        x = (x & (x<<1))
        i += 1
    print(i)
    
