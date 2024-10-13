# solve max subarray problem recursively 
import numpy as np
import matplotlib.pyplot as plt
import random
import time

def create_random_array(size, min_value, max_value):
    # Create an array of the specified size with random integers
    return [random.randint(min_value, max_value) for _ in range(size)]

def find_max_crossing_subarray(arr, left, mid, right):
    # Find maximum subarray in the left half
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    # Find maximum subarray in the right half
    right_sum = float('-inf')
    total = 0
    for j in range(mid + 1, right + 1):
        total += arr[j]
        right_sum = max(right_sum, total)

    # Return the sum of the maximum crossing subarray
    return left_sum + right_sum

def find_max_subarray(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    # Recursive case: divide the array
    mid = (left + right) // 2

    # Find the maximum subarray sum in three parts
    left_max = find_max_subarray(arr, left, mid)
    right_max = find_max_subarray(arr, mid + 1, right)
    cross_max = find_max_crossing_subarray(arr, left, mid, right)

    # Return the maximum of the three
    return max(left_max, right_max, cross_max)

# to measure runtimes for different array sizes
arraysizes = [2, 4, 8, 16, 32, 64, 128]
runtimes = []


for i in arraysizes:
    curruntimes = [] 
    # Run 10 times for each array size to get average runtime
    for j in range(10):
        # Create an array with a specific size
        recarray = create_random_array(i, -50, 50)
        start_time = time.perf_counter()
        max_subarray_sum = find_max_subarray(recarray, 0, len(recarray) - 1)
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        curruntimes.append(elapsed_time)
    # Calculate average runtime
    average_runtime = sum(curruntimes) / len(curruntimes)
    runtimes.append(average_runtime)

# Plotting the results
plt.plot(arraysizes, runtimes, marker='o')
plt.title("Recursive Max Subarray Runtime")
plt.xlabel("Array Size")
plt.ylabel("Run Time (ms)")
plt.grid(True)
plt.show()
