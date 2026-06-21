class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        col = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            col[num] = 1 + col.get(num, 0)
        print(col)
        for num, times in col.items():
            freq[times].append(num)
        print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

