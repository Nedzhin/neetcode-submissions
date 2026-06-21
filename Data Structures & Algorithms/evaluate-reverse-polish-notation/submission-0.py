class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '*':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(o1*o2)
            elif t == '/':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(int(o1/o2))
            elif t == '-':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(o1-o2)
            elif t == '+':
                o2 = stack.pop()
                o1 = stack.pop()
                stack.append(o1+o2)
            else:
                stack.append(int(t))
        
        return stack[-1]