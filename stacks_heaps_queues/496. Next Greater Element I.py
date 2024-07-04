class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length = len(nums2)
        nge = dict()
        stack = []
        answer = []
        for idx in range(length - 1, -1, -1):
            while stack and stack[-1] <= nums2[idx]:
                stack.pop()
            if stack:
                nge[nums2[idx]] = stack[-1]
            stack.append(nums2[idx])

        for num in nums1:
            if num in nge:
                answer.append(nge[num])
            else:
                answer.append(-1)

        return answer

# TC - O(n)
# SC - O(n)
