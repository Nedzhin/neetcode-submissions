class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pref = [1]
        # aft = [1]
        # for i in range(len(nums)):
        #     pref.append(pref[-1]*nums[i])
        
        # for i in range(len(nums)-1,-1, -1):
        #     aft.append(aft[-1]*nums[i])
        # res = []
        # for i in range(len(nums)):
        #     res.append(pref[i]*aft[len(nums)-i-1])
        # return res
        
        res = [1]*len(nums)
        
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]

        return res