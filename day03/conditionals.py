water_level = 50

if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# ----------------------

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    # if-block code
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    # nesting
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    # elif statement:
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    # Add another 'if' statement.
    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo.upper() == "Y":
        bill += 3
    # If the answer is 'N', not necessarily to add an 'else' statement.
    print(f"Your final bill is ${bill}.")

else:
    # else-block code
    print("Sorry, you have to grow taller before you can ride.")

# -----------------------

