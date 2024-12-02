# solve max subarray problem with brute force 
import numpy as np
import matplotlib.pyplot as plt
import random
import time

def create_random_array(size, min_value, max_value):
    # Create an array of the specified size with random integers
    return [random.randint(min_value, max_value) for _ in range(size)]

def max_subarray_bruteforce(arr):
    max_sum = float('-inf')  # Start with the smallest possible number
    # Loop over each possible starting point of the subarray
    for i in range(len(arr)):
        current_sum = 0
        # Loop over each possible ending point of the subarray
        for j in range(i, len(arr)):
            current_sum += arr[j]  # Add the current element to the sum
            # Update max_sum if we found a new maximum
            max_sum = max(max_sum, current_sum)
    return max_sum


arraysizes = [2,4,8,16,32,64,128]
runtimes = []
for i in arraysizes:
    curruntimes= []
    for j in range(10): ## do 10 runs of each array size and keep average runtime
        brutearray = create_random_array(i,-50,50)
        start_time = time.perf_counter()
        maxsubaray = max_subarray_bruteforce(brutearray)
        end_time = time.perf_counter()
        elapsedtime = (end_time - start_time) * 1000 # in miliseconds
        curruntimes.append(elapsedtime)
    average_runtime = sum(curruntimes) / len(curruntimes)
    runtimes.append(average_runtime)

plt.plot(arraysizes, runtimes, marker='o')

plt.title("BRUTE FORCE find max sub array")
plt.xlabel("Array size")
plt.ylabel("Run time (ms)")

# Show the graph
plt.grid()  
plt.show()