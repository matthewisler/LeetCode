class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        ret_list = [0]
        for i, point in enumerate(gain):
            ret_list.append(curr_alt + point)
            curr_alt += point
        print(f"ret_list: {ret_list}")
        return max(ret_list)
        