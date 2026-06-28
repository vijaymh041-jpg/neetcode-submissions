class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k>0:
            buff=nums.pop()
            for i in range(0,len(nums)-2):
                nums[i+1]==nums[i]
            nums.insert(0,buff)
            k-=1
            
                



        """
        Do not return anything, modify nums in-place instead.
        """
        