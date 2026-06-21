class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = defaultdict(int)
        c2= defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            c1[s[i]] +=1
            c2[t[i]] +=1
        
        if c1==c2:
            return True
        
        return False