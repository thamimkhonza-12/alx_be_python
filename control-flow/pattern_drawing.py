# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")

    # Print a newline to move to the next row
    print()

    # Move to the next row
    row += 1