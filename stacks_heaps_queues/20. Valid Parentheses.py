# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the 
# same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

# Initialize a Stack: It starts by creating an empty list called stack to store opening brackets.
# Iterate Through the String: It loops through each character (bracket) in the input string s one by one.
# Handle Opening Brackets: If the character is an opening bracket ((, [, or {), it pushes it onto the top of the stack using stack.append().
# Handle Closing Brackets: If the character is a closing bracket (e.g., ), ], or }), it performs a few checks:
# Empty Stack Check: If the stack is empty, it means we have a closing bracket with no preceding opening bracket to match it with. It immediately returns False.
# Mismatch Check: It checks if the current closing bracket matches the most recent opening bracket (which is sitting at the top of the stack at stack[-1]). If they don't match (for example,
# a ) trying to close a [), it returns False.
# Pop the Match: If the brackets do match, it removes that opening bracket from the top of the stack using stack.pop(), essentially crossing out that matched pair.
# Final Validation: After checking every character in the string, it checks if the stack is empty.
# If there are still items left in the stack, it means there were opening brackets that never found their closing partners, so it returns False.
# If the stack is completely empty, it means every bracket was perfectly matched and closed. It returns True.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(',']':'[', '}':'{'}
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return False if stack else True

# TC - O(n)
# SC - O(n)
