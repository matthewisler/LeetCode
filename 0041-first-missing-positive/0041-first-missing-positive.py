class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        output = len(nums)
        seen = [False] * (output + 1)
        
        for num in nums:
            if 0 < num <= output:
                seen[num] = True

        
        for i in range(1, output+1):
            if not seen[i]:
                return i

        return output+1