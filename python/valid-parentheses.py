# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in d.values():
                stack.append(c)
            if c in d.keys():
                if not stack or stack[-1] != d[c]:
                    return False
                else:
                    stack.pop(-1)
        if stack:
            return False
        return True