class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in dic:
                return [i, dic[complement]]

            dic[num] = i
        
