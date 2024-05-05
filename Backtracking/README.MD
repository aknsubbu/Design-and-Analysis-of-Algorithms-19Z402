# Backtracking 

This invloves a systematic search for a solution to a problem. It is a class of algorithms that considers searching every possible combination to solve a problem. It is a brute force approach to solve a problem.

Follows Depth First Search (DFS) approach to solve the problem. 

## Contents

- [State Space Tree](#state-space-tree)
- [N-Queens Problem](#n-queens-problem)
- [Graph Coloring](#graph-coloring)
- [Sum of Subsets](#sum-of-subsets)



We use a State Space Tree to solve the problem. The tree is a representation of all the possible solutions to the problem. The tree has the following properties:
- The root node represents the initial state of the problem.
- The branches represent the possible moves from the current state.
- The leaf nodes represent the final state of the problem.

There are two ways to show the solution:
1. **Fixed Size Tuple** : We can use a fixed size tuple to represent the state of the problem. We can then use the tuple to represent the state of the problem.
Example: ```(1 0 1 0 1)``` This tuple represents the state of the problem.
The elements in the tuple that are 1 represent the solution to the problem from the sample space. 

2. **Variable Size Tuple** : We can use a variable size tuple to represent the state of the problem. We can then use the tuple to represent the state of the problem.
Example: ```(1,5,6)``` This tuple represents the state of the problem where we consider the elements at the index 1,5,6 from the sample space.

## N-Queens Problem

The N-Queens problem is a classic problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

Algorithm: -
```
    int n // number of queens
    int board[n][n] // chess board
    int solSet[n] // solution set

    bool checkSafe (int board[][], int solSet, int row, int col) {
        // check if the queen can be placed at the given position
        if (board[row][col] == 1) {
            return false;
        }
        for (int i = 0; i < n; i++) {
            if (board[row][i] == 1) {
                return false;
            }
            if (board[i][col] == 1) {
                return false;
            }
            if (board[row+i][col+i] == 1) {
                return false;
            }
            if (board[row-i][col-i] == 1) {
                return false;
            }
            if (board[row+i][col-i] == 1) {
                return false;
            }
            if (board[row-i][col+i] == 1) {
                return false;
            }
        }
        return true;

    }

    bool solveNQueens (int board[][], int solSet, int row) {
        if (row >= n) {
            return true;
        }
        for (int i = 0; i < n; i++) {
            if (checkSafe(board, solSet, row, i)) {
                board[row][i] = 1;
                if (solveNQueens(board, solSet, row+1)) {
                    return true;
                }
                board[row][i] = 0;
            }
        }
        return false;
    }


```

## Graph Coloring

Graph coloring is a way of coloring the vertices of a graph such that no two adjacent vertices have the same color.

Algorithm: -
```
    int n // number of vertices
    int graph[n][n] // graph
    int color[n] // color of the vertices

    bool checkSafe (int graph[][], int color[], int vertex, int c) {
        for (int i = 0; i < n; i++) {
            if (graph[vertex][i] == 1 && c == color[i]) {
                return false;
            }
        }
        return true;
    }

    bool graphColoring (int graph[][], int color[], int vertex) {
        if (vertex >= n) {
            return true;
        }
        for (int i = 0; i < n; i++) {
            if (checkSafe(graph, color, vertex, i)) {
                color[vertex] = i;
                if (graphColoring(graph, color, vertex+1)) {
                    return true;
                }
                color[vertex] = -1;
            }
        }
        return false;
    }

```

## Sum of Subsets

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Algorithm: -
```
    int n // number of elements
    int set[n] // set of elements
    int sum // sum to be found
    int solSet[n] // solution set

    bool sumOfSubsets (int set[], int solSet[], int n, int sum, int currSum, int currIndex) {
        if (currSum == sum) {
            return true;
        }
        if (currIndex >= n || currSum > sum) {
            return false;
        }
        for (int i = currIndex; i < n; i++) {
            solSet[i] = 1;
            if (sumOfSubsets(set, solSet, n, sum, currSum+set[i], i+1)) {
                return true;
            }
            solSet[i] = 0;
        }
        return false;
    }

```

