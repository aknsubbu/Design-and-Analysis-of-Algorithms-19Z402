def prims_algorithm(graph):
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
    
    def notVisited(graph,visited):
        notVisited = []
        for edge in graph:
            if edge[0] in visited and edge[1] in visited:
                continue
            notVisited.append(edge)
        return notVisited
    
    mst = []
    visited=set()
    graph = sorted(graph, key=lambda x: x[2])
    numVertices = len(set([x[0] for x in graph] + [x[1] for x in graph]))
    print("Number of vertices:", numVertices)
    mst.append(graph[0])
    visited.add(graph[0][0])
    visited.add(graph[0][1])
    
    while len(mst) < numVertices -1:
        neighbours = []
        notVisitedEdges = notVisited(graph,visited)
        for edge in mst:
            for e in notVisitedEdges:
                if edge[0] in e[:2] or edge[1] in e[:2]:
                    neighbours.append(e)
        smallest = smallest_edge(neighbours)
        if smallest and not inMST(smallest, mst):
            mst.append(smallest)
            visited.add(smallest[0])
            visited.add(smallest[1])
        else:
            break
    return mst

            






# Test cases
graph1 = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4),
          (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]

graph2 = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4)]

print("final")
print(prims_algorithm(graph1))
print(prims_algorithm(graph2))
