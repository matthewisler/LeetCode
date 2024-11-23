class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split(" ")
        output = ""
        for word in s_list:
            if len(word) > 0:
                output = word + " " + output
        return output.strip()
