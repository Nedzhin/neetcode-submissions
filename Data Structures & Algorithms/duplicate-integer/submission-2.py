class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        col = set()

        for num in nums:
            if num in col:
                return True
            else:
                col.add(num)
        
        return False