class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_hash = {}
        for i,value in enumerate(nums):
            if value in num_hash and i - num_hash[value] <= k:
                return True
            else:
                num_hash[value] = i
        return False