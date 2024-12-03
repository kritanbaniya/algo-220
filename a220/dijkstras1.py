import heapq

def dijkstra(graph, source):
    ##predecessor takes up O(V) space and O(V) time
    predecessor = {v: None for v in graph}  # To track paths, so we can reconstruct path from a note to another node
    ##Visited takes up O(V) space and O(V) time
    Visited = {v: False for v in graph}
    ## distance_from_start takes up O(V) space where v is total number of verticies in the graph
    distance_from_start = {v: float('inf') for v in graph} ## initiliazing distance from source to all nodes as infinity in the begining
    distance_from_start[source] = 0 ## changing distance from source to cource to 0
    
    priority_queue = [(0, source)]  # (distance, vertex)
    
    
    while priority_queue:  ##takes up to  O(E log E) time
        current_distance, current_vertex = heapq.heappop(priority_queue) ## O(log E),the greedy step, which is why it sometimes fails for graph with negative edges
        Visited[current_vertex] = True
        
        # Skip if the distance is not optimal, this happens when there are dupes of vertex in priority queu with worse distances
        if current_distance > distance_from_start[current_vertex]: ## is there is already a better recorded distance for this vertex, skip next steps
            continue
        
        # Relax neighbors
        for neighbor, edge_weight in graph[current_vertex]:  ## iterating through the current vertext's neighbors
            if Visited[neighbor]:                              ## this also makes it so the program terminates even if there is a negative cyce
                continue
            distance = current_distance + edge_weight
            if distance < distance_from_start[neighbor]:
                distance_from_start[neighbor] = distance
                predecessor[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor)) ## the book uses decrease key (O(log n)), but we will used heap push (O(log n)), 
                                                                   
                                                                    
    return distance_from_start, predecessor 
    ## distance_from_start is the dictionary with Vertext and shortest path (length) to vertext from start.
    ## predecessor is the dictionary with the previous node of a vertext, it is used to re-construct the acctual path shortest from start to node

def reconstruct_path(predecessor, source, target):
    path = []
    while target is not None:
        path.append(target)
        target = predecessor[target]
    path = path[::-1]  # Reverse the path
    if path[0] != source:
        return [] ## when there is no path from source to target
    return path



# Run Dijkstra's Algorithm
# distances, predecessors = dijkstra(book_graph, 'S')
# print("Dijkstra's Distances:", distances)
# print("Dijkstra's Path to D:", reconstruct_path(predecessors, 'S', 'Z'))


# distances, predecessors = dijkstra(graph_dijkstra, 'A')
# print("Dijkstra's Distances:", distances)