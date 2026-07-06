from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        arr=Counter(nums)
        keys=list(arr.keys())
        values=list(arr.values())
        for i in range(len(values)):
            if values[i]>len(nums)//3:
                result.append(keys[i])
        return result
        
        