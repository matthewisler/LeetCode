class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors = collections.defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        seen = [False] * n
        for node in restricted:
            seen[node] = True
        
        def dfs(curr_node):
            self.ans += 1
            seen[curr_node] = True

            for next_node in neighbors[curr_node]:
                if not seen[next_node]:
                    dfs(next_node)
        
        self.ans = 0
        dfs(0)
        return self.ans