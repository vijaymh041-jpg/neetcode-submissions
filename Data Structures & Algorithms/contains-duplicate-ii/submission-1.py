class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        print(i)
                        print(j)
                        return True
                
        return False
        