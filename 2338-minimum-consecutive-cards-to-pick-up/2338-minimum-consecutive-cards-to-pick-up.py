class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        from collections import defaultdict
        counts = defaultdict(list)
        for i in range(len(cards)):
            counts[cards[i]].append(i)

        ans = float("inf")
        for key in counts:
            arr = counts[key]
            for i in range(len(arr)-1):
                ans = min(ans, arr[i+1]-arr[i]+1)
        if ans == float("inf"):
            return -1
        return ans