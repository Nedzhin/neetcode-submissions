class Solution:
    def climbStairs(self, n: int) -> int:
        col = [0]*(n+1)

        col[0] = 1
        col[1] = 1
        for i in range(2, n+1):
            col[i] = col[i-1] + col[i-2]  
        
        return col[n]
        