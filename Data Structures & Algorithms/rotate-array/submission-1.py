class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            buf=nums.pop()
            nums.insert(0,buf)
        


        
        
            
                



        """
        Do not return anything, modify nums in-place instead.
        """
        