class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if token == "*":
                first = operands.pop()
                second = operands.pop()
                operands.append(second * first)
            elif token == "+":
                first = operands.pop()
                second = operands.pop()
                operands.append(second + first)
            elif token == "/":
                first = operands.pop()
                second = operands.pop()
                operands.append(int(second / first))
            elif token == "-":
                first = operands.pop()
                second = operands.pop()
                operands.append(second - first)
            else:
                operands.append(int(token))
        return operands[0]

# TC - O(n)
# SC - O(n)
