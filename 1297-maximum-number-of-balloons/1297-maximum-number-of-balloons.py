class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counter = Counter(text)
        balloon_set = set("balloon")
        if len(balloon_set & counter.keys()) != 5:
            return 0
        
        counter['l'] //= 2
        counter['o'] //= 2

        return min(counter['b'],counter['a'],counter['l'],counter['o'],counter['n'])