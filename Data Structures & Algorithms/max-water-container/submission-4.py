class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        result=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                inter = abs(min(heights[i],heights[j])*(i-j))
                if inter>result:
                    result=inter
            print(result)
        return result
        