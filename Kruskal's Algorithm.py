def kruskal(num_nodes, edges):
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])  # Path compression
        return parent[i]

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    minimum_spanning_tree = []
    parent = [i for i in range(num_nodes)]  # Initialize parent array
    rank = [0] * num_nodes  # Initialize rank array to keep track of tree heights

    for edge in edges:
        node1, node2, weight = edge
        parent_node1 = find(parent, node1)
        parent_node2 = find(parent, node2)

        if parent_node1 != parent_node2:
            minimum_spanning_tree.append(edge)
            union(parent, rank, parent_node1, parent_node2)

    return minimum_spanning_tree

# Example usage:
num_nodes = 4
edges = [(0, 1, 4), (1, 2, 1), (0, 2, 3), (2, 3, 5), (3, 0, 2)]

minimum_spanning_tree = kruskal(num_nodes, edges)
print("Minimum Spanning Tree:", minimum_spanning_tree)
