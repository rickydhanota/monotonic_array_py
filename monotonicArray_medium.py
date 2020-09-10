# Write a function that take in an array of integers and returns a boolean representing whether the array is monotonic
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entire non-decreasing
# Note that empty arrays and arrays of one element are monotonic

# Sample input array = [-1, -5, -10, -1100, -1101, -1102, -9001]
# Sample output is true


# O(n) time | O(1) space - where n is the length of the array
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array [i] < array[i-1]:
            isNonDecreasing = False #is not decreasing, meaning it is increasing
        if array[i] > array[i-1]:
            isNonIncreasing = False # is non increasing, meaning it is decreasing
    return isNonDecreasing or isNonIncreasing


# print(isMonotonic([-1, -5, -10, -1100, -1101, -1102, -9001]))
print(isMonotonic([1, 5, 10, 1100, 1101, 1102, 9001]))