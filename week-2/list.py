# List in Python:
my_list = [10, "Hello", True, 3.14]

print(my_list[1])  # Output: "Hello"


# Inserting Elements
# use append():
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)  # Output: [10, 20, 30, 40]


# use insert():
numbers.insert(1, 15)

print(numbers)  # Output: [10, 15, 20, 30, 40]


# Deleting Elements
# use remove():
numbers.remove(20)

print(numbers)  # Output: [10, 15, 30, 40]


# use pop():
numbers.pop(2)

print(numbers)  # Output: [10, 15, 40]


# Searching for an Element
# Use the in keyword to check if an element exists in a list:
print(15 in numbers)  # Output: True

# Find the index of an element using index():
print(numbers.index(15))  # Output: 1


# Traversing a List
for num in numbers:
    print(num)


# Sorting a List
# Use the sort() method to sort a list in ascending order:
numbers.sort()

print(numbers)  # Output: [7, 10, 25, 32, 50]


# Reversing a List
# Use the reverse() method to reverse the order of a list:
numbers.reverse()

print(numbers)  # Output: [50, 32, 25, 10, 7]


# List Comprehensions
# Create new lists using concise, Pythonic syntax:
squares = [x**2 for x in range(1, 6)]

print(squares)  # Output: [1, 4, 9, 16, 25]

