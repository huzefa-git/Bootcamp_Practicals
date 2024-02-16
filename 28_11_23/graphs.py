# class graph:
#     def __init__(self,size):
#         self.size = size
#         self.matrix = [[0]*self.size for i in range(self.size)]
    
#     # def addedge(self,u,v):
#     #     self.matrix[u][v] = 1
#     #     self.matrix[v][u] = 1
    
#     def addedge1(self,u,v,w):
#         self.matrix[u][v] = w
#         self.matrix[v][u] = w

    # def printlist(self):
        # for i in self.matrix:
        #     print(i)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def addedge1(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))

    def printList(self):
        print(self.graph)
        for u,v in self.graph.items():
            print(u,"->",v)

    # def bfs(self,start):
    #     visited = set()
    #     queue = [start,0]
    #     while queue:
    #         vertex = queue.pop(0)
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             print(vertex)
    #             for neighbour in self.graph[vertex]:
    #                 queue.append(neighbour)
    def bfs(self,start):
        visited = set()
        queue = [(start,0)]
        while queue:
            vertex,weight = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex,weight)
                for neighbour,weight in self.graph[vertex]:
                    queue.append((neighbour,weight))
    def dfs(self,start):
        visited = set()
        queue = [(start,0)]
        while queue:
            vertex,weight = queue.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex,weight)
                for neighbour,weight in self.graph[vertex]:
                    queue.append((neighbour,weight))

g = Graph()
g.addedge1(1,2,3)
g.addedge1(1,3,5)
g.addedge1(2,4,6)
g.addedge1(2,5,7)
g.addedge1(2,8,8)
g.printList()
#g.bfs(1)
g.dfs(1)