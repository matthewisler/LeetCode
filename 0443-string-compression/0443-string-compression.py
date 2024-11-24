class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            consecutive_run = 0
            while i <= len(chars)-1 and chars[i] == char:
                consecutive_run += 1
                i+=1
            if consecutive_run == 1:
                chars[index] = char
                index += 1
            else:
                chars[index] = char
                index += 1
                for digit in str(consecutive_run):
                    chars[index] = digit
                    index += 1
        chars[:] = chars[:index]
