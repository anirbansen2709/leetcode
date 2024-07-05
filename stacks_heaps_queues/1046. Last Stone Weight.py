import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, - stone)
        while len(stone_heap) > 1:
            y = heapq.heappop(stone_heap)
            x = heapq.heappop(stone_heap)
            if x != y:
                heapq.heappush(stone_heap, y - x)
        
        return - stone_heap[0] if len(stone_heap) else 0

# TC - O(n * logn)
# SC - O(n)
