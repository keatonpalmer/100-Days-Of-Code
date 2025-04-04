import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Mode

# Create string variable
user_password = ""

# For loop for number of letters and add to previously declared variable
for char in range(0, nr_letters):
    user_password += random.choice(letters)

# For loop for number of symbols add to previously declared variable
for char in range(0, nr_symbols):
    user_password += random.choice(symbols)

# For loop for number of numbers add to previously declared variable
for char in range(0, nr_numbers):
    user_password += random.choice(numbers)

# Output user password
print(user_password)

# Hard Mode

# Create empty list
password_list = []

# For loop for number of letters and add to previously declared variable
for char in range(0, nr_letters):
    user_password += random.choice(letters)

# For loop for number of symbols add to previously declared variable
for char in range(0, nr_symbols):
    user_password += random.choice(symbols)

# For loop for number of numbers add to previously declared variable
for char in range(0, nr_numbers):
    user_password += random.choice(numbers)

# Output characters of password in the format of the list
print(password_list)

# Randomly shuffles the passwords_list characters
random.shuffle(password_list)

# Output the shuffled characters
print(password_list)

# Create password string variable
password = ""

#  For loop to iterate through the password_list and add the char values
for char in password_list:
    password += char

#Output user password
print(f"Your password is: {password}")