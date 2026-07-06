class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high=len(prices)
        i=0
        temp=0
        profit=0
        while i<high-1:
            if prices[i]<prices[i+1]:
                temp=prices[i+1]-prices[i]
                profit+=temp
            i+=1
        return profit
        