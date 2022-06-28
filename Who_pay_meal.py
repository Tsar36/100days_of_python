import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

'''
The programm will randomly determine a person who will pay the bill :)
'''

# Get the total number of list names:

num_item = len(names)

# Genarate a random number between 0 and last item:

random_choice = random.randint(0, num_item - 1)
the_person_who_will_pay = names[random_choice]
print(the_person_who_will_pay + " is going to buy the meal today")

# the_person_who_will_pay = random.choice(names) # ------ the advanced way using 'choice()'
