# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3. For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Logic
# self.small (Max-Heap): Stores the smaller half of the numbers. Since Python's heapq only provides a min-heap by default, the code 
# simulates a max-heap by pushing the negated values of the numbers. self.large (Min-Heap): Stores the larger half of the numbers.
# How addNum(num) works: By default, every new number is pushed into the small heap (as a negative value).
# Ordering Check: It then checks if the heaps are out of order. If the largest number in the small heap (which is -self.small[0]) 
# is greater than the smallest number in the large heap (self.large[0]), that number belongs in the larger half. It pops the value 
#from small and pushes it into large.
# Size Balancing: To easily find the median, the two heaps must be balanced such that their sizes never differ by more than 1.
# If small has over 1 more element than large, it moves the top element from small to large.
# If large has over 1 more element than small, it moves the top element from large to small.
# How findMedian() works: Because the heaps are balanced, if one heap is larger than the other, the total number of elements is odd.
# The median is simply the top element of the heap with more elements. If the heaps are exactly the same size, the total number of 
# elements is even. The median is the average of the top element of the small heap and the top element of the large heap.

import heapq 

class MedianFinder:
    def __init__(self):
        self.small = [] #max_heap
        self.large = [] #min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, - num)
        if self.small and self.large and  -self.small[0] > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, - val)
        if len(self.small) - len(self.large) > 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, - val)
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, - val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return - self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + self.small[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# TC - O(logn) - insert / pop from heap
# SC - O(n)
