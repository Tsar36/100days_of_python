print("Pizza Order")

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

# Pizza ordering:
if size == "S":
    bill += 15
    print("Small Pizza")
elif size == "M":
    bill += 20
    print("Medium Pizza")
else:
    bill += 25
    print("Large Pizza")

# Addons:

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

# The final bill:

print(f"Your final bill is ${bill}.")