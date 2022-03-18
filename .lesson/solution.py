# Title: N5 Assignment 2018-19
# Date: 19 Jan 2019
# Author: Mr Friend

# import random module
import random

# Declare list and variables
endings = ["ing", "end", "axe", "gex", "goh"]
endingsIndex = 0
noOfStudents = 0
studentName = ""
studentUsername = ""

# Get the number of students
noOfStudents = int(input("Enter the number of students: "))

# Loop for the number of students
for student in range(noOfStudents):
    
    # Get the first 3 letters of the students name
    studentName = input("Enter first 3 letters of the students name: ")
    
    # Check length of student name
    while len(studentName) != 3:
        studentName = input("Enter a valid response.  First 3 letters of the students name: ")
    
    # Generate a random number
    endingsIndex = random.randint(0, 4)
    
    # Generate username
    if endingsIndex == 0:
        studentUsername = studentName + endings[0]
    
    if endingsIndex == 1:
        studentUsername = studentName + endings[1]
    
    if endingsIndex == 2:
        studentUsername = studentName + endings[2]
    
    if endingsIndex == 3:
        studentUsername = studentName + endings[3]
    
    if endingsIndex == 4:
        studentUsername = studentName + endings[4]
    
    # Display username
    print("Username: " + studentUsername)

