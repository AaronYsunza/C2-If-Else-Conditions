a = 200
b = 33

if (b > a):
  print("b is greater than a")
else:
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative

user_number = int(input("Input a positive or negative number: "))

if (user_number) > 0:
  print("Your number is a positive number.")
elif(user_number == 0):
  print("You entered 0.")
else:
  print("Your number is a negative number.")

# Ask the user for their age 
# If they are younger than 13, tell them they can only watch PG/G Movies
#If they are 13 and older but younger than 17, they can only watch PG-13/PG/G movies.
# If they are older than 17 they can watch all movies.

user_age = int(input("What is your age? "))

if (user_age) < 13:
  print("You can only watch PG and G Movies.")
elif 13 < (user_age) < 17:
  print("You can watch PG-13/PG/G Movies.")
else:
  print("You can watch all movies.")

is_Hungry = True
is_Sleepy = False
is_Bored = True
if(is_Hungry == True):
  print("You should go eat.")
if(is_Sleepy == True):
  print("You should go sleep.")
if (is_Sleepy == False):
  print("Wow, you're well rested.")

if(is_Hungry == is_Bored or is_Sleepy == is_Hungry):
  print("You should do your homework.")
else:
  print("You can play outside.")

if(is_Sleepy == is_Hungry and is_Hungry == is_Bored):
  if(is_Sleepy == is_Bored):
    print("It's nap time.")
else:
  print("It's time for bed.")

# Ask the user for a number 
# Tell the user if the number is even or odd

even_odd = int(input("Type in a number: "))

if (even_odd%2 != 0):
  print("Your number is odd.")
elif (even_odd%2 == 0):
  print("Your number is even.")
else:
  print("N/A")

# Math Quadrants
# Ask the user for an x and a y value

# Using a nested conditional, output which quadrant they are in

x = int(input("What's your X-axis? "))
y = int(input("what's your Y-axis? "))

if (x > 0 and y > 0):
  if (y > 0):
   print("It is in the first quadrant.")
  else:
    print("Your number is in the fourth quadrant.")
elif (x < 0):
  if (y < 0):
    print("It is in the third quadrant.")
  if(y > 0):
    print("Your number is in the second quadrant.")

# create an if statement using "and" or "or" for the third and second quadrant

if (x < 0 and y > 0):
  print("It is in the second quadrant")
elif (x < 0 and y < 0):
  print("It is in the third quadrant.")

# let the user know when they are on the x-axis or y-axis
# if we have +y or -y but x == 0
# "You are on the y-axis"
# if we have -x and +x but y == 0
# "You are on the x-axis"

if(x == 0 and y != 0):
  print("You are on the y-axis.")
if(x != 0 and y == 0):
  print("You are on the x-axis.")

# if x and y are 0, output the origin
if (x == 0 and y == 0):
  print("You're on the origon.")

# and, or
# and takes precedence over or
# "and" both coniditions have to be correct
# "or" only one of the conditions have to be correct

x = 5
y = 6
z = 7
if(x == 5 and y == 5 or z ==5):
  print("Yay")
else:
  print("Nay")

if(x == 5 or y == 5 and z == 5):
  print("Yay")
else:
  print("Nay")