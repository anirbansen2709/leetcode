class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if (bracket == ')' and stack[-1] != '(') or (bracket == ']' and stack[-1] != '[') or (bracket == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        if stack:
            return False
        return True

# TC - O(n)
# SC - O(n)
