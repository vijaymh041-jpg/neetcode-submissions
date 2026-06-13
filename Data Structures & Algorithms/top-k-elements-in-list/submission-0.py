class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                res.append(nums[i])
        nums=list(set(res))
        res=nums[:k]
        return res
            
        