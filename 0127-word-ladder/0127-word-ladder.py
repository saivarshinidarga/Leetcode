from collections import deque

class Solution(object):
    def ladderLength(self, bw, ew, wl):
        if ew not in wl:
            return 0
        
        wl.append(bw)
        adj = {}
        
        # Build pattern dictionary
        for word in wl:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj.setdefault(pattern, []).append(word)
        
        queue = deque([bw])
        visited = set([bw])
        res = 1
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for i in range(len(cur)):
                    pattern = cur[:i] + "*" + cur[i+1:]
                    
                    for ne in adj.get(pattern, []):
                        if ne == ew:
                            return res + 1
                        
                        if ne not in visited:
                            visited.add(ne)
                            queue.append(ne)
                    
                    # optimization: avoid revisiting
                    adj[pattern] = []
            
            res += 1
        
        return 0