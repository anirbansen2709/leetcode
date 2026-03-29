# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# The solution iterates through the stock prices once. It maintains two key values: min_price: This variable tracks the lowest stock 
# price encountered up to the current day (Pi) being processed ( source). It's initialized to a very large number (float('inf')) to
# ensure the first price in the array becomes the initial min_price. max_profit: This variable stores the highest profit calculated so 
# far ( source). It's initialized to 0.
# In each step of the loop, for the current price (Pi):
# We update min_price to be the minimum of its current value and Pi​.
# We calculate the current_profit by subtracting the min_price (the lowest buying point encountered so far) from Pi
# We then update max_profit to be the maximum of its current value and this current_profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float(inf)
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# TC - O(n)
# SC - O(1)
