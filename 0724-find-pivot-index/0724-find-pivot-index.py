class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = right_sum = 0
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]+nums[i])
        
        for i in range(0, len(prefix)):
            if i == 0:
                left_sum = 0
                right_sum = prefix[-1] - nums[0]
            if i == len(prefix)-1:
                right_sum = 0
                left_sum = prefix[-1] - nums[len(nums)-1]
            if i > 0 and i<len(prefix)-1:
                left_sum = prefix[i-1]
                right_sum = prefix[len(prefix)-1] - prefix[i]
            if left_sum == right_sum:
                return i
        return -1
