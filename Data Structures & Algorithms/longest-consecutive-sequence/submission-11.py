class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
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
                    result=count
                count=1
            
        return result
        