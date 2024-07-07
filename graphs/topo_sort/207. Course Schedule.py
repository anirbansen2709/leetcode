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
        pre_map[crs] == []
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
