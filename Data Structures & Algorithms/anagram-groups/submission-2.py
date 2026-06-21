class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        col = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in col:
                col[sorted_word].append(word)
            else:
                col[sorted_word] = [word]

        res = []
        for groups in col.values():
            res.append(groups)
            print(res)
        return res