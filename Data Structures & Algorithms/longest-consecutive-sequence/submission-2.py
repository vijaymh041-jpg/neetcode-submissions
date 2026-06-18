class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        read=[]
        count=0
        if len(nums)==0:
            return 0
        else:
            val=nums[0]
        for i in range(len(nums)):
            if val in nums:
                count+=1
            else:
                read.append(count)
            val+=1
        return count
        
        