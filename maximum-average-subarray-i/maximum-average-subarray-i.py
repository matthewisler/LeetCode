class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = curr = ans = 0
        while right < k:
            curr += nums[right]
            right += 1
            
        ans = curr/k
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
        
            ans = max(ans, curr/k)
        
        return ans