class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            count=nums.count(nums[i])
            if count>len(nums)/3:
                arr.append(nums[i])
        return list(set(arr))
        