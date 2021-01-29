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

if(is_Hungry == True):
  print("You should go eat.")
if(is_Sleepy == True):
  print("You should go sleep.")
if (is_Sleepy == False):
  print("Wow, you're well rested.")
else:
  print("Wow you're well fed.")
  
# Ask the user for a number 
# Tell the user if the number is even or odd

even_odd = int(input("Type in a number: "))

if (even_odd%2 != 0):
  print("Your number is odd.")
elif (even_odd%2 == 0):
  print("Your number is even.")
else:
  print("N/A")
