class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = curr = ans = 0
        for i in range(0, k):
            curr += nums[i]
        ans = curr / k
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr/k)
        
        return ans