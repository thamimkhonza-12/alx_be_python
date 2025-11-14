# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the reminder message
reminder_message = ""

# Match Case to handle priority levels
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' has an unrecognized priority level"

# Modify message based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message = f"Note: {reminder_message}. Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder_message)