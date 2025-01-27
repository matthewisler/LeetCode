class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque

        increasing = deque()
        decreasing = deque()
        left = 0
        ans = 0

        for i in range(len(nums)):
            while increasing and nums[i] < increasing[-1]:
                increasing.pop()
            while decreasing and nums[i] > decreasing[-1]:
                decreasing.pop()
            
            increasing.append(nums[i])
            decreasing.append(nums[i])

            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1
            
            ans = max(ans, i - left + 1)
        return ans