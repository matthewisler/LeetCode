class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_arr = [x**2 for x in nums]
        return sorted(new_arr)