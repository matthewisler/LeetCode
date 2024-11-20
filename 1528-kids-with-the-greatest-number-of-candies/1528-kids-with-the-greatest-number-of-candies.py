class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        with_extra_candy = [x+extraCandies for x in candies]
        max_candies = max(candies)
        ret_list = []
        for i in range(len(candies)):
            if with_extra_candy[i] >= max_candies:
                ret_list.append(True)
            else:
                ret_list.append(False)
        return ret_list