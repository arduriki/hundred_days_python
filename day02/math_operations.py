addition = 3 + 5
subtract = 7 - 4
multiply = 3 * 2
division_float = 6 / 3
division_int = 6 // 3
exponent = 2 ** 2

"""
PRIORITIES -> PEMDAS -> Left & Right
Parentheses
Exponents
Multiplication
Division
Addition
Subtraction
"""

priority_demo = 3 * (3 + 3) / 3 - 3
# parentheses, multiplication, division, subtraction
print(priority_demo)

# Rounding numbers
rounded_number = round(2.6666666, 2)
print(rounded_number) # 2.67

# Shorthand maths
score = 0
score += 1 # score = score + 1
print(score) # 1
# f-strings
print(f"Your score is {score}")