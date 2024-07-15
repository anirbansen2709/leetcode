from collections import defaultdict, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        counts = [- count for count in task_count.values()]
        heapq.heapify(counts)
        queue = deque()
        intervals = 0
        while counts or queue:
            intervals += 1
            if counts:
                count = heapq.heappop(counts)
                count += 1
                if count:
                    queue.append((count, intervals + n))
            if queue and queue[0][1] == intervals:
                count, _ = queue.popleft()
                heapq.heappush(counts, count)
        return intervals
