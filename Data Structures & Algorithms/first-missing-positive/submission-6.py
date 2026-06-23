class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr=[]
        result=0
        nums=list(set(nums))
        for i in range(len(nums)):
            if nums[i]>-1:
                arr.append(nums[i])
        if len(arr)==0:
            return 1
        j=0
        while j<len(arr):
            if arr[0]>1:
                return 1
            elif arr[j]+1 not in arr:
                return arr[j]+1
            j+=1

        # if len(arr)==0:
        #     return 1
        # low=min(arr)
        # high=max(arr)
        # if low>1:
        #     return 1
        # if low==high:
        #     return low+1
        # for i in range(low,high+1):
        #     result+=i
        # mid=sum(arr)
        # if mid==result:
        #     return high+1
        # return result-mid
            

            

        