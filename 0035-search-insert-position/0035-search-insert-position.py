class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        prev_lower = False
        if nums[0] > target:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target:
                prev_lower = True
            if nums[i] > target and prev_lower:
                return i
        return len(nums)