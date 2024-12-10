class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_count = 1
        count = 1
        first_thru = True
        if len(nums) == 0:
            return 0

        for num in sorted_nums:
            if first_thru:
                prev_num = num
                first_thru = False
            else:
                if prev_num + 1 == num:
                    count += 1
                    max_count = max(count, max_count)
                else:
                    if prev_num == num:
                        continue
                    else:
                        count = 1
            prev_num = num
        return max_count