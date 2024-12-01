class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count_note = {}
        char_count_magazine = {}
        for char in ransomNote:
            if char in char_count_note:
                char_count_note[char] += 1
            else:
                char_count_note[char] = 1
        
        for char in magazine:
            if char in char_count_magazine:
                char_count_magazine[char] += 1
            else:
                char_count_magazine[char] = 1
        
        for char in ransomNote:
            if char in magazine and char_count_note[char] <= char_count_magazine[char]:
                continue
            else:
                return False
        return True
