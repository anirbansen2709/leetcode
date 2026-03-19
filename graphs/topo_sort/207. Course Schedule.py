# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai. For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses.
# Otherwise, return false.

# Logic
# The problem asks whether you can finish all courses given their prerequisites, which essentially boils down to detecting if there is a cycle in a directed graph. If there is a cycle (e.g.,
# Course A requires Course B, and Course B requires Course A), you can never finish.Your code uses Depth-First Search (DFS) to find these cycles:Graph Construction: You create an adjacency 
# list (pre_map) using a defaultdict. For every course, you map it to a list of its immediate prerequisites.Cycle Detection (DFS): You iterate through every single course idx from $0$ to 
# $numCourses - 1$ and run the can_complete helper function.Tracking the Path: The visited set acts as your recursion stack. It keeps track of the courses you are currently visiting in your
# DFS path.Base Case 1 (Cycle Found): If you visit a course that is already in your visited set, you've looped back on yourself. You found a cycle, so you return False.Base Case 2 (Clear Path)
# : If a course has no prerequisites left (pre_map[crs] == []), it can definitely be completed. Return True.Backtracking: Once you've recursively checked all prerequisites for a specific 
# course and found no cycles, you remove it from the visited set (visited.remove(crs)) so it doesn't falsely trigger a cycle detection for parallel DFS paths.Optimization / Memoization: 
# Once a course is known to be completable, you clear its prerequisite list to avoid redundant work if another course requires it later.

from collections import defaultdict
class Solution:
    def can_complete(self, crs, visited, pre_map):
        if crs in visited:
            return False
        if pre_map[crs] == []:
            return True
        visited.add(crs)
        for nei in pre_map[crs]:
            if not self.can_complete(nei, visited, pre_map):
                return False
        visited.remove(crs)
        pre_map[crs] = []
        return True        

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        for idx in range(numCourses):
            visited = set()
            if not self.can_complete(idx, visited, pre_map):
                return False
        
        return True

# TC - O(V + E)
# SC - O(V + E)
