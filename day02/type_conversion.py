num_char = len(input("What is your name?\n"))
# Type check
print(type(num_char)) # int

# Type change
num_char = str(num_char)
print("Your name has " + num_char + " characters.")

#-----------------------

a = float(123)
print(type(a)) # float
print(70 + float("100.5")) # sums the float
print(str(70) + str(100)) # concatenates the String
