# Link To the complete Problem Statement: https://www.hackerrank.com/challenges/30-operators/problem
# Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost * float(tip_percent)/100
    tax = meal_cost * float(tax_percent)/100
    print(round(meal_cost + tip + tax))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
