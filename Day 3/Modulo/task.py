# You can wrap an input in an int() to change the data type to int

# Create variable, input, and change the data type of the input to an int
user_number = int(input("Please enter a number: "))

#  Mathematical operation to determine whether the user's input is even or odd
solution = user_number % 2

# if else statement to determine whether the number is even or odd
if solution == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")