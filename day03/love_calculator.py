print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true_word = "true"
love_word = "love"

score_true = 0
score_love = 0

name1 = name1.lower()
name2 = name2.lower()

for name_letter in name1:
    for true_letter in true_word:
        if name_letter == true_letter:
            score_true += 1
    for love_letter in love_word:
        if name_letter == love_letter:
            score_love += 1

for name_letter in name2:
    for true_letter in true_word:
        if name_letter == true_letter:
            score_true += 1
    for love_letter in love_word:
        if name_letter == love_letter:
            score_love += 1

total_score = int(str(score_true) + str(score_love))

if total_score < 10 or total_score > 90:
    print(f"Your score is {
          total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

"""-------------
ANOTHER SOLUTION
-------------"""

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
