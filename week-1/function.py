# Greeting Function
# Define the function 'greet' using the 'def' keyword
def greet():
    # Print a welcome message
    print("Hello! Welcome to the program.")

# Call the greet function to execute it
greet()


# Greeting Function with a Parameter
# Define a function 'greet_user' that takes one parameter, 'name'
def greet_user(name):
    # Print a personalized welcome message using the parameter
    print(f"Hello, {name}! Welcome to the program.")

# Call the greet_user function with the name 'Alex'
greet_user("Alex")


# Adding Two Numbers with a Function
# Define a function 'add_numbers' that takes two parameters, 'a' and 'b'
def add_numbers(a, b):
    # Return the sum of the parameters
    return a + b

# Call the add_numbers function with 3 and 5 as arguments
result = add_numbers(3, 5)

# Print the result of the addition
print("The sum is:", result)


# Calculating the Area of a Rectangle
# Define a function 'calculate_area' that takes two parameters, 'length' and 'width'
def calculate_area(length, width):
    # Calculate the area and store it in a local variable 'area'
    area = length * width
    # Return the calculated area to the caller
    return area

# Call the calculate_area function and print the result
print(calculate_area(10, 5))  # This will print the area of a rectangle with length 10 and width 5

# Attempting to print 'area' outside the function will result in an error because 'area' is a local variable
# print(area)  # Uncomment this line to see the NameError: name 'area' is not defined
