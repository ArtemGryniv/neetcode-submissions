class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {'[': ']', '(': ')', '{': '}'}

        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char != opens[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
            