class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        left_list = []
        right_list = []

        for num in nums1:
            if num not in nums2:
                if num not in left_list:
                    left_list.append(num)
        
        for num in nums2:
            if num not in nums1:
                if num not in right_list:
                    right_list.append(num)
        
        return [left_list, right_list]