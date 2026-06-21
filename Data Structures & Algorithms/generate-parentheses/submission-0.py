class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(oN, cN):
            if oN == cN == n:
                res.append(''.join(stack))
                return
            
            if oN < n:
                stack.append('(')
                backtrack(oN+1, cN)
                stack.pop()
            
            if cN < oN:
                stack.append(')')
                backtrack(oN, cN+1)
                stack.pop()
        
        backtrack(0,0)
        return res