# Link to the complete Problem Statement: https://www.hackerrank.com/challenges/30-loops/problem

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
        print(n,"x",i,"=",(i*n))
