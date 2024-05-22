# Dynamic Programming 

Dynamic Programming is a method for solving a complex problem by breaking it down into simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure.

## Contents

- [Memoization](#memoization)
- [Litmus Test for Dynamic Programming](#litmus-test-for-dynamic-programming)
- [Bellman's Principle of Optimality](#bellmans-principle-of-optimality)
- [Steps to solve a Dynamic Programming Problem](#steps-to-solve-a-dynamic-programming-problem)
- [Multi-Stage Graphs](#multi-stage-graphs)
- [All Pairs Shortest Path](#all-pairs-shortest-path)
- [Bellman Ford Algorithm](#bellman-ford-algorithm)
- [Optimal Binary Search Tree](#optimal-binary-search-tree)


## Memoization

Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

-- follows the top-down approach...

## Litmus Test for Dynamic Programming

1. **Overlapping Subproblems**: The problem can be broken down into smaller subproblems which are reused several times.
2. **Optimal Substructure**: An optimal solution can be constructed from optimal solutions of its subproblems.

## Bellman's Principle of Optimality

An optimal policy has the property that whatever the initial state and initial state & initial decision are, the remaining decisions must constitute an optimal policy with regard to the state resulting from the first decision.

## Steps to solve a Dynamic Programming Problem

We find all the possible solutions to the subproblems and then choose the best one.

Mostly write iterative functions to avoid redundancy and the overhead of function calls.   

1. **Define the problem**: Define the problem and the subproblems.
2. **Guess**: Guess the solution for the subproblems.
3. **Relate subproblem solutions**: Recursively define the value of an optimal solution.
4. **Iterate/Memoize**: Either build a bottom-up table or use memoization to solve the problem.
5. **Solve the original problem**: Construct an optimal solution from the computed information.

##  Multi-Stage Graphs 

Multi-stage graphs are directed and weighted graphs where the nodes are divided into stages. We have to find the optimal path from the start to the end node.    

> Principle of Optimality holds for this problem because the optimal path from the start to the end node is the optimal path from the start to the next node and the optimal path from the next node to the end node.

We can keep track of cost by doing    ```COST (Stage , Node)```.  For nodes that are more than one edge away from the end node, we can add up all the possible costs and choose the minimum cost.   
 ***We always only calculate the cost from one stage to another. Then the optimal soltion can be taken as the optimal solution as the sum of the minimum cost of each stage.***

 Formula : -
 ```math
    COST (i,j) = min { COST (i+1,k) + c(i,j,k) } 
    --for all k in stage i+1    
```

Algorithm: -
```python
def multistage_graph(graph):
    n = len(graph) # number of vertices
    stages = [0] * (n + 1)
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)

    # Base case: vertices in the first stage
    for v in range(1, stages[1] + 1):
        dist[v] = 0

    # DP
    for u in range(1, n):
        for v in graph[u]:
            if dist[u] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[u] + v[1]
                parent[v[0]] = u

    # Reconstruct the path
    path = []
    end_vertex = n
    while end_vertex != -1:
        path.append(end_vertex)
        end_vertex = parent[end_vertex]

    return dist[n], path[::-1]

# Example usage
graph = {
    1: [(2, 2), (3, 1)],
    2: [(4, 5), (5, 7)],
    3: [(4, 4), (5, 2)],
    4: [(6, 1)],
    5: [(6, 3)],
    6: []
}
shortest_distance, shortest_path = multistage_graph(graph)
print("Shortest distance:", shortest_distance)
print("Shortest path:", shortest_path)

```

## All Pairs Shortest Path

The problem is to find the shortest path between all pairs of vertices in a graph. We can use the Floyd-Warshall algorithm to solve this problem.

The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. It is used to handle negative edge weights.

Algorithm: -
```c
    int dist[V][V], i, j, k;
    //dist [v][v] is the graph
    // V is the number of vertices
    // k is the intermediate vertex

    //here we assign the graph to the dist array
    for (i = 0; i < V; i++) {
        for (j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    // we iterate over all the vertices and find the shortest path
    for (k = 0; k < V; k++) {
        for (i = 0; i < V; i++) {
            for (j = 0; j < V; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
```


## Bellman Ford Algorithm

The Bellman Ford algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph. It is used to handle negative edge weights.

Time Complexity : - O(V*E) where V is the number of vertices and E is the number of edges.___This is slower than Dijkstra's Algorithm.___ O(N^2) to O(N^3) where N is the number of vertices.


## Optimal Binary Search Tree

Optimal Binary Search Tree is a binary search tree that provides the smallest possible search time for a given sequence of keys. The cost of a BST is the sum of the search costs of each key multiplied by its probability of being searched.

The Optimal Binary Search Tree problem can be solved using dynamic programming. We can use the following steps to solve the problem:

1. Define the subproblems: Define the subproblems and the subproblem space.
2. Guess: Guess the root of the optimal BST.
3. Relate subproblems: Recursively define the value of an optimal solution.
4. Iterate/Memoize: Either build a bottom-up table or use memoization to solve the problem.
5. Solve the original problem: Construct an optimal solution from the computed information.

Algorithm: -
```c
    int n = keys.length;
    int dp[n][n];
    for (int i = 0; i < n; i++) {
        dp[i][i] = freq[i];
    }
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k <= j; k++) {
                int cost = ((k > i) ? dp[i][k - 1] : 0) +
                           ((k < j) ? dp[k + 1][j] : 0) +
                           sum(freq, i, j);
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
```

