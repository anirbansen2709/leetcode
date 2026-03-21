# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you
# need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

# Top-Down Dynamic Programming
1. The Setup (coinChange method)
# Initialization: It stores the coins array, sorts it (though sorting isn't strictly necessary for this specific DP approach to work, it's harmless here), and stores its length.
# The Cache (Memoization Table): It creates a 2D array called min_coins initialized with -1. Rows represent the target amount (from 0 to amount). Columns represent the coin index 
# (from 0 to len(coins)).
# Triggering the recursion: It kicks off the recursive helper function get_min_coins, starting with the last coin in the sorted array (self.length - 1) and the full target amount.
# Final Result: If the recursion returns infinity (float(inf)), it means no combination of coins can make up the amount, so it returns -1. Otherwise, it returns the calculated minimum coins.
# 2. The Recursive Engine (get_min_coins method)
# This function asks: "What is the minimum number of coins needed to make amount using only the coins from index 0 up to idx?"
# It follows these steps: Base Case (Only one coin type left): * if idx == 0: If we are looking at the very first coin in our list, we have no other options.
# If the remaining amount is perfectly divisible by this coin (amount % self.coins[idx] == 0), we return exactly how many of those coins we need (amount // self.coins[idx]).
# If it's not divisible, we can't make the exact change, so we return float('inf') (infinity) to represent an invalid path.
# Check the Cache: * if min_coins[amount][idx] != -1: If we've already solved this specific combination of amount and idx before, immediately return the saved answer. 
# This prevents redundant calculations.
# Explore Options (Take it or Leave it): * Leave it (dont_take): We decide not to use the coin at the current idx. We move on to the next available coin (idx - 1) but keep the amount the same.
# Take it (take): We check if the current coin is small enough to fit in the remaining amount (if amount >= self.coins[idx]). If it fits, we "take" one coin (adding 1 to our count) and 
# subtract its value from our amount.
# Crucial detail: Notice that the recursive call for take passes idx, not idx - 1. This is because we have an infinite supply of each coin, so we might want to use this exact same coin again.
# Record and Return: It compares the take and dont_take scenarios, picks the minimum value, saves it into the min_coins cache, and returns it up the chain.

class Solution:
    def get_min_coins(self, idx, amount, min_coins):
        if idx == 0:
            if amount % self.coins[idx] == 0:
                return amount // self.coins[idx]
            return float(inf)
        if min_coins[amount][idx] != -1:
            return min_coins[amount][idx]
        #dont take 
        dont_take = self.get_min_coins(idx - 1, amount, min_coins)
        take = float(inf)
        if amount >= self.coins[idx]:
            take = 1 + self.get_min_coins(idx, amount - self.coins[idx], min_coins)
        min_coins[amount][idx] = min(take, dont_take)
        return min_coins[amount][idx]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.coins.sort()
        self.length = len(coins)
        min_coins = [[-1 for _ in range(self.length + 1)] for _ in range(amount + 1)]
        answer = self.get_min_coins(self.length - 1, amount, min_coins)
        return answer if answer != float(inf) else -1

# TC - O(A * N) where A = amount and N = len(coins)
# SC - O(A * N)
