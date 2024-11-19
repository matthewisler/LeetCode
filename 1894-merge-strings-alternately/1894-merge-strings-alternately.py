class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        word1_list = [x for x in word1]
        word2_list = [x for x in word2]
        word1_range = len(word1_list)
        word2_range = len(word2_list)
        word_range = max(word1_range, word2_range)
        for i in range(word_range):
            if i>=word1_range:
                pass
            else:
                merged.append(word1[i])
            if i>=word2_range:
                pass
            else:
                merged.append(word2[i])
        return "".join(merged)
            

        