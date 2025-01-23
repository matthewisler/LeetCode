class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        ans = 0
        jewels = [x for x in jewels]
        for i in range(len(stones)):
            if stones[i] in jewels:
                ans += 1
        return ans
