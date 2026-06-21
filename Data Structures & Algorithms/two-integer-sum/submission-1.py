class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # res = [None]*2

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res[0] = i
        #             res[1] = j
        #             return res
        
        col = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in col:
                return [col[diff], i]
            col[n] = i