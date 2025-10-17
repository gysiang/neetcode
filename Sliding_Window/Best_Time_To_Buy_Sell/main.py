from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return (0)
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            current_profit = prices[i] - min_price
            if (current_profit > max_profit):
                max_profit = current_profit
            elif (min_price > prices[i]):
                min_price = prices[i]
        print(max_profit)
        return (max_profit)
                
c = Solution()
c.maxProfit([10,1,5,6,7,1])
