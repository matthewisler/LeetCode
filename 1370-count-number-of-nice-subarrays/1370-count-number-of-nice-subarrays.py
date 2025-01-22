class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        counts[0] = 1
        curr = ans = 0

        for num in nums:
            curr += num%2
            ans += counts[curr-k]
            counts[curr] += 1
        
        return ans