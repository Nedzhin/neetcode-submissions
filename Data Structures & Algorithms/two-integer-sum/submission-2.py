class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        col = {}

        for i in range(len(nums)):
            if target-nums[i] in col:
                return [col[target-nums[i]], i]
            else:
                col[nums[i]] = i
        
        
        