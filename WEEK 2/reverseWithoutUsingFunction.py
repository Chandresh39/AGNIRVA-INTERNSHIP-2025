# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create an empty list to hold the reversed elements
reversed_numbers = []

# Loop through the original list in reverse order
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])

# Print the reversed list
print("Reversed list:", reversed_numbers)