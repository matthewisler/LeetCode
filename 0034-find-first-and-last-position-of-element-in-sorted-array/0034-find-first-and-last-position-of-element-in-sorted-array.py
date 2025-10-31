class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        if count == 0:
            return [-1,-1]
        
        
        

        start = nums.index(target)

        if count == 1:
            return [start, start]

        sorted_arr = sorted(nums, reverse = True)
        end = len(nums) - sorted_arr.index(target) - 1
        return [start, end]