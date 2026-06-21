class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for l in s:
            if l not in dic1:
                dic1[l] = 0
            dic1[l] +=1

        for k in t:
            if k not in dic2:
                dic2[k] = 0
            dic2[k] +=1

        if dic1 == dic2:
            return True

        return False        