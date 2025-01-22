class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for char in sentence:
            if char in dic:
                continue
            dic[char] = 1
        return len(dic) == 26