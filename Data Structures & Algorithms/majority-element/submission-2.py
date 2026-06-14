from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=dict(Counter(nums))
        idx=list(freq.values())
        res=list(freq.keys())
        for i in range(len(idx)):
            if idx[i]>len(nums)/2:
                return res[i]
        
        