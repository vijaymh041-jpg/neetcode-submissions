class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            if nums[i]+nums[j]==target:
                lis.append(i)
                lis.append(j)
                return lis
            j+=1
            if j==len(nums):
                i+=1
                j=i+1

        return lis
                    
        