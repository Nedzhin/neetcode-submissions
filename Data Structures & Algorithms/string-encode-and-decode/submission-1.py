class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            for ch in word:
                res.append(ch)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res_list = []
        print(s)
        i = 0
        while i < len(s):
            l = int(s[i])
            i+=1
            while s[i] != '#':
                l = l *10 + int(s[i])
                i+=1

            i +=1
            j = i 
            cur =[]
            while i < j+l:
                cur.append(s[i])
                i+=1   
            res_list.append(''.join(cur))
            print(cur)
        return res_list
            
                