class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high=len(prices)
        i=0
        temp=0
        profit=0
        for i in range(len(prices)):
            if i+1<len(prices) and prices[i]<prices[i+1]:
                temp=prices[i+1]-prices[i]
                profit+=temp
        return profit
        