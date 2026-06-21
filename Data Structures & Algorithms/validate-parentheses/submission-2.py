class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenth = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b in parenth:
                if stack and stack[-1] == parenth[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return True if not stack else False

        #     if b == '(' or b=='[' or b=='{':
        #         stack.append(b)
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         cur = stack.pop()
        #         if b == ')' and cur != '(':
        #             return False
        #         elif b == '}' and cur != '{':
        #             return False
        #         elif b == ']' and cur != '[':
        #             return False
        
        # if len(stack) == 0:
        #     return True
        # return False