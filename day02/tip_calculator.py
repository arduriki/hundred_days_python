#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill?\n$ "))
tip_to_give = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
tip_percentage = 1 + (tip_to_give / 100)
people_to_split_bill = int(input("How many people to split the bill?\n"))
bill_per_person = bill_amount * tip_percentage / people_to_split_bill
print(f"Each person should pay: ${bill_per_person:.2f}")
