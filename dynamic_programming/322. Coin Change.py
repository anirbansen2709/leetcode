# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you
# need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

# Top-Down Dynamic Programming
# 1. The Setup (coinChange method)
# Initialization: It stores the coins array and its length..
# The Cache (Memoization Table): It creates a 2D array called `dp` initialized with float('inf'). Rows represent the target amount (from 0 to amount). Columns represent the coin index 
# (from 0 to len(coins)).
# Triggering the recursion: It kicks off the recursive helper function `get_min_coins`, starting with the FIRST coin in the array (idx = 0) and the full target amount.
# Final Result: If the recursion returns infinity (float('inf')), it means no combination of coins can make up the amount, so it returns -1. Otherwise, it returns the calculated minimum coins.
# 2. The Recursive Engine (get_min_coins method)
# This function asks: "What is the minimum number of coins needed to make amount using only the coins from index `idx` up to the end of the array?"
# It follows these steps: 
# Base Case (Last coin type reached): 
# * if idx == self.length - 1: If we are looking at the very last coin in our list, we have no other options.
# If the remaining amount is perfectly divisible by this coin (amount % self.coins[idx] == 0), we return exactly how many of those coins we need (amount // self.coins[idx]).
# If it's not divisible, we can't make the exact change, so we return float('inf') (infinity) to represent an invalid path.
# Check the Cache: 
# * if dp[amount][idx] != float('inf'): If we've already solved this specific combination of amount and idx before, immediately return the saved answer. 
# This prevents redundant calculations.
# Explore Options (Take it or Leave it): 
# * Leave it (dont_take): We decide not to use the coin at the current idx. We move on to the next available coin (idx + 1) but keep the amount the same.
# * Take it (take): We check if the current coin is small enough to fit in the remaining amount (if amount >= self.coins[idx]). If it fits, we "take" one coin (adding 1 to our count) and 
# subtract its value from our amount.
# Crucial detail: Notice that the recursive call for `take` passes idx, not idx + 1. This is because we have an infinite supply of each coin, so we might want to use this exact same coin again.
# Record and Return: It compares the take and dont_take scenarios, picks the minimum value, saves it into the dp cache, and returns it up the chain.

class Solution:
    def get_min_coins(self, idx, amount, dp):
        if idx == self.length - 1:
            if (amount % self.coins[idx]) == 0:
                return amount // self.coins[idx]
            return float(inf)
        if dp[amount][idx] != float(inf):
            return dp[amount][idx]
        dont_take = self.get_min_coins(idx + 1, amount, dp)
        take = float(inf)
        if amount >= self.coins[idx]:
            take = 1 + self.get_min_coins(idx, amount - self.coins[idx], dp)
        dp[amount][idx] = min(dont_take, take)
        return dp[amount][idx]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.length = len(self.coins)
        dp = [[float(inf) for _ in range(self.length)] for _ in range(amount + 1)]
        answer = self.get_min_coins(0, amount, dp)
        return answer if answer != float(inf) else -1

# TC - O(A * N) where A = amount and N = len(coins)
# SC - O(A * N)
