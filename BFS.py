"""
This is my O(n) BFS-solution for finding the shortest reach between
2 nodes in a graph. Solves all test cases for problem "BFS: Shortest
Reach in a Graph", by pranav9413 on www.hackerrank.com
Author: William D. Stem
"""

from collections import deque

class Graph:
    def __init__(self, numNodes):
        self.n = numNodes
        self.edges = dict()
    def connect(self,i,j):
        self.edges.setdefault(i, []).append(j)
        self.edges.setdefault(j, []).append(i)
    def find_all_distances(self,start):
        visited = [False for _ in xrange(self.n)]
        distances = [-1 for _ in xrange(self.n)]
        queue = deque()
        queue.append((start, 0))
        while queue:
            (node, level) = queue.popleft()
            distances[node] = level*6
            level += 1
            if self.edges.has_key(node):
                for nextNode in self.edges[node]:
                    if not visited[nextNode]:
                        visited[nextNode] = True
                        queue.append((nextNode,level))
        distances.pop(start)
        print " ".join(map(str,distances))

t = input()
for i in xrange(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1, y-1)
    s = input()
    graph.find_all_distances(s-1)
