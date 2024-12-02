# Kritan Baniya, CSC 220 Algorithims, HW 4
#heap sort vs insertion
import numpy as np
import matplotlib.pyplot as plt
import random
import time

def create_random_array(size, min_value, max_value):
    # Create an array of the specified size with random integers
    return [random.randint(min_value, max_value) for _ in range(size)]

# Function to maintain the max-heap property
def Max_heapify(array, index, heap_size):
    largest = index
    left = 2 * index + 1  # Left child index
    right = 2 * index + 2 # Right child index  ## is +1 and +2 because it is indexed from 0 not 1

    # Check if left child is larger than root
    if left < heap_size and array[left] > array[largest]:
        largest = left

    # Check if right child is larger than the current largest
    if right < heap_size and array[right] > array[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != index:
        array[index], array[largest] = array[largest], array[index]  # Swap
        Max_heapify(array, largest, heap_size)  # Recursively heapify the affected subtree

# Function to build a max-heap from an unsorted array
def Build_max_heap(array):
    heap_size = len(array)
    # Start from the last non-leaf node and heapify each node
    for i in range(heap_size // 2 - 1, -1, -1):
        Max_heapify(array, i, heap_size)

# Function to perform heap sort
def Heapsort(array):
    Build_max_heap(array)
    heap_size = len(array)

    # Extract elements one by one from the heap
    for i in range(heap_size - 1, 0, -1):
        # Move current root to the end
        array[0], array[i] = array[i], array[0]
        # Call Max_heapify on the reduced heap
        Max_heapify(array, 0, i)
    
    return array  # Return the sorted array

def insertion_sort(lst):  ## insersion sort to compare
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]  # Swap elements
            j -= 1  # Move left in the list
    return lst  # Return the sorted list


arraysizes = list(range(4, 4097, 64)) ## array sizes increases by 64, but each array size is tested 3 times for a average of 3
runtimes_heap = []
runtimes_inserstion = []

for i in arraysizes:
    #print(f"currently on: {i}")
    current_runtimes_heap= []
    current_runtimes_insertion = []
    for j in range(3): ## do 3 runs of each array size and keep average runtime
        
        random_array = create_random_array(i,-5000,5000) ## creating random filled array
        random_array_py = random_array.copy()  ### this one will be used for insersion sorting method // copying so same arry is sorted
        
        # heap sorting and measuring time
        start_time = time.perf_counter()
        heapsortarray = Heapsort(random_array)
        end_time = time.perf_counter()
        elapsedtime = (end_time - start_time) * 1000 # in miliseconds
        current_runtimes_heap.append(elapsedtime)
        
        ##insersion sort runtime and measuring time
        # start_time_py = time.perf_counter()
        # py_sort_array = insertion_sort(random_array_py)
        # end_time_py = time.perf_counter()
        # elapsedtime_py = (end_time_py - start_time_py) * 1000 # in miliseconds
        # current_runtimes_insertion.append(elapsedtime_py)
        
    T_runtime = sum(current_runtimes_heap) / 5 ## average run times for heap sort
    #Py_runtime = sum(current_runtimes_insertion) / 5 ## average run times for insersion sort
    runtimes_heap.append(T_runtime)
    #runtimes_inserstion.append(Py_runtime)
    
    
plt.figure(figsize=(15, 6)) 

# Plotting the data
plt.plot(arraysizes, runtimes_heap, marker='o', label='Heap Sort', color='blue')
#plt.plot(arraysizes, runtimes_inserstion, marker='o', label='Insersion Sort', color='orange')

# Adding titles and labels
plt.title('Runtime Comparison of Heap Sort') # vs Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Runtime (milliseconds)')
plt.xticks(arraysizes) 
plt.grid() 
plt.legend()

# Show the plot
plt.show()

