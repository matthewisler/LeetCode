class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import defaultdict

        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        
        return len(set(counts.values())) == 1