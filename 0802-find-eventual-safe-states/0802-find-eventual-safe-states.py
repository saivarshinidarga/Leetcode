from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        revg = [[] for _ in range(n)]
        out = [0] * n
        
        # Build reverse graph and outdegree
        for u in range(n):
            out[u] = len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        
        q = deque()
        for i in range(n):
            if out[i] == 0:
                q.append(i)
        
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True
            
            for nei in revg[node]:
                out[nei] -= 1
                if out[nei] == 0:
                    q.append(nei)
        res = []
        for i in range(n):
            if safe[i]:
                res.append(i)
        
        return res