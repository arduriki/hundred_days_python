target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total_number = 0
for number in range(0, target+1, 2):
    total_number += number

print(total_number)

"""-----------
OTHER SOLUTION
-----------"""

alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)
