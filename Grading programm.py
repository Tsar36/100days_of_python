student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail" 

# 🚨 Don't change the code below 👇
print(student_grades)

# Dictionary

dictionary = {"Bug": "An error", "Function": "a pice of code", "Loop": "the action of doing smth over and over again"}
# print(dictionary["Loop"])

# Adding a new  item - key:Value to the existing dictionary:

dictionary["print"] = "show the output of smth"
# print(dictionary["Bug"])

# create a new empty dictionary:

new_dictionary = {}

# Wipe an existing dictionary:

# dictionary = {}
# print(dictionary)

# Edit an item in a dictionary:

dictionary["Bug"] = "it is a feature :)"
# print(dictionary["Bug"])

# Example of usage:
for key in dictionary:
  print(key) # prints only keys
  print(dictionary[key]) # prints only values