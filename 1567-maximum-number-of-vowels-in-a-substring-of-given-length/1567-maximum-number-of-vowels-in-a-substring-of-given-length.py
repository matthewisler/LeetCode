class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = 'aeiou'
        for letter in s[:k]:
            if letter in vowels:
                count += 1
        
        max_count = count
        #max_count is the max value for the first iteration
        for starting_letter in range(0,len(s)-k):
            if s[starting_letter] in vowels:
                count -= 1
            if s[starting_letter+k] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count

