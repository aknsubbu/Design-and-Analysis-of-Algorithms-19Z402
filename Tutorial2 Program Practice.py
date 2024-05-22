# nQueens Problem 

def nQueens(n):
    board = [['*' for _ in range(n)] for _ in range(n)]
    result = [] 

    def isSafe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
            
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
                
        return True
   
    def solve(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if isSafe(board, row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '*'
    
    solve(0)
    return result


for solution in nQueens(4):
    for row in solution:
        print(row)
    print()


# Floyd-Warshalls Algorithm
import copy 

def floyd_warshall(graph):
    n=len(graph)
    dist = copy.deepcopy(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = [[0, 5, float('inf'), 10],
            [float('inf'), 0, 3, float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]]
dist = floyd_warshall(graph)
print("Shortest distances between every pair of vertices:")
for row in dist:
    print(row)


# 0/1 Knapsack Problem

def knapsack(weight,value,capacity):
    n=len(weight)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(n+1):
        for w in range(capacity+1):
            if i==0 or w==0:
                dp[i][w]=0
            elif weight[i-1]<=w:
                dp[i][w]=max(value[i-1]+dp[i-1][w-weight[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]

weight=[10,20,30]
value=[60,100,120]
capacity=50
print(knapsack(weight,value,capacity))
