#Sorting a list of numbers in ascending order:
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)  # Output: [10, 20, 30, 40, 50]


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if a swap occurred on this pass
        swapped = False
        for j in range(n - i - 1):  # Reduce the comparison length each iteration
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

# Example usage
numbers = [50, 20, 40, 10, 30]
bubble_sort(numbers)
print("Sorted list:", numbers)  # Output: [10, 20, 30, 40, 50]
