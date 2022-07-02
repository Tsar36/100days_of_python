# Functions ---------------------------------------

def name_of_function():
  # Do this
  print("Hello")
  # Then do this
  num_char = len("Hello")
  # Finally DO this
  print(num_char)
  
# Calling the function
name_of_function()

# Reborg challenge

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

for step in range(6):  # from 0 to 5
  jump()
# while not at_goal():
# jump()

# WHILE -------------------------------------------

while something_is_true:
#  Do something repeatedly

# Reborg challenge - 2

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  while on_right():
    move()
  turn_left()
  move()
  turn_right()
  while front_is_clear():
    move()
  turn_right()
  move()
  turn_left()
while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()
  
#for step in range(6):  # from 0 to 5
#  jump()

# Functions with inputs
# Arguments and Parrametters


# --- The simple function:

# def greet():
#   print("Hello")
#   print("mam's")
#   print("coders")
# greet()

# --- The simple function with input:

# def greet_with_input(name):
#   print(f"Hello {name}")
#   print(f"{name} is a mam's coder :)")
# greet_with_input("Serhii")

# --- Function with more then 1 inputs:

def greet(name, location):
  print(f"Hello {name}")
  print(f"your location is {location}")
greet(name="Serhii", location="Lviv")