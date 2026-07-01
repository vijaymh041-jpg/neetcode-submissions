class Solution:
    def maxArea(self, heights: List[int]) -> int:
        buffer=list(set(heights))
        if len(buffer)==1:
            return buffer[0]*buffer[0]
        first=buffer[-1]
        second=buffer[-2]
        print(first,second)
        area=min(first,second)*(abs(heights.index(first)-heights.index(second)))
        return area