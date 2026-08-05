class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = []
        if sorted(prices, reverse=True)==prices:
            return 0
        for i in range(len(prices)):
            for j in range(1,len(prices)):
                result.append(prices[j]-prices[i])
        return max(result)


        