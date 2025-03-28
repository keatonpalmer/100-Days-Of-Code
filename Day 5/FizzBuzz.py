# Create a loop for numbers 1 - 100

for number in range(1, 101):

    # Check to see if number is divisible by 3 and 5, and if so print "FizzBuzz"
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Check to see if number is divisible by 3, and if so print "Fizz"
    elif number % 3 == 0:
        print("Fizz")
    # Check to see if number is divisible by 5, and if so print "Buzz"
    elif number % 5 == 0:
        print("Buzz")
    # If not divisible by 3 or 5, print the number. I was missing the else statement initially, which resulted in the words "Fizz" and "Buzz" appearing in addition to the number
    else:
        print(number)