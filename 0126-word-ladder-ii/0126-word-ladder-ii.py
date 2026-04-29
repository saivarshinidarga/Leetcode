from collections import defaultdict, deque

class Solution:
    def findLadders(self, bw, ew, wl):
        if ew not in wl:
            return []

        wl.append(bw)

        # Build adjacency (pattern -> words)
        adj = defaultdict(list)
        for word in wl:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        # BFS to build level map
        queue = deque([bw])
        level_map = {bw: 1}

        while queue:
            cur = queue.popleft()
            step = level_map[cur]

            if cur == ew:
                break

            for i in range(len(cur)):
                pattern = cur[:i] + "*" + cur[i+1:]
                for ne in adj[pattern]:
                    if ne not in level_map:
                        level_map[ne] = step + 1
                        queue.append(ne)

        res = []

        # DFS to build paths
        def dfs(cur, path):
            if cur == bw:
                res.append(path[::-1])
                return

            step = level_map[cur]

            for i in range(len(cur)):
                pattern = cur[:i] + "*" + cur[i+1:]
                for ne in adj[pattern]:
                    if level_map.get(ne, 0) == step - 1:
                        dfs(ne, path + [ne])

        if ew in level_map:
            dfs(ew, [ew])
        res = [list(p) for p in set(tuple(p) for p in res)]
        return res