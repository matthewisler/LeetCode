class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        note_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)

        return note_counter <= mag_counter
