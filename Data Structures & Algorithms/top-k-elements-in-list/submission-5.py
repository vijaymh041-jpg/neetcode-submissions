class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        liso=[]
        if len(nums)==1 or nums==list(set(nums)):
            return nums
        for i in nums:
            if i not in liso:
                liso.append(i)
            else:
                res.append(i)
        nums=list(set(res))
        res=nums[:10]
        return res
            
        