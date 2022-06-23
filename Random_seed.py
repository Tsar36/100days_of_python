print('''Randomisation and Python Lists''')

import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)

# # 0.000000 to 0.9999999...
# randomFloat = random.random()
# print(randomFloat)

'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
e.g. 1 means Heads 0 means Tails
'''

randomSide = random.randint(0, 1)

if randomSide == 1:
  print("Heads")
else:
  print("Tail")


# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")