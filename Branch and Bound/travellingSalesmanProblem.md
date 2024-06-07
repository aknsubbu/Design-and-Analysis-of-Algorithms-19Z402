# Travelling Salesman Problem
 
 For solving minimization and maximization, we avoid backtracking. We will try to generate only the useful nodes... We will kill the nodes that are not nessecary.    
 We pursue only the nodes that provide the best results. This allows us to reduce the number of calculations and imporve computational efficiency. 
 
 Given matrix should be reduced... 
 Write the minimum values for each row and subtract that minimum values from the row. 
 Do the same for the columns, so that after the coulmns mins are subtracted the mins for all the cols should be zero.   
 The sum of the row mins are now the approx min for the trip of the TS
 
 For State Space Tree....
 
We have to find the cost for each node. Upper Bound will be infinity initailly and will update when a leaf node is reached. 

```
Cost of Node: cost of (i,j)+inital reduced cost + cost of reduction in the specific branch 
```

* We will keep track of the minimum cost and the path that leads to that cost.

* We follow this in a recursive manner and expand only the children of the node that has the minimum cost.

* This reduces the number of computations required. The cost at the end of the tree  or the leaf node is the minimum cost for the trip.

* The path that leads to that cost is the path that we have to follow.

* The time complexity of this algorithm is O(n^2) and the space complexity is O(n^2) where n is the number of nodes in the graph.

