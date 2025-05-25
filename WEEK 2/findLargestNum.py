# Create a list of numbers
numbers = [10, 25, 7, 50, 32]

# Initialize the largest number as the first element
largest = numbers[0]

# Loop through the list to find the largest number
for num in numbers:
    if num > largest:
        largest = num

# Print the largest number
print("The largest number is:", largest)