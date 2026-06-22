class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        product=1
        for i in range(len(nums)):
            temp=nums[i]
            nums[i]=1
            for j in range(len(nums)):
                product=product*nums[j]
            result.append(product)
            product=1
            nums[i]=temp
        return result

        