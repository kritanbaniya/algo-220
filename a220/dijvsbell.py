import matplotlib.pyplot as plt
import time
from randgraph import generate_sparse_graph, generate_dense_graph
from bellmanford1 import bellman
from dijkstras1 import dijkstra


graph_sizes = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]

# rt_dijkstra_dense = []                                      ##[1,2,3,4,5,6,7,8,9,10]
# rt_dijkstrs_sparse = []                                     ##[2,3,4,5,6,7,8,9,10,11]

# rt_bellmanford_dense = []                                   ##[3,4,5,6,7,8,9,10,11,12]
# rt_bellmanford_sparse = []                                  ##[4,5,6,7,8,9,10,11,12,13]


#########################################################################################################
## tests for dijkstra and bellmanford on random dense graphs 
# for i in graph_sizes:
#     currruntimes_dj = [] 
#     currruntimes_bf = [] 
    
    
    
#     for _ in range(3):  ## 3 trials for each graph size
#         graph_dense = generate_dense_graph(i)
        
#         start_time = time.perf_counter()
        
#         returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
#         end_time = time.perf_counter()
#         elapsed_time = (end_time - start_time) * 1000  # in milliseconds
#         currruntimes_dj.append(elapsed_time)
#     # Calculate average runtime
#     average_runtime_dj = sum(currruntimes_dj) / len(currruntimes_dj)
#     rt_dijkstra_dense.append(average_runtime_dj)


#     for _ in range(3):  ## 3 trials for each graph size
#         graph_dense = generate_dense_graph(i)
        
#         start_time = time.perf_counter()
        
#         returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
#         end_time = time.perf_counter()
#         elapsed_time = (end_time - start_time) * 1000  # in milliseconds
#         currruntimes_bf.append(elapsed_time)
#     # Calculate average runtime
#     average_runtime_bf = sum(currruntimes_bf) / len(currruntimes_bf)
#     rt_bellmanford_dense.append(average_runtime_bf)
############################################################################################################

## tests for dijkstra and bellmanford on random sparse graphs
# for i in graph_sizes:
#     currruntimes_dj = [] 
#     currruntimes_bf = [] 

    
    
#     for _ in range(3):  ## 3 trials for each graph size
#         graph_sparse = generate_sparse_graph(i)
        
#         start_time = time.perf_counter()
        
#         returned_distance, returned_previous = dijkstra(graph_sparse, 'Node1')
        
#         end_time = time.perf_counter()
#         elapsed_time = (end_time - start_time) * 1000  # in milliseconds
#         currruntimes_dj.append(elapsed_time)
#     # Calculate average runtime
#     average_runtime_dj = sum(currruntimes_dj) / len(currruntimes_dj)
#     rt_dijkstrs_sparse.append(average_runtime_dj)


#     for _ in range(3):  ## 3 trials for each graph size
#         graph_sparse = generate_sparse_graph(i)
        
#         start_time = time.perf_counter()
        
#         returned_distance, returned_previous = bellman(graph_sparse, 'Node1')
        
#         end_time = time.perf_counter()
#         elapsed_time = (end_time - start_time) * 1000  # in milliseconds
#         currruntimes_bf.append(elapsed_time)
#     # Calculate average runtime
#     average_runtime_bf = sum(currruntimes_bf) / len(currruntimes_bf)
#     rt_bellmanford_sparse.append(average_runtime_bf)

###########################################################################################################################
 ## 
 
 ##testing runtimes for graphs of various edge dinsity
rt_bellmanford_dense_20 = []
rt_bellmanford_dense_40 = []
rt_bellmanford_dense_60 = []
rt_bellmanford_dense_80 = []

rt_dijkstras_dense_20 = []
rt_dijkstras_dense_40 = []
rt_dijkstras_dense_60 = []
rt_dijkstras_dense_80 = []

for i in graph_sizes:
    currruntimes_dj_20 = [] 
    currruntimes_dj_40 = []
    currruntimes_dj_60 = []
    currruntimes_dj_80 = []
    currruntimes_bf_20 = [] 
    currruntimes_bf_40 = [] 
    currruntimes_bf_60 = [] 
    currruntimes_bf_80 = [] 
    
    
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.20)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj_20.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj_20) / len(currruntimes_dj_20)
    rt_dijkstras_dense_20.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.40)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj_40.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj_40) / len(currruntimes_dj_40)
    rt_dijkstras_dense_40.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.60)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj_60.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj_60) / len(currruntimes_dj_60)
    rt_dijkstras_dense_60.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.80)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj_80.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj_80) / len(currruntimes_dj_80)
    rt_dijkstras_dense_80.append(average_runtime_dj)

    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.20)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf_20.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_bf_20) / len(currruntimes_bf_20)
    rt_bellmanford_dense_20.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.40)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf_40.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_bf_40) / len(currruntimes_bf_40)
    rt_bellmanford_dense_40.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.60)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf_60.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_bf_60) / len(currruntimes_bf_60)
    rt_bellmanford_dense_60.append(average_runtime_dj)
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i, 0.80)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf_80.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_bf_80) / len(currruntimes_bf_80)
    rt_bellmanford_dense_80.append(average_runtime_dj)


###########################################################################################################################
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# # First subplot for dense graphs
# ax1.plot(graph_sizes, rt_dijkstra_dense, marker='o', label='Dijkstra', color='blue')
# ax1.plot(graph_sizes, rt_bellmanford_dense, marker='o', label='Bellman Ford', color='red')
# ax1.set_title('Runtime Comparison on Dense Graphs')
# ax1.set_xlabel('Graph size (by # of nodes)')
# ax1.set_ylabel('Runtime (milliseconds)')
# ax1.set_xticks(graph_sizes)
# ax1.set_yticks([i * 5 for i in range(0, 10)])
# ax1.set_ylim(0, 50)
# ax1.grid()
# ax1.legend()

# # Second subplot for sparse graphs
# ax2.plot(graph_sizes, rt_dijkstrs_sparse, marker='o', label='Dijkstra', color='blue')
# ax2.plot(graph_sizes, rt_bellmanford_sparse, marker='o', label='Bellman Ford', color='red')
# ax2.set_title('Runtime Comparison on Sparse Graphs')
# ax2.set_xlabel('Graph size (by # of nodes)')
# ax2.set_ylabel('Runtime (milliseconds)')
# ax2.set_xticks(graph_sizes)
# ax2.set_yticks([i * 0.2 for i in range(0, 16)])
# ax2.set_ylim(0, 3.0)
# ax2.grid()
# ax2.legend()

# # Adjust the layout to prevent overlapping
# plt.tight_layout()

# # Show the plots
# plt.show()



#### graphing different density comparsisions

# variables = {
#     "rt_bellmanford_dense_20": rt_bellmanford_dense_20,
#     "rt_bellmanford_dense_40": rt_bellmanford_dense_40,
#     "rt_bellmanford_dense_60": rt_bellmanford_dense_60,
#     "rt_bellmanford_dense_80": rt_bellmanford_dense_80,
#     "rt_dijkstras_dense_20": rt_dijkstras_dense_20,
#     "rt_dijkstras_dense_40": rt_dijkstras_dense_40,
#     "rt_dijkstras_dense_60": rt_dijkstras_dense_60,
#     "rt_dijkstras_dense_80": rt_dijkstras_dense_80
# }

# for name, value in variables.items():
#     print(f"{name}: {value}")



plt.figure(figsize=(12, 6))  # Wider figure for better clarity

# Plotting the data
plt.plot(graph_sizes, rt_bellmanford_dense_20, marker='o', label='BF on .20 density', color='blue')
plt.plot(graph_sizes, rt_bellmanford_dense_40, marker='o', label='BF on .40 density', color='cyan')
plt.plot(graph_sizes, rt_bellmanford_dense_60, marker='o', label='BF on .60 density', color='skyblue')
plt.plot(graph_sizes, rt_bellmanford_dense_80, marker='o', label='BF on .80 density', color='dodgerblue')
plt.plot(graph_sizes, rt_dijkstras_dense_20, marker='o', label='DJ on .20 density', color='red')
plt.plot(graph_sizes, rt_dijkstras_dense_40, marker='o', label='DJ on .40 density', color='darkred')
plt.plot(graph_sizes, rt_dijkstras_dense_60, marker='o', label='DJ on .60 density', color='tomato')
plt.plot(graph_sizes, rt_dijkstras_dense_80, marker='o', label='DJ on .80 density', color='orange')

# Adding titles and labels
plt.title('Runtime Comparison of Dijkstras vs bellman ford with diffent graph density')
plt.xlabel('graph_sizes')
plt.ylabel('Runtime (milliseconds)')
plt.xticks(graph_sizes)  # Set x-ticks to the values in array_size
plt.yticks([i * 5 for i in range(0, 12)])  # Set y-ticks for clarity
plt.ylim(0, 60)  # Set y-axis limit from 0 to 20 ms
#plt.xscale('log')  # Use a logarithmic scale for x-axis
plt.grid()  # Optional: Add grid for better readability
plt.legend()  # Add legend

# Show the plot
plt.show()