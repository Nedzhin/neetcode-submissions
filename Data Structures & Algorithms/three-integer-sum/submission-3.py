class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        j = 0
        while j < len(nums)-2:
            l = j+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r] == 0 - nums[j]:
                    result.append([nums[j], nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1       
                elif nums[l] + nums[r] > 0-nums[j]:
                    r -=1
                else:
                    l+=1
            
            j+=1
            while nums[j-1] == nums[j] and j<len(nums)-2:
                j+=1
            
        
        return result
