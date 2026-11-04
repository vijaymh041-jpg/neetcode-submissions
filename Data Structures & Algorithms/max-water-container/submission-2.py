class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        result=[]
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                result.append(abs(min(heights[i],heights[j])*(i-j)))
        return max(result)
        