class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        for i in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                length-=1
        k=length 
        return k
        