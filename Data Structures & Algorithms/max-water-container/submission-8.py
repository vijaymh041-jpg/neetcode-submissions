class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        result=0
        i=0
        j=len(heights)-1
        
        while i<j:
            inter = min(heights[i],heights[j])*(j-i)
            if inter>result:
                result=inter
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return result
        