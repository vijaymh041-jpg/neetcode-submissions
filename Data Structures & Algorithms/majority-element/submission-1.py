from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=dict(Counter(nums))
        res=list(freq.keys())
        return res[0]
        
        