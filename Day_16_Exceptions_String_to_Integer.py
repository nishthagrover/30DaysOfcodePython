# Link to the complete problem statement: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
#solution

import sys

S = input().strip()
try:
    print(int(S))
except:
    print("Bad String")
    
