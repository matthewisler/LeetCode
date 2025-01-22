class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans_set = set(nums)

        for i in range(len(ans_set)):
            if i not in ans_set:
                return i
        return len(ans_set)