class Solution:
    def simplifyPath(self, path: str) -> str:
        list_vals = path.split("/")
        stack = []
        for directory in list_vals:
            if directory == ".":
                continue
            elif stack and directory == "..":
                stack.pop()
            else:
                if directory == "..":
                    continue
                if len(directory) > 0:
                    stack.append(directory)

        stack = [x for x in stack if len(x)>0]
        return '/'+'/'.join(stack)

