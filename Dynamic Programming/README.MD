# Dynamic Programming 

Dynamic Programming is a method for solving a complex problem by breaking it down into simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure.

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

## All Pairs Shortest Path

The problem is to find the shortest path between all pairs of vertices in a graph. We can use the Floyd-Warshall algorithm to solve this problem.

## Bellman Ford Algorithm

The Bellman Ford algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph. It is used to handle negative edge weights.

Time Complexity : - O(V*E) where V is the number of vertices and E is the number of edges.___This is slower than Dijkstra's Algorithm.___ O(N^2) to O(N^3) where N is the number of vertices.

