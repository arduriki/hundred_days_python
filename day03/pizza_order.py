print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size.upper() == "S":
    bill += 15
    if add_pepperoni.upper() == "Y":
        bill += 2
    if extra_cheese.upper() == "Y":
        bill += 1
elif size.upper() == "M":
    bill += 20
    if add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1
else:
    bill += 25
    if add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1

print(f"Your final bill is: ${bill}.")

# Another way to solve it:
bill = 0

if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
