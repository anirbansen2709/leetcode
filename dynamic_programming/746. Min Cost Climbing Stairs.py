class Solution:
    def get_min_stairs(self, idx):
        if idx >= len(self.cost):
            return 0
        one = self.get_min_stairs(idx + 1)
        two = self.get_min_stairs(idx + 2)
        return self.cost[idx] + min(one, two)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        one = self.get_min_stairs(0)
        two = self.get_min_stairs(1)
        return min(one, two)

# TC - O(2^n)
# SC - O(n)

class Solution:
    def get_min_stairs(self, idx, min_costs):
        if idx >= len(self.cost):
            return 0
        if min_costs[idx] != float('inf'):
            return min_costs[idx]
        one = self.get_min_stairs(idx + 1, min_costs)
        two = self.get_min_stairs(idx + 2, min_costs)
        min_costs[idx] = self.cost[idx] + min(one, two)
        return min_costs[idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        min_costs = [float('inf') for _ in range(len(cost))]
        one = self.get_min_stairs(0, min_costs)
        two = self.get_min_stairs(1, min_costs)
        return min(one, two)
# TC - O(n)
# SC - O(2n)


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [float('inf') for _ in range(len(cost))]
        min_costs[-1] = cost[-1]
        min_costs[-2] = cost[-2]
        for idx in range(len(cost) - 3, -1, -1):
            min_costs[idx] = cost[idx] + min(min_costs[idx + 1], min_costs[idx + 2])
        return min(min_costs[0], min_costs[1])
# TC - O(n)
# SC - O(n)
