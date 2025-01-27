class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == stack[-1]:
                    stack.append(char)
                elif char.lower() == stack[-1].lower():
                    stack.pop()                
                else:
                    stack.append(char)
        return "".join(stack)