# future_age_calculator.py
# Ask the user for their current age and tell them how old they'll be in 2050.
# Assumes current year = 2023, so we add 27 years.

# Prompt user (note the space after the question mark as requested)
current_age = int(input("How old are you? "))

# Years to add from 2023 to 2050
years_until_2050 = 2050 - 2023  # 27

# Calculate age in 2050
age_in_2050 = current_age + years_until_2050

# Print result in the required format
print(f"In 2050, you will be {age_in_2050} years old.")