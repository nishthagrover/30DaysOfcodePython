# Link to the complete Problem Statement: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Solution 

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n = int(input())

    phone = {}

    for i in range(n):
        name, number = input().split(" ")
        phone[name] = int(number)
   
    while True:
        try:
            name = input()
            if name in phone:
                print(name, "=", phone[name], sep="")
            else: 
                print("Not found")   
        
        except: 
            break
