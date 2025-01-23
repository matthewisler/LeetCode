class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        ans = defaultdict(list)
        for word in strs:
            ans[tuple(sorted(word))].append(word)
        return list(ans.values())