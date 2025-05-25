# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Initialize a counter for even numbers
count = 0

# Loop through each number in the list
for num in numbers:
    # Check if the current number is even
    if num % 2 == 0:
        count += 1  # Increment the count if the number is even

# Print the total count of even numbers
print("Even numbers count:", count)