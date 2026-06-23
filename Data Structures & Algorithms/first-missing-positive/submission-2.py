class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr=[]
        result=0
        nums=list(set(nums))
        for i in range(len(nums)):
            if nums[i]>-1:
                arr.append(nums[i])
        low=min(arr)
        high=max(arr)
        if low>1:
            return 1
        if low==high:
            return low+1
        for i in range(low,high+1):
            result+=i
        mid=sum(arr)
        if mid==result:
            return high+1
        return result-mid
            

            

        