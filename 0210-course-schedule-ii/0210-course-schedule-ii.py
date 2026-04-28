class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for s,d in prerequisites:
            adj[s].append(d)
        output = []
        cycle , completed = set() , set()
        def dfs(cur):
            if cur in completed:
                return True
            if cur in cycle:
                return False
            cycle.add(cur)
            for ne in adj[cur]:
               if dfs(ne) == False:
                  return False
            completed.add(cur)
            cycle.remove(cur)
            output.append(cur)
            return True
        for c in range(n):
            if dfs(c) == False:
                return []
        return output
     

