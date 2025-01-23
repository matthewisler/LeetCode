class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        sums = defaultdict(list)
        for i in range(len(nums)):
            num = [int(x) for x in str(nums[i])]
            sums[sum(num)].append(nums[i])
        
        curr = float("-inf")
        ans = float("-inf")
        for key, value in sums.items():
            if len(value) == 0 or len(value) == 1:
                continue
            value = sorted(value)
            ans = max(ans, value[-1] + value[-2])        

        if ans > float("-inf"):
            return ans
        else:
            return -1