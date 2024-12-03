class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern_dict = {}
        if len(words) != len(pattern):
            return False
        for word, pattern_char in zip_longest(words, pattern):
            if pattern_char in pattern_dict:
                if pattern_dict[pattern_char] != word:
                    return False
            elif word in pattern_dict.values():
                return False
            
            pattern_dict[pattern_char] = word

        return True