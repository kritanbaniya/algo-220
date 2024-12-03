import random
 ## making graphs wont impact run time mesurements since its not included between start and stop of timer
def generate_sparse_graph(n_nodes): 
    ##Generate a sparse graph with  2.5 * n_nodes edges
    graph = {}
    
    ##Initialize all nodes
    for i in range(1, n_nodes + 1):
        node_name = f'Node{i}'
        graph[node_name] = []
    
    ##Ensure the graph is connected by creating a path through all nodes, to make it sparse
    for i in range(1, n_nodes):
        current_node = f'Node{i}'
        next_node = f'Node{i+1}'
        weight = random.randint(1, 10)
        
        # Add bidirectional edges  // basically undirected graphs
        graph[current_node].append((next_node, weight))
        graph[next_node].append((current_node, weight))
    
    ##Add a few random edges to make it bit more complex and not a 100% sparse graph
    extra_edges = n_nodes // 2
    for _ in range(extra_edges):
        node1 = f'Node{random.randint(1, n_nodes)}'
        node2 = f'Node{random.randint(1, n_nodes)}'
        if node1 != node2 and not any(edge[0] == node2 for edge in graph[node1]): ## making sure its not a self loop again 
                                                                                ##and that a node doesnt already existt between them
            weight = random.randint(1, 10)
            graph[node1].append((node2, weight))  ## again making it bidirectional
            graph[node2].append((node1, weight))
    
    return graph

def generate_dense_graph(n_nodes, chance = 0.80): ##default chance set to 80%
    ##Generate a dense graph with approximately n_nodes * (n_nodes-1) * %chance edges
    ## A complete graph with n_nodes had n_nodes*(n_nodes-1) edges, and a complete graph is the most denst it can get
    graph = {}
    
    # Initialize all nodes
    for i in range(1, n_nodes + 1):
        node_name = f'Node{i}'
        graph[node_name] = []
    
    # Add edges - each node will connect to about (varies when changing % chance) of other nodes
    for i in range(1, n_nodes + 1):
        node1 = f'Node{i}'
        for j in range(i + 1, n_nodes + 1):
            if random.random() < chance:  # % chance of edge creation, i dont want it to be a complete graph. 
                node2 = f'Node{j}'
                weight = random.randint(1, 10)
                graph[node1].append((node2, weight))  ## again, making it bidirectional
                graph[node2].append((node1, weight))
    
    return graph




# Sparse graphs
# sparse10 = generate_sparse_graph(10)
# sparse15 = generate_sparse_graph(15)
# sparse20 = generate_sparse_graph(20)
# sparse25 = generate_sparse_graph(25)
# sparse30 = generate_sparse_graph(30)
# sparse35 = generate_sparse_graph(35)
# sparse40 = generate_sparse_graph(40)
# sparse45 = generate_sparse_graph(45)
# sparse50 = generate_sparse_graph(50)

# # Dense graphs
# dense10 = generate_dense_graph(10)
# dense15 = generate_dense_graph(15)
# dense20 = generate_dense_graph(20)
# dense25 = generate_dense_graph(25)
# dense30 = generate_dense_graph(30)
# dense35 = generate_dense_graph(35)
# dense40 = generate_dense_graph(40)
# dense45 = generate_dense_graph(45)
# dense50 = generate_dense_graph(50)


# print ("sparse: ", sparse10)
# print ("Dense" , dense10)