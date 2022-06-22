print("Welcome to the rollercoaster!")

# Check the height for permitions to ride
height = int(input("What is your height in cm.?: "))
bill = 0

# Check the age to determine the price of tickets

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What's your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $ 5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $ 7")
  elif age >= 45 and age <= 55:
    print("Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $ 12")
    
# Addons:
    
  wants_photo = input("Do you want a photo taken? Y or N: ")
  if wants_photo == "Y":
    # Add $3 to the bill
    bill += 3
  
  print(f"Your final bill is {bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")