class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        count=1
        result=0
        for i in range(len(nums)):
            j=i+1
            if j<len(nums) and abs(nums[i]-nums[j])==1:
                count+=1
            else:
                if result<count:
                    result=count
                count=1

        return result
        