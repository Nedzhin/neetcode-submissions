class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col = {}

        for word in strs:
            key = [0]*26
            for c in word:
                key[ord(c) - ord('a')] +=1
            
            tuple_key = tuple(key)
            if tuple_key in col:
                col[tuple_key].append(word)
            else:
                col[tuple_key] = [word]

        res = []
        for groups in col.values():
            res.append(groups)
            print(res)
        return res