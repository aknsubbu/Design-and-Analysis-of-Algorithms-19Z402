# Design and Analysis of Algorithms

## This repository contains the code for the assignments of the course Design and Analysis of Algorithms (19Z402) from PSG College of Technology, Coimbatore.

## Table of Contents
**DIVIDE AND CONQUER** : 
- Introduction to Algorithm Design techniques 
- Divide and Conquer Methodology 
- Solving recurrence relations 
- Masters Theorem 
- Finding Maximum and Minimum Element 
- [Quick sort](#quick-sort)
- [Merge sort](#merge-sort) 
- [Convex Hull](#convex-hull)   

**GREEDY METHOD**: 
- Greedy Strategy
- Knapsack Problem 
- Minimum Spanning Trees
- Single Source Shortest Path Method 
- Huffman Trees    

**DYNAMIC PROGRAMMING** : 
- Principle of Optimality 
- Knapsack Problem 
- All Pairs Shortest Path 
- Optimal Binary Search Tree 
- Multistage Graphs   
  

**BACKTRACKING**: 
- State Space Tree 
- Knapsack Problem 
- The Eight Queens Problem 
- Sum of subsets 
- Graph Coloring    

**BRANCH AND BOUND** : 
- Bounding Functions 
- 0/1 Knapsack Problem 
- Traveling SalesPerson Problem 
- Assignment Problem


## Divide and Conquer Algorithm   
Divide and Conquer Algorithm breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems.    
Each subproblem should deal with the same issue as the main problem.    
Each recursion of the algorithm makes the problem smaller until it reaches a base case. The algorithm is split into three parts :
- Divide: This divides each problem into smaller problems allowing us to make the number of elements to be calcuated on smaller.
- Conquer: This allows us to perform the required operation on the elements and solve the subproblems by addressing the base case. 
- Combine: This is where we recombine all the parts of the problem to find our final result. 

### Merge Sort 
___
Merge Sort is based on the divide and conquer approach. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

Time Analysis:   
**Merge Sort Function**    
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Merge Function**
- Best Case: O(n)
- Average Case: O(n)
- Worst Case: O(n)


### Quick Sort
___
Quick Sort is based on the divide and conquer approach.   
The idea is to pick the first element as the pivot. We have to pick the second element as i and j as the last element. 
- Increment i till we find an element greater than the pivot.
- Decrement j till we find an element less than the pivot.
- Swap the elements at i and j.
- Repeat the process until i is greater than j.
- Swap the pivot with the element at j.


Time Analysis:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2)

Useful Youtube Vieo:    
[Quick Sort Algorithm by Abdul Badri](https://www.youtube.com/watch?v=7h1s2SojIRw)



### Convex Hull
___
Convex Hull is the smallest convex polygon that contains all the points in the set.
The algorithm is based on the divide and conquer approach.
- Find the bottem most point. 
- Sort the points based on the angle with the bottom most point.
- If two points have the same angle, then the point that is closer to the bottom most point is considered first.
- We insert the first two points into the stack.
- For the remaniang elements, if the angle is counter-clockwise we insert the point into the stack.
- If the angle is clockwise, we pop the top element from the stack and insert the point into the stack.
- The stack contains the convex hull of the points.
