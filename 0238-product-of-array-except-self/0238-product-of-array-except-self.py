class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy

        num_len = len(nums)
        answer = [1] * num_len

        prefix = 1
        for i in range(num_len):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(num_len-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer