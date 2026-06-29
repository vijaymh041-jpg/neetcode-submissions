class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=i+1
        while i<len(nums)-1:
            if nums[i]==nums[j] and abs(i-j)<=k:
                print(i,j)
                return True
            j+=1
            if j==len(nums):
                i+=1
                j=i+1


                
        return False
        