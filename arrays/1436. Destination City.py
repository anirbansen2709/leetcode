class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest_set = set()
        src_set = set()
        for src, dest in paths:
            if src in dest_set:
                dest_set.remove(src)
            else:
                src_set.add(src)
            if dest in src_set:
                src_set.remove(dest)
            else:
                dest_set.add(dest)
        return list(dest_set)[0]

# TC - O(N)
# SC - O(N)
