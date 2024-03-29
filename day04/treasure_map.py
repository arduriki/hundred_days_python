import sys


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if int(position[1]) >= 1 and int(position[1]) <= 3:
    row = int(position[1]) - 1
    if position[0].lower() == "a":
        col = 0
    elif position[0].lower() == "b":
        col = 1
    elif position[0].lower() == "c":
        col = 2
    else:
        print("Sorry, write the correct input.")
        sys.exit()
else:
    print("Sorry, write the correct input.")
    sys.exit()

map[row][col] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

"""-----------
OTHER SOLUTION
-----------"""

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"