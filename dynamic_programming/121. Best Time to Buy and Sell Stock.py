class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for idx in range(1, len(prices)):
            min_price = min(min_price, prices[idx - 1])
            profit = prices[idx] - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# TC - O(n)
# SC - O(1)
