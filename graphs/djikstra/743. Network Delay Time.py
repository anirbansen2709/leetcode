from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distance = {idx : float(inf) for idx in range(1, n + 1)}
        distance[k] = 0

        graph = defaultdict(list)
        for src, dest, weight in times:
            graph[src].append((weight, dest))
        
        queue = [(0, k)]
        while queue:
            weight, node = heapq.heappop(queue)
            for neighbour_weight, neighbour in graph[node]:
                 new_weight = weight + neighbour_weight
                 if new_weight < distance[neighbour]:
                    distance[neighbour] = new_weight
                    heapq.heappush(queue, (new_weight, neighbour))

        answer = max(distance.values())
        return answer if answer != float(inf) else -1

# TC - O(V + ElogV)
# SC - O(V + E)
