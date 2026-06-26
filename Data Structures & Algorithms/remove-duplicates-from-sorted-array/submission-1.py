class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1=sorted(list(set(nums)))
        nums[:len(nums1)]=nums1
        return len(nums1)