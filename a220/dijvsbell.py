import matplotlib.pyplot as plt
import time
from randgraph import generate_sparse_graph, generate_dense_graph
from bellmanford1 import bellman
from dijkstras1 import dijkstra


graph_sizes = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]

rt_dijkstra_dense = []                                      ##[1,2,3,4,5,6,7,8,9,10]
rt_dijkstrs_sparse = []                                     ##[2,3,4,5,6,7,8,9,10,11]

rt_bellmanford_dense = []                                   ##[3,4,5,6,7,8,9,10,11,12]
rt_bellmanford_sparse = []                                  ##[4,5,6,7,8,9,10,11,12,13]


## tests for dijkstra and bellmanford on random dense graphs 
for i in graph_sizes:
    currruntimes_dj = [] 
    currruntimes_bf = [] 
    
    
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj) / len(currruntimes_dj)
    rt_dijkstra_dense.append(average_runtime_dj)


    for _ in range(3):  ## 3 trials for each graph size
        graph_dense = generate_dense_graph(i)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_dense, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf.append(elapsed_time)
    # Calculate average runtime
    average_runtime_bf = sum(currruntimes_bf) / len(currruntimes_bf)
    rt_bellmanford_dense.append(average_runtime_bf)
##############################################

## tests for dijkstra and bellmanford on random sparse graphs
for i in graph_sizes:
    currruntimes_dj = [] 
    currruntimes_bf = [] 

    
    
    for _ in range(3):  ## 3 trials for each graph size
        graph_sparse = generate_sparse_graph(i)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = dijkstra(graph_sparse, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_dj.append(elapsed_time)
    # Calculate average runtime
    average_runtime_dj = sum(currruntimes_dj) / len(currruntimes_dj)
    rt_dijkstrs_sparse.append(average_runtime_dj)


    for _ in range(3):  ## 3 trials for each graph size
        graph_sparse = generate_sparse_graph(i)
        
        start_time = time.perf_counter()
        
        returned_distance, returned_previous = bellman(graph_sparse, 'Node1')
        
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        currruntimes_bf.append(elapsed_time)
    # Calculate average runtime
    average_runtime_bf = sum(currruntimes_bf) / len(currruntimes_bf)
    rt_bellmanford_sparse.append(average_runtime_bf)

##############################################


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First subplot for dense graphs
ax1.plot(graph_sizes, rt_dijkstra_dense, marker='o', label='Dijkstra', color='blue')
ax1.plot(graph_sizes, rt_bellmanford_dense, marker='o', label='Bellman Ford', color='red')
ax1.set_title('Runtime Comparison on Dense Graphs')
ax1.set_xlabel('Graph size (by # of nodes)')
ax1.set_ylabel('Runtime (milliseconds)')
ax1.set_xticks(graph_sizes)
ax1.set_yticks([i * 5 for i in range(0, 10)])
ax1.set_ylim(0, 50)
ax1.grid()
ax1.legend()

# Second subplot for sparse graphs
ax2.plot(graph_sizes, rt_dijkstrs_sparse, marker='o', label='Dijkstra', color='blue')
ax2.plot(graph_sizes, rt_bellmanford_sparse, marker='o', label='Bellman Ford', color='red')
ax2.set_title('Runtime Comparison on Sparse Graphs')
ax2.set_xlabel('Graph size (by # of nodes)')
ax2.set_ylabel('Runtime (milliseconds)')
ax2.set_xticks(graph_sizes)
ax2.set_yticks([i * 0.2 for i in range(0, 16)])
ax2.set_ylim(0, 3.0)
ax2.grid()
ax2.legend()

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Show the plots
plt.show()