class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        con = set()
        for num in nums:
            if num not in con:
                con.add(num)
            else:
                return True
        
        return False
         