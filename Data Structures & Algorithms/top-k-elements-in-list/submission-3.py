class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        liso=[]
        if len(nums)==1 or nums==list(set(nums)):
            return nums
        for i in range(len(nums)):
            if nums[i] not in liso:
                liso.append(nums[i])
            else:
                res.append(nums[i])
        nums=list(set(res))
        res=nums[:k]
        return res
            
        