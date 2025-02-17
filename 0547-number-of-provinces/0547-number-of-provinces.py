class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans 