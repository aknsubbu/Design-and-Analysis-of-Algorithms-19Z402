import heapq
import sys

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, val):
        self.size += 1
        heapq.heappush(self.heap, val)

    def pop(self):
        self.size -= 1
        return heapq.heappop(self.heap)

    def empty(self):
        return self.size == 0

    def top(self):
        return self.heap[0]
    
    def min(self):
        return self.heap[0]

def graphInput():
    graph = []
    n = int(input("Enter the number of vertices: "))
    startingVertex = int(input("Enter the starting vertex: "))
    for i in range(n):
        graph.append(list(map(int, input().split())))
    return graph, startingVertex, n


# graph, src, n = graphInput()
visited=set()

def possibleNeighbours(graph,src,n):
    w=[]
    for i in range(n):
        if graph[src][i]!=0:
            w.append(i)
    return w   


def dijkstra(graph, src, n):
    dist=[-1]*n
    dist[src]=0
    q=MinHeap()
    q.push((0,src))
    while not q.empty():
        d,u=q.pop()
        if u in visited:
            continue
        else:
            visited.add(u)
        w=possibleNeighbours(graph,u,n)
        for v in w:
            if dist[v]==-1:
                dist[v]=dist[u]+graph[u][v]
                q.push((dist[v],v))
            elif dist[v]>dist[u]+graph[u][v]:
                dist[v]=dist[u]+graph[u][v]
                q.push((dist[v],v))
    return dist

#testing 

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]]
src = 0
n = 9
print(dijkstra(graph, src, n))