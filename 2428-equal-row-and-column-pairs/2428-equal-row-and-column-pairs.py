class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        row_dic = defaultdict(int)
        for row in grid:
            row_dic[tuple(row)] += 1
        
        col_dic = defaultdict(int)
        for col in range(len(grid[0])):
            curr_coll = []
            for row in range(len(grid)):
                curr_coll.append(grid[row][col])
            
            col_dic[tuple(curr_coll)] += 1

        ans = 0
        for arr in row_dic:
            ans += row_dic[arr] * col_dic[arr]
        
        return ans