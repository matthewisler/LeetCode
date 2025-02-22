class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        first = True
        for i in range(len(nums)):
            if first:
                first = False
                if nums[i] % 2 == 0:
                    prev_even = True
                else:
                    prev_even = False

            elif prev_even:
                if nums[i] % 2 == 0:
                    return False
                else:
                    prev_even = False
            
            else:
                if nums[i] % 2 == 0:
                    prev_even = True
                else:
                    return False
        return True
            