from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        one_odd = False

        for x in counts.values():
            if x%2==1 and not one_odd:
                one_odd = True
            elif x%2==1:
                return False
        return True