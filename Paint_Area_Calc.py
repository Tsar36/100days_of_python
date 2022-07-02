# --- Paint Area Calculation ---:
'''
The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
number of cans = (wall height ✖️ wall width) ÷ coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 ✖️ 4) ÷ 5
                     = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

'''
#Write your code below this line 👇


import math                                   # for round of cans, we can't buy 1,6 cans example...

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)             # Using the 'math.ceil module' to round 
    print(f"You'll need {cans} cans of paint")


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)