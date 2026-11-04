class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        inter = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        inter.append(sorted([nums[i],nums[j],nums[k]]))
        for i in range(0,len(inter)):
            if inter[i] not in result:
                result.append(inter)
        return result

            
