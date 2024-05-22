# Travelling Salesman Problem
 
 For solving minimization and maximization, we avoid backtracking. We will try to generate only the useful nodes... We will kill the nodes that are not nessecary. We pursue only the nodes that provide the best results. This allows us to reduce the number of calculations and imporve computational efficiency. 
 
 Given matrix should be reduced... 
 Write the minimum values for each row and subtract that minimum values from the row. 
 Do the same for the columns, so that after the coulmns mins are subtracted the mins for all the cols should be zero.   
 The sum of the row mins are now the approx min for the trip of the TS
 
 For State Space Tree....
 
We have to find the cost for each node. Upper Bound will be infinity initailly and will update when a leaf node is reached. 

'''
Cost of Node: cost of (i,j)+inital reduced cost + cost of reduction in the specific branch 
'''