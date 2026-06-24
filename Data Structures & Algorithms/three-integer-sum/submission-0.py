class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        arr.append(nums[i])
                        arr.append(nums[j])
                        arr.append(nums[k])
            if arr!=[]:
                result.append(arr)
            arr=[]
        return result
        