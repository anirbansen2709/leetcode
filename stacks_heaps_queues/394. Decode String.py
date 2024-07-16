class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                current = ''
                while stack:
                    val = stack.pop()
                    if val == '[':
                        break
                    current = val + current
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                decoded = current * int(num)
                stack.append(decoded)
        return ''.join(stack)
