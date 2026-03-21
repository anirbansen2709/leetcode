# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# if n <= 2: return n: Handles the base cases. If there are 1 or 2 stairs, there are exactly 1 or 2 ways to climb them.
# first = 1, second = 2: Initializes the combinations for the previous two steps (n-2 and n-1). Tracking only these two variables
# instead of a full array keeps your space complexity at a highly optimized O(1).
# third = second + first: The core logic inside the loop. The number of ways to reach the current step is simply the sum of the ways
# to reach the previous two steps (Fibonacci pattern).
# first = second, second = third: Shifts your tracked steps forward by one to prepare for the next loop iteration.
# return second: Once the loop finishes at step n, second contains the final calculated combinations.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for _ in range(3, n + 1):
            third = second + first
            first = second
            second = third
        return second

# TC - O(n)
# SC - O(1)
