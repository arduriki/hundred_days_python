age = int(input("How old are you?\n"))
weeks_in_year = 52
your_age_in_weeks = age * weeks_in_year
ninety_year_old_weeks = 90 * 52
your_weeks_left = ninety_year_old_weeks - your_age_in_weeks
print(f"You have {your_weeks_left} weeks left.")