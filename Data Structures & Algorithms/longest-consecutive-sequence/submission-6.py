class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        count=0
        for i in range(len(nums)):
            j=i+1
            if j<len(nums) and nums[j]-nums[i]==1:
                count+=1
            else:
                if result<count+1:
                    result=count+2
                count=0
            
        return result
        