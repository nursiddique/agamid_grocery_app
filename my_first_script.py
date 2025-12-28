# my_first_script.py
# Exercise 1: Calculation
# This script calculates the total cost of items in a shopping cart
# and prints the result to the console.

milk = 2
bread = 1
egg = 4
total_cost = milk + bread + egg
print("Total cost of items:", total_cost)

# Exercise 2: String Manipulation
# This script takes a user's name as input and prints a greeting message.

user_name = input("Enter your name: ") # Get user input for name
greeting_message = "Hello, " + user_name + "! Welcome to the program." # Create greeting message
print(greeting_message) # Print the greeting message to the console

# Exercise 3: Common Errors
# The program has an error, find it and fix it

# milk = "3"
# bread = 2.5
# total = milk + bread
# print("The total cost is: $" + total) 

milk = "3"
bread = 2.5
total = float(milk) + bread
print("The total cost is: $" + str(total))
