class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s_list = [x for x in s]
        found_vowels = []
        count = 0
        for char in s:
            if char in vowels:
                found_vowels.append(char)
        print(found_vowels)
        for i in range(len(s)):
            if s[i] in vowels:
                s_list[i] = found_vowels[len(found_vowels)-(1+count)]
                count += 1
        return "".join(s_list)
