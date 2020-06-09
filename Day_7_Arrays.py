# Link to the complete Problem Statement: https://www.hackerrank.com/challenges/30-arrays/problem

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr = arr[::-1]
    for a in arr:
        print(a, end = " ")

