def bellman(graph, source):
    ## distance_from_start takes up O(V) space where v is total number of verticies in the graph
    distance_from_start = {v: float('inf') for v in graph}
    distance_from_start[source] = 0
    ##predecessor takes up O(V) space
    predecessor = {v: None for v in graph}  ## To track paths
    
    # Relax edges (V-1) times
    for _ in range(len(graph) - 1):  ## Iterate for V-1 times
        relaxed = False  # Flag to check if any relaxation occurs
        for u in graph:
            for v, weight in graph[u]:
                if distance_from_start[u] + weight < distance_from_start[v]:
                    distance_from_start[v] = distance_from_start[u] + weight
                    predecessor[v] = u
                    relaxed = True  ## A relaxation happened, so set the flag
        
        ##If no relaxation occurred, we can break early and prevent looping unnecessarily, because no more faster path is possible
        if not relaxed:
            break
                    
    
    # Check for negative weight cycles,, since we only perform (v-1) sweeps, we check if the v'th sweep makes ay relaxation to indicate -cycles
    for u in graph:
        for v, weight in graph[u]:
            if distance_from_start[u] + weight < distance_from_start[v]: ## if nodes are relaxed even after (v-1) loops, there is a negative cycle
                return "Negative weight cycle detected", None
    
    return distance_from_start, predecessor

def reconstruct_path(predecessor, source, target):
    path = []
    while target is not None:
        path.append(target)
        target = predecessor[target]
    path = path[::-1]  # Reverse the path
    if path[0] != source:
        return [] ## when there is no path from source to target
    return path



# book_graph = {  ## this was graph from the book
#     'S' : [('T', 10),('Y',5)],
#     'T' : [('Y', 2),('X',1)],
#     'X' : [('Z', 4)],
#     'Y' : [('T',2),('X',9),('Z',2)],
#     'Z' : [('S',7),('X',6)]      
# }

# # Run Bellman-Ford Algorithm
# distances, predecessors = bellman(graph_bellman, 'A')
# print("Bellman-Ford Distances:", distances)
# print("Bellman-Ford Path to D:", reconstruct_path(predecessors, 'A', 'S'))
