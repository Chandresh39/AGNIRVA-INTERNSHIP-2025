# Python script to check if a number is even or odd

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Use modulus operator to determine if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")