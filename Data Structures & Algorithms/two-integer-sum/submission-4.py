class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        i=0
        j=1
        while i<len(nums):
            if nums[i]+nums[j]==target:
                lis.append(i)
                lis.append(j)
            else:
                j+=1
            if j==len(nums)-1:
                i+=1
                j=i+1
            
        return lis
                    
        