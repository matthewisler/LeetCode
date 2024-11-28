class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        substring = set()
        start_index = 0

        for end_index in range(len(s)):
            while s[end_index] in substring:
                substring.remove(s[start_index])
                start_index += 1

            substring.add(s[end_index])
            max_count = max(max_count, end_index - start_index + 1)
                
        return max_count