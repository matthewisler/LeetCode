class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        zeros = 0
        left = 0
        for i in range(len(nums)):
            zeros += (nums[i] == 0)
            while zeros > 1:
                zeros -= (nums[left] == 0)
                left += 1
            max_length = max(max_length, i-left)
        return max_length