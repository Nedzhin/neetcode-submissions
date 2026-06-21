class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        aft = [1]
        for i in range(len(nums)):
            pref.append(pref[-1]*nums[i])
        
        for i in range(len(nums)-1,-1, -1):
            aft.append(aft[-1]*nums[i])
        print(len(pref))
        print(len(aft))
        print(len(nums))
        res = []
        for i in range(len(nums)):
            res.append(pref[i]*aft[len(nums)-i-1])
        return res
        