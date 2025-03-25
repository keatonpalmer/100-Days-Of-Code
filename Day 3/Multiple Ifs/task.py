print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Create bill variable for int value
bill = 0

# Checks to see if customer height is greater than or equal to 120 cm
if height >= 120:
    print("You can ride the rollercoaster")

    # Asks the customer their age. Ticket price depends on how old the customer is
    age = int(input("What is your age? "))

    # If customer is 12 or under, their ticket is $5 and bill is set to 5
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")

    # else if customer is 18 or under, their ticket is $7 and bill is set to 7
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    # else they have to be an adult and their bill is $12 and bill is set to 12
    else:
        bill = 12
        print("Adult tickets are $12.")
    # Customer is asked if they want a photo taken
    wants_photo = input("Would you like to have your photo taken? Type y for Yes and n for No. ")

    # If customer enters y, 3 is added to their bill
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
