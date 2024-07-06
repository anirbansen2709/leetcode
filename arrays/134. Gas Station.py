class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        start = 0
        for idx in range(length):
            total_gas += (gas[idx] - cost[idx])
            if total_gas < 0:
                total_gas = 0
                start = idx + 1
        return start 

# TC - O(n)
# SC - O(1)
