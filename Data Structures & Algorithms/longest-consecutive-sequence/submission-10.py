class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        count=1
        if len(nums)==1:
            return 1
        for i in range(len(nums)):
            j=i+1
            if j<len(nums) and nums[j]-nums[i]==1:
                count+=1
            else:
                if result<count:
                    result=count+1
                count=1
            
        return result
        