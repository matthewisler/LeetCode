class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        ans = []
        counts = defaultdict(int)
        for arr in nums:
            for x in arr:
                counts[x] += 1
        
        for key in counts:
            if counts[key] == len(nums):
                ans.append(key)
        
        return sorted(ans)