class Solution:
    def get_max_profit(self, idx, buy):
        if idx == self.length:
            return 0
        if buy:
            take = - self.prices[idx] + self.get_max_profit(idx + 1, False)
            dont = self.get_max_profit(idx + 1, True)
            profit = max(take, dont)
        else:
            take = self.prices[idx] + self.get_max_profit(idx + 1, True)
            dont = self.get_max_profit(idx + 1, False)
            profit = max(take, dont)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.length = len(prices)
        return self.get_max_profit(0, True)


# TC - O(exponential)

class Solution:
    def get_max_profit(self, idx, buy, max_prof):
        if idx == self.length:
            return 0
        if max_prof[buy][idx] != float('-inf'):
            return max_prof[buy][idx]
        if buy:
            take = - self.prices[idx] + self.get_max_profit(idx + 1, False, max_prof)
            dont = self.get_max_profit(idx + 1, True, max_prof)
            profit = max(take, dont)
        else:
            take = self.prices[idx] + self.get_max_profit(idx + 1, True, max_prof)
            dont = self.get_max_profit(idx + 1, False, max_prof)
            profit = max(take, dont)
        max_prof[buy][idx] = profit
        return max_prof[buy][idx]

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.length = len(prices)
        max_prof = [[float('-inf') for _ in range(self.length)] for _ in range(2)]
        return self.get_max_profit(0, True, max_prof)

# TC - O(2 * n)
# SC - O(2 * n)
