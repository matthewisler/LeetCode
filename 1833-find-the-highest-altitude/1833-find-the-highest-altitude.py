class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        left = right = curr = 0
        ans = [gain[0]]
        for i in range(1, len(gain)):
            ans.append(ans[-1] + gain[i])
        return max(max(ans), 0)


        