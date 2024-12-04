class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = [0]*26
        t_dict = [0]*26

        for ch in s:
            s_dict[ord(ch) - ord('a')] += 1

        for ch in t:
            t_dict[ord(ch) - ord('a')] += 1
        
        return s_dict == t_dict
        