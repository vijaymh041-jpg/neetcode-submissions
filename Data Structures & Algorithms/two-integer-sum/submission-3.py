class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        i=0
        while i<len(nums):
            j=i+1
            if nums[i]+nums[j]==target:
                lis.append(i)
                lis.append(j)
            if j==len(nums)-1:
                i+=1
        return lis
                    
        