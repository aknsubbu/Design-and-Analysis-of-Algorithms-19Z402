def prims_algorithm(graph):
    def find_neighbours(mst, graph):
        neighbours = []
        if not mst:
            return neighbours
        for vertex in mst:
            for edge in graph:
                if vertex[0] in edge[:2] and vertex[1] not in edge[:2] and edge not in mst and edge not in neighbours:
                    neighbours.append(edge)
                elif vertex[1] in edge[:2] and vertex[0] not in edge[:2] and edge not in mst and edge not in neighbours:
                    neighbours.append(edge)
        return neighbours

    def smallest_edge(neighbours):
        if neighbours:
            sorted_neighbours = sorted(neighbours, key=lambda x: x[2])
            return sorted_neighbours[0]
        return None
    
    def inMST(edge, mst):
        for e in mst:
            if (edge[0], edge[1]) == (e[0], e[1]) or (edge[0], edge[1]) == (e[1], e[0]):
                return True
        return False
    
    mst = []  # Initialize MST
    graph = sorted(graph, key=lambda x: x[2])  # Sort the graph based on weights
    mst.append(graph[0])  # Add the edge with the smallest weight to MST

    while len(set([v for edge in mst for v in edge[:2]])) < len(set([v for edge in graph for v in edge[:2]])):
        neighbours = find_neighbours(mst, graph)
        smallest = smallest_edge(neighbours)
        if smallest and not inMST(smallest, mst):  # Check if the edge is not already in MST
            mst.append(smallest)
        
    return mst

# Test cases
graph1 = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4),
          (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]

graph2 = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4)]

print("final")
print(prims_algorithm(graph1))
print(prims_algorithm(graph2))
