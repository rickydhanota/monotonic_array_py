# Write a function that take in an array of integers and returns a boolean representing whether the array is monotonic
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entire non-decreasing
# Note that empty arrays and arrays of one element are monotonic

# Sample input array = [-1, -5, -10, -1100, -1101, -1102, -9001]
# Sample output is true

def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array [i] < array[i-1]:
            isNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing


print(isMonotonic([-1, -5, -10, -1100, -1101, -1102, -9001]))