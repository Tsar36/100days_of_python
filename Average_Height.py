# fruits = ["Apple", "Peach", "Pear"]
# for i in fruits:
#   print(fruits)
#   print(i + " Pie")


## --- Average Height Exercise -- using 'sum()' and 'len()'

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# total_heights = sum(student_heights)
# total_students = len(student_heights)
# average_heights = round(total_heights / total_students)

# print(average_heights)

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

total_students = 0
for student in student_heights:
    total_students += 1
print(total_students)

average_heights = round(total_heights / total_students)
print(average_heights)