class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col = {}

        for word in strs:
            key = "".join(sorted(word))
            
            print(key)
            if key not in col:
                col[key] = []
            col[key].append(word)

        res = []

        for value in col.values():
            res.append(value)

        return res        