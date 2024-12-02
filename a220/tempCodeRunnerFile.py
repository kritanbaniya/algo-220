plt.title('Runtime Comparison of Dijkstras vs Bellman Ford\'s Algorithims')
plt.xlabel('Graph size (by # of nodes)')
plt.ylabel('Runtime (milliseconds)')
plt.xticks(graph_sizes)  # Set x-ticks to the values in graph_sizes
plt.yticks()  # Set y-ticks for clarity
plt.ylim(0, 20)  # Set y-axis limit from 0 to 20 ms
#plt.xscale('log')  # Use a logarithmic scale for x-axis
plt.grid()  # Optional: Add grid for better readability
plt.legend()  # Add legend

# Show the plot
plt.show()