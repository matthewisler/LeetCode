class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num>0]      
        output = len(nums)+1
        for i in range(1, output):
            if i not in nums:
                return i
        return output