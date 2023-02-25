class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        for i in range(len(prices)):
            if prices[i]>= mini: prices[i] = prices[i]-mini
            else: 
                mini = prices[i]
                prices[i] = 0 
        return max(prices)