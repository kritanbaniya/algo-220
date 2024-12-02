import matplotlib.pyplot as plt

# Sample data for demonstration
arraysizes = [2, 16, 64, 256, 1024, 4096]  # Example sizes of arrays
runtime_heap = [0.01, 0.05, 0.1, 0.5, 1.5, 19.0]  # Example runtimes for heap sort (in seconds)
runtime_python = [0.005, 0.03, 0.08, 0.4, 1.0, 18.0]  # Example runtimes for Python's built-in sort (in seconds)

# Create the plot
plt.figure(figsize=(12, 6))  # Wider figure for better clarity

# Plotting the data
plt.plot(arraysizes, runtime_heap, marker='o', label='Heap Sort', color='blue')
plt.plot(arraysizes, runtime_python, marker='o', label='Python Sort', color='orange')

# Adding titles and labels
plt.title('Runtime Comparison of Heap Sort vs Python Sort')
plt.xlabel('Array Size')
plt.ylabel('Runtime (milliseconds)')
plt.xticks(arraysizes)  # Set x-ticks to the values in array_size
plt.yticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # Set y-ticks for clarity
plt.ylim(0, 20)  # Set y-axis limit from 0 to 20 ms
#plt.xscale('log')  # Use a logarithmic scale for x-axis
plt.grid()  # Optional: Add grid for better readability
plt.legend()  # Add legend

# Show the plot
plt.show()
