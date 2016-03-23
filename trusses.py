 open(graph_file, r)
 crummy_code_to_reduce_graph_to_k_truss(graph_file, k)
    until no change do
        for each edge e = (a,b) in graph_file:
            if (size(intersection(neighbours(a), neighbours(b)) < k - 2:
                remove e from graph_file
    return remaining edges for each node \ 
