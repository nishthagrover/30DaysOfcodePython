# Link to the complete Problem Statement: https://www.hackerrank.com/challenges/30-inheritance/problem

# Solution

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    sum = 0

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores       

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        
        for i in self.scores:
            self.sum += i
        self.sum /= len(scores)
        
        if self.sum >= 90:
            grade = "O"
            return grade
        
        if self.sum >= 80:
            grade = "E"
            return grade
        
        if self.sum >= 70:
            grade = "A"
            return grade
        
        if self.sum >= 55:
            grade = "P"
            return grade
        
        if self.sum >= 40:
            grade = "D"
            return grade
        
        else:
            grade = "T"
            return grade
        
        return grade 

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

