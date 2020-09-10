# Write a function that take in an array of integers and returns a boolean representing whether the array is monotonic
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entire non-decreasing
# Note that empty arrays and arrays of one element are monotonic

# Sample input array = [-1, -5, -10, -1100, -1101, -1102, -9001]
# Sample output is true

def isMonotonic(array):
    array.sort() #-9001, -1102, -1101, -1100, -10, -5, -1
    

print(isMonotonic([-1, -5, -10, -1100, -1101, -1102, -9001]))