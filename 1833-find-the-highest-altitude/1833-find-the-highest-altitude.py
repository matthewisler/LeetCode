class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        ret_list = [0]
        for i, point in enumerate(gain):
            curr_alt += point
            ret_list.append(curr_alt)
        return max(ret_list)
        