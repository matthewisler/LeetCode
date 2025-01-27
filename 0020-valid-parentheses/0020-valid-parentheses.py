class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for char in s:
            if char in mapping:
                stack.append(char)
            
            else:
                if not stack:
                    return False
                
                prev_char = stack.pop()
                if char != mapping[prev_char]:
                    return False
                
        return not stack
        