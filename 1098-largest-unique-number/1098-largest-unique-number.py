class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        for num in nums:
            if num not in counts:
                counts[num] = nums.count(num)
            

        counts = OrderedDict(sorted(counts.items(), key=lambda kv: kv[0], reverse=True))
        for num, freq in counts.items():
            if freq == 1:
                return num
        
        return -1
        