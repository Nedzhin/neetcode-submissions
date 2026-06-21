class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == '(' or b=='[' or b=='{':
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if b == ')' and cur != '(':
                    return False
                elif b == '}' and cur != '{':
                    return False
                elif b == ']' and cur != '[':
                    return False
        
        if len(stack) == 0:
            return True
        return False