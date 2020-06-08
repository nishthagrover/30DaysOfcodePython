# Link to the complete Problem Statement: https://www.hackerrank.com/challenges/30-review-loop/problem

# Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    test = int(input())
    for i in range(test):
        s = input()
        
        for i in range (len(s)):
            if i%2 == 0:
                print(s[i],sep = "", end = "")
        
        print(" ",sep = "", end = "")

        for i in range (len(s)):
            if i%2 == 1:
                print(s[i],sep = "", end = "")
        
        print("")
