fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)  # prints the item of the list
    print(fruit + " pie")
# indentation is really important
print(fruits)  # print the list after the for loop

# empty list
numbers = []
# For loop with range
for number in range(1, 11):
    print(number)
    # add to a list
    numbers.append(number)
print(numbers)

# Add step
for number in range(1, 11, 3):
    # jumps every three numbers
    print(number)

total = 0
for number in range(1, 101):
    # add
    total += number
print(total)
